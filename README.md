# 3rd Eye Real-time Event Detection for Video Surveillance Application

3rd Eye is a real-time event detection video surveillance application that monitors video feeds, detects fires, and alerts users instantly. Built as a web application using Electron, it can be converted into a desktop application for enhanced accessibility and usability.
# Features
+ Real-Time Monitoring: Continuously monitors video feeds for any signs of fire.
+ Instant Alerts: Sends immediate notifications to users upon detecting a fire using Pushbullet.
+ Desktop Application: Built with Electron, allowing it to run as a standalone desktop application.
+ User-Friendly Interface: Easy-to-use interface for setting up and monitoring video feeds.

# Technologies Used
+ Electron: For creating the desktop application.
+ Web Technologies: HTML, CSS, JavaScript for the frontend.
+ Backend: Node.js, Express.js for handling server-side operations.
+ Machine Learning: Fire detection algorithms for analyzing video feeds.
+ Pushbullet: For sending instant alerts to users.

# Installation
## Prerequisites
Ensure you have the following installed:

+ Node.js (includes npm)
+ Git
+ Python (for setting up the Python environment)
+ Create React App (for setting up the React app)

# Steps
## 1.Clone the Repository:
+ ```git clone https://github.com/your-username/3rd-Eye-realtime-event-detection-for-video-surveillance-application.git```
+ ```cd 3rd-Eye-realtime-event-detection-for-video-surveillance-application```

## 2.Install Dependencies:
+ ```npm install```

## 3.Create Python Virtual Environment:
+ ```python -m venv env```

## 4.Activate the Virtual Environment:
### Windows:
+ ```.\env\Scripts\activate```
### Linux/Mac:
+ ```Linux/Mac:```

## 5.Install Python Dependencies:
+ ```pip install -r requirements.txt```

## 6.Set Up React App:
+ ```npx create-react-app client```
+ ```cd client```

## 7.Configure Pushbullet:
+ Obtain your Pushbullet API key from your **Pushbullet account settings**.
+ Create a .env file in the root directory of the project and add your API key:
+ ```PUSHBULLET_API_KEY=your_pushbullet_api_key```

## 8.Run the Application:
Return to the project root directory:
+ ```cd ..```
Double-click the start.bat file to launch the application.

# Usage
## 1.Launch the Application:

Start the application by running the start.bat file. This will open the application window.

## 2.Set Up Video Feeds:

Add the video feeds you want to monitor by following the on-screen instructions.

## 3.Monitor and Get Alerts:

Once the video feeds are set up, the application will start monitoring in real-time. In case of fire detection, you will receive instant alerts via Pushbullet.

# Contributing
We welcome contributions to enhance 3rd Eye. Here’s how you can help:

**1.Fork the repository.<br>
2.Create a new branch (```git checkout -b feature-branch```).<br>
3.Make your changes.<br>
4.Commit your changes (```git commit -m 'Add some feature```).<br>
5.Push to the branch (```git push origin feature-branch```).<br>
6.Open a pull request.<br>**
