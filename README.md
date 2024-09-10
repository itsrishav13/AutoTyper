AutoTyper App


The AutoTyper App is a simple automation tool built with Python and Tkinter. It allows users to paste a block of text, specify how many times they want it typed, and control the typing speed to simulate human-like typing. The app can also automatically press "Enter" after each typed line if required.

Features
Input a custom text to be typed automatically.
Choose the number of repetitions for the text.
Set a delay before the typing begins.
Option to press "Enter" after each typed line.
Control the typing speed to mimic natural human typing.
Prerequisites
Before running the application, you need to install the required Python packages:

tkinter (usually comes pre-installed with Python)
pyautogui
You can install pyautogui via pip:

bash
Copy code
pip install pyautogui
How to Use
Clone or download the project:

bash
Copy code
git clone [https://github.com/your-repo/autotyper-app.git](https://github.com/itsrishav13/AutoTyper.git)
Navigate to the project directory:

bash
Copy code
cd autotyper-app
Run the Python script:

bash
Copy code
python autotyper.py
App Usage:

Paste Your Text: Enter the text you want to auto-type.
Number of Times: Specify how many times you want the text to be typed.
Press Enter after every line?: Check this box if you want the app to press "Enter" after typing each line.
Time to Wait: Enter the number of seconds to wait before the typing starts (default is 3 seconds).
Typing Speed: Set the typing speed in seconds per character (default is 0.2 seconds).
Press the Submit button to begin the auto-typing process.
Files in the Project:

autotyper.py: The main script for running the AutoTyper app.
logo.png: An icon for the app window (make sure this file is in the same directory as the script).
