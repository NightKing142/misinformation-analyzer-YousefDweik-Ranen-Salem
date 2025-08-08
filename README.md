Misinformation Analyzer (TruthLens)
This project is a web-based tool designed to analyze text for potential misinformation, cognitive biases, and logical fallacies. Users can paste a social media post, news headline, or any block of text, and the application will provide an AI-powered analysis, highlighting a "misleading score" and detailing the specific rhetorical tactics used.

The application is built with a separate frontend and backend, which communicate via a REST API.

Getting Started: How to Run This Project
Follow these steps to download the project from GitHub and get it running on your local machine.

Prerequisites
Before you begin, ensure you have the following software installed:

Python (version 3.8 or newer)

Node.js (which includes npm)

Git

PyCharm

WebStorm

Step 1: Download the Project
Open a terminal (like Git Bash or Command Prompt) and run the following command to clone the repository from GitHub. This will create a new folder on your computer containing all the project files.

git clone https://github.com/NightKing142/misinformation-analyzer-YousefDweik-Ranen-Salem.git

After the download is complete, navigate into the newly created project folder:

cd misinformation-analyzer-YousefDweik-Ranen-Salem

Setup and Installation
Once you have downloaded the files, proceed with the setup instructions for both the backend and frontend.

Part 1: Backend Setup (PyCharm)
The backend is responsible for handling API requests and communicating with the Google Gemini API.

Open the Project in PyCharm:

Open PyCharm and select File > Open.

Navigate to and select the main misinformation-analyzer-YousefDweik-Ranen-Salem folder you just downloaded.

Configure the Python Interpreter:

PyCharm needs to know which Python executable to use. Go to File > Settings > Project: [Your Project Name] > Python Interpreter.

Click the gear icon ⚙️ and select Add....

In the new window, select Virtualenv Environment on the left, then choose the Existing option.

Click the ... button and find the python.exe file inside your project's backend/venv/Scripts folder.

Click OK to confirm.

Install Dependencies:

At the bottom of the PyCharm window, click on the Terminal tab.

Navigate into the backend directory:

cd backend

Install the required Python libraries by running these commands one by one, pressing Enter after each:

pip install Flask
pip install flask-cors
pip install google-generativeai
pip install python-dotenv



Run the Backend Server:

In the PyCharm terminal (while still inside the backend folder), run the command:

python backend.py

The backend server will now be running at http://127.0.0.1:5000.

Part 2: Frontend Setup (WebStorm)
The frontend provides the user interface in your browser.

Open the Project in WebStorm:

Open WebStorm and select File > Open.

Navigate to and select the main misinformation-analyzer-YousefDweik-Ranen-Salem folder.

Open the WebStorm Terminal:

At the bottom of the WebStorm window, click on the Terminal tab.

Install Dependencies:

The package.json file is located in a subfolder. Navigate to the correct directory by running:

cd frontend/finalproject

Now, install all the required Node.js packages:

npm install

(It is normal to see warnings about vulnerabilities after installation. You can safely ignore these for this project.)

Run the Frontend Server:

In the same terminal (while inside the frontend/finalproject folder), run the start command:

npm start

A new browser tab should automatically open with the application running at http://localhost:3000.

How to Use
Ensure both the backend (in PyCharm) and frontend (in WebStorm) servers are running.

Open your browser to http://localhost:3000.

Paste any text you want to analyze into the text area.

Click the "Analyze Text" button.

The results, including a score, summary, and a detailed breakdown of fallacies and biases, will appear below.
