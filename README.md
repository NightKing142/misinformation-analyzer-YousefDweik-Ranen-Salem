Misinformation Analyzer
This project is a web-based tool designed to analyze text for potential misinformation, cognitive biases, and logical fallacies. Users can paste a social media post, news headline, or any block of text, and the application will provide an AI-powered analysis, highlighting a "misleading score" and detailing the specific rhetorical tactics used.

The application is built with a separate frontend and backend, which communicate via a REST API.

Tech Stack
Frontend:

React.js

HTML5 & CSS3

Backend:

Flask (Python)

Google Gemini API for AI-powered text analysis

Version Control:

Git + GitHub

Setup and Installation
To get this project running locally, you will need to set up and run both the backend and frontend servers separately using PyCharm and WebStorm.

1. Backend Setup (PyCharm)
The backend is responsible for handling API requests and communicating with the Google Gemini API.

Open the Project in PyCharm:

Open PyCharm and select File > Open.

Navigate to and select the main misinformation-analyzer folder to open the entire project. PyCharm will recognize the backend subfolder.

Open the PyCharm Terminal:

At the bottom of the PyCharm window, click on the Terminal tab. This opens a command line that is already configured for your project, often with a virtual environment automatically set up.

Install Dependencies:

In the PyCharm terminal, install all the required Python libraries by running these commands one by one.

pip install Flask
pip install flask-cors
pip install google-generativeai
pip install python-dotenv


Alternatively, type the following command into the PyCharm terminal:

python backend/backend.py

The backend server will now be running on http://127.0.0.1:5000.

2. Frontend Setup (WebStorm)
The frontend provides the user interface in your browser.

Open the Project in WebStorm:

Open WebStorm and select File > Open.

Navigate to and select the main misinformation-analyzer folder. WebStorm will recognize the frontend subfolder.

Open the WebStorm Terminal:

At the bottom of the WebStorm window, click on the Terminal tab.

Install Dependencies:

The terminal should already be in your main project directory. First, navigate into the frontend folder:

cd frontend

Now, install all the required Node.js packages:

npm install

Run the Frontend Server:

In the same terminal, run the start command:

npm start

A new browser tab should automatically open with the application running at http://localhost:3000.

How to Use
Ensure both the backend (in PyCharm) and frontend (in WebStorm) servers are running.

Open your browser to http://localhost:3000.

Paste any text you want to analyze into the text area.

Click the "Analyze Text" button.

The results, including a score, summary, and a detailed breakdown of fallacies and biases, will appear below.
