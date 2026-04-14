# CISC121_FINAL_PROJECT
GitHub repository for CISC121 final project: Playlist Vibe Builder - Declan Cameron

## 1.	Chosen Problem: Playlist Vibe Builder:

The Playlist Vibe Builder is an app that takes a list of songs and sorts them based on energy level, illustrating the reordering process until the final sorted playlist is achieved. This problem was chosen because I found it to have the most applicable daily use which can easily be implemented into preexisting apps for iteration. 

#### What the user will see during the simulation:

The user will see the current pivot at the end of the array highlighted in yellow which will be compared to the “I” pointe moving in purple to compare and swap items that are lower than the pivot. Once a partition is finished, the pivot and-or values in the correct positions will be highlighted green, while partitions continue on the unfinished smaller segments from left to untill the whole list is sorted green.

## 2.   Chosen Algorithm: Quick Sort:

The Quick Sort algorithm is implemented for the reordering process, utilizing a “divide and conquer” recursive approach to compare shrinking segments of the inputted list of songs. Quick sort was chosen because of its in-place sorting nature, minimizing the need for extra space while reordering O(1), and for its quick returning speed O(nlogn) for optimal user experience compared to other much slower algorithms.

#### The algorithm has the following preconditions:

- Each song must have an energy score from 0-100 to be used as numerical comparisons
  
- Minimum of two songs to be sorted, otherwise the app will return “already sorted” if one song is provided, or “empty list” when an empty list is provided. The app will check for these edge cases before running the main code.
  
#### And assumptions:

- All the energy scores are evaluated properly, making the inequalities during comparison accurate
## 3.   Demo Video:
 ***Video Demo uploaded in GitHub repository***

## 4.   Problem Breakdown & Computational Thinking:

#### Decomposition: 
The reordering process consists of 3 distinct steps: First portioning the full array using the last value in the array as the initial pivot; secondly, recursively repeating this process down the line for the sub arrays of smaller elements than the previous pivot; and lastly recursively repeating the process all the way back up the line for all the sub arrays of larger elements left on the stack.

#### Pattern Recognition: 
Quick sort utilizes a pointer system which keeps track of indices as it iterates, allowing us to use for or while loops for efficiency. This partition iteration is applied recursively for less than and greater than pivot sub array. 

#### Abstraction: 
The GUI only illustrates the highlighted indices in the array as they pass iterations and new sub arrays are assigned. Background work such as pointer comparison and temporary value holders do not need to be shown as the goal is to introductorily visualize and teach Quick Sort. 

#### Algorithm Design: 
Inputs: Recognizable, non-negative DICTIONARY of unorganized song titles with numerical score tied to each (0-100 energy). Constraints: if the input song list is less or equal to 1, early exit code and returns “already sorted” or “empty list”. Output: Completed sorted playlist by ascending energy with visualizations of the full sorting process. 

#### Process Flowchart:

***Flowchart uploaded in GitHub Repository***

## 5.    Steps to Run (local) + Requirements.tx 
#### Follow these steps to run Playlist Vibe Builder on your local computer:
1. Open your folder where you have saved the project files:
   
Example: cd path/to/your/folder

3. Run the following command in terminal to install Gradio from the requirements.txt provided:

pip install -r requirements.txt

4. Run the following command in terminal to launch the app using the Python script:

python app.py

5. Copy the https address provided by your terminal and paste it into your web browser to use the Playlist Vibe Builder!

#### Requirements.tx (uploaded in GitHub Repository):
gradio

## 6.   Hugging Face Link:
#### GitHub Repository Link: 
https://github.com/DeclanCameron/CISC121_FINAL_PROJECT.git
#### Hugging Face Link: 
https://declan999-cisc-121-project.hf.space

## 7.   Test Verification Cases:
#### Test #1: Initial test:
What you tested: If the initial code for the app ran correctly for a normal song list

Draft behavior: Invalid JSON String input even though the input formatting is correct and >=1.

Final behavior: The App correctly visualizes and renders a normal input list and sorts it correctly. Corrected line of code that states requested format to understand cuts in songs vs one big song

***Screenshots uploaded in GitHub repository***

Ai assisted improvement

#### Test #2: Empty list edge case:
What you tested: if an empty list input to the app outputs a valid error answer and explanation. App expected to output properly given the reused code line from the previous test.

Draft and final behavior: app outputs “Input is empty. Please enter some songs”, and error sign, correctly handling this edge case 

***Screenshots uploaded in GitHub repository***

No AI used

#### Test #3: List with only one song:
Expectations: The app should properly return that the playlist is already sorted because it consists of only one song.

Draft behavior: The app ran without crash. However, a logic error occurred as the final explanation text explained how Quick Sort sorted the list, even though it did not sort it at all. The output explanation associated with the base case of a single song list was bypassed.

Final code behavior: After fixing the if statement for the base case exit, the code ran as expected outputting “List has only one song; it is already sorted.”

***Screenshots uploaded in GitHub repository***

No AI used

## 8.    Author & Acknowledgment:
#### AUTHOR:
Name: Declan Cameron

Contact: 25bsqh@queensu.ca 

Queen’s ID: 20555462

#### ACKNOWLEDGEMENTS
Ai disclosure:

Ai Tools Used: Microsoft Copilot

Collection of chats used: https://copilot.microsoft.com/shares/DTxHspeonyyJ9VFEKaCJA

Influenced Project Parts: Ai was used in the implementation stage of coding the app.py file, allowing me to transfer my ideas into visual code, ready to be expressed via gradio. Clarity comments in the app.py file were self-written, as well as touch-up corrections throughout the file for desired output. Ai was used responsibly and as a co-driver throughout developing stage of the Playlist Vibe Builder. Setup stage and finalizations were self-driven.

External Sources/references: 

https://www.youtube.com/watch?v=5Sf2kQ89qsY

https://www.youtube.com/watch?v=elasjsgKkbWY

https://visualgo.net/en/sorting

https://huggingface.co/spaces/Rahatara/SimulateSearch

