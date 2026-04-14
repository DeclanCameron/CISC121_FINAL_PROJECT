import gradio as gr
import random

# Global variables for frames between button presses
animation_frames = []
current_index = 0

# VISUAL DESIGN - Convert JSON frames into a horizontal row of colored blocks

def render_frame_html(songs):

    color_map = {
        "PIVOT (Yellow)": "#FFD700",
        "POINTER I (Blue)": "#1E90FF",
        "POINTER J (Purple)": "#8A2BE2",
        "SWAPPED": "#FFA500",          # Orange for swapped blocks
        "CORRECT (Green)": "#32CD32",  # Only for blocks in final positions
        "normal": "#D3D3D3"
    }

    html = "<div style='display:flex; gap:10px; margin-top:10px;'>"

    for song in songs:
        title = song["title"]
        energy = song["energy"]
        status = song.get("status", "normal")
        color = color_map.get(status, "#D3D3D3")

        html += f"""
        <div style="
            width:120px;
            height:80px;
            background:{color};
            border-radius:8px;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            font-size:14px;
            font-weight:bold;
            text-align:center;
            border:2px solid black;
        ">
            {title}<br>({energy})
        </div>
        """

    html += "</div>"
    return html

# Input control and edge case handling for invalid lists

def parse_input(text):
    if not text or not text.strip():
        return None, "Input is empty. Please enter some songs."

    songs = []
    try:
        entries = text.split(";")
        for entry in entries:
            if not entry.strip():
                continue
            title, energy = entry.split(",")
            songs.append({
                "title": title.strip(),
                "energy": int(energy.strip()),
                "status": "normal"
            })
    except Exception:
        return None, "Invalid format. Use: Song Name,Energy; Song Name,Energy"

    return songs, None

# Quick sort algorithm with illustration built in

def quick_sort_visual(songs):
    frames = []
    
    if not songs: #base case for an empty list
        return frames, [], 
    
    if len(songs) == 1: #base case for a list with only one song
        frames.append({
            "message": "List has only one song; it is already sorted.",
            "songs": [dict(s) for s in songs] # Fixed bracket here
        })
        return frames, songs, "Sorted!"

    def partition(arr, low, high): #iteration part of quicksort per array
        pivot_val = arr[high]["energy"]
        arr[high]["status"] = "PIVOT (Yellow)"
        
        i = low - 1
        frames.append({
            "message": f"New Partition: Pivot is {arr[high]['title']} ({pivot_val})",
            "songs": [dict(s) for s in arr]
        })

        for j in range(low, high):
            arr[j]["status"] = "POINTER J (Purple)"
            frames.append({
                "message": f"Comparing {arr[j]['title']} ({arr[j]['energy']}) to pivot ({pivot_val})",
                "songs": [dict(s) for s in arr]
            })

            if arr[j]["energy"] <= pivot_val:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                arr[i]["status"] = "SWAPPED"
                frames.append({
                    "message": f"Swapping {arr[i]['title']} to the left side.",
                    "songs": [dict(s) for s in arr]
                })

            if arr[j].get("status") != "CORRECT (Green)":
                arr[j]["status"] = "normal"

        arr[i + 1], arr[high] = arr[high], arr[i + 1] #final pivot swap

        for item in arr:
            if item.get("status") != "CORRECT (Green)":
                item["status"] = "normal"

        # Make the final position of the moved pivot block now green
        arr[i + 1]["status"] = "CORRECT (Green)"

        frames.append({
            "message": "Pivot moved to final sorted position.",
            "songs": [dict(s) for s in arr]
        })

        return i + 1

    def solve(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            solve(arr, low, pi - 1)
            solve(arr, pi + 1, high)

    working_list = [dict(s) for s in songs]
    solve(working_list, 0, len(working_list) - 1)
    
    # last message for when all blocks are correctly positioned
    for item in working_list:
        item["status"] = "CORRECT (Green)"

    frames.append({
        "message": (
            "Sort Complete! The playlist is now fully sorted. "
            "Quick Sort achieved this by repeatedly selecting pivots and dividing the playlist "
            "into smaller and smaller sub‑arrays. Each pivot was placed into its permanent position "
            "as the algorithm moved left‑to‑right through the list, using recursion to sort every "
            "subsection until the entire playlist was ordered by energy."
        ),
        "songs": [dict(s) for s in working_list]
    })
    
    return frames, working_list, "Success"

# Animation Controls

def start_sort(text):
    global animation_frames, current_index

    songs, error = parse_input(text)
    if error:
        return error, "", "Error"

    frames, sorted_list, msg = quick_sort_visual(songs)

    animation_frames = frames
    current_index = 0

    if not frames:
        return "No steps to show.", "", "Frame 0 of 0"

    first = frames[0]
    return (
        first["message"],
        render_frame_html(first["songs"]),
        f"Frame 1 of {len(frames)}"
    )


def next_frame():
    global animation_frames, current_index

    if not animation_frames:
        return "No animation loaded. Please enter songs and press 'Start Sorting'.", "", ""

    if current_index < len(animation_frames) - 1:
        current_index += 1
    
    frame = animation_frames[current_index]

    return (
        frame["message"],
        render_frame_html(frame["songs"]),
        f"Frame {current_index+1} of {len(animation_frames)}"
    )


def prev_frame():
    global animation_frames, current_index

    if not animation_frames:
        return "No animation loaded.", "", ""

    if current_index > 0:
        current_index -= 1

    frame = animation_frames[current_index]

    return (
        frame["message"],
        render_frame_html(frame["songs"]),
        f"Frame {current_index+1} of {len(animation_frames)}"
    )

# Random Demo Playlist Generator

def generate_demo_list():
    titles = [
        "Uptown Funk", "Blinding Lights", "Levitating", "Bad Guy",
        "Shape of You", "Thunderstruck", "Viva La Vida",
        "Radioactive", "Believer", "Havana", "Stay"
    ]

    random.shuffle(titles)
    selected = titles[:9]

    demo_list = "; ".join(f"{title},{random.randint(0,100)}" for title in selected)

    return demo_list

# Gradio user interface

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎵 Playlist Vibe Builder — Step‑By‑Step Quick Sort")
    gr.Markdown(
        "Enter songs with their corresponding energy level in the format: `Uptown Funk,70`.<br>"
        "Enter multiple songs separated by semicolons.<br>"
        "Example: `Pop,80; Jazz,30; Rock,60`",
        elem_id="instructions"
    )

    with gr.Row():
        input_box = gr.Textbox(
            label="Enter songs",
            placeholder="Song A,55; Song B,20; Song C,90",
            scale=4
        )
        with gr.Column(scale=1):
            demo_btn = gr.Button("🎲 Generate Demo Playlist")
            start_btn = gr.Button("🚀 Start Sorting", variant="primary")
            next_btn = gr.Button("➡️ Next Step")
            prev_btn = gr.Button("⬅️ Back Step")

    msg_out = gr.Textbox(label="Status / Step Message", interactive=False)
    frame_counter = gr.Label(label="Progress Tracking")
    songs_out = gr.HTML(label="Visualization")

    demo_btn.click(
        fn=generate_demo_list,
        inputs=None,
        outputs=input_box
    )

    start_btn.click(
        fn=start_sort,
        inputs=input_box,
        outputs=[msg_out, songs_out, frame_counter]
    )

    next_btn.click(
        fn=next_frame,
        inputs=None,
        outputs=[msg_out, songs_out, frame_counter]
    )

    prev_btn.click(
        fn=prev_frame,
        inputs=None,
        outputs=[msg_out, songs_out, frame_counter]
    )

if __name__ == "__main__":
    demo.launch()