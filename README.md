## Live Demo

[Click here to view the Weather Announcement System](https://wheatherannouncementsystem-xarzbpsappah2k7xhanrjt6.streamlit.app/)


# Weather Announcement System 🌦️

## Project Overview

The Weather Announcement System is a Python-based web application that provides real-time weather information for any city.

Users can enter a city name to get weather details and listen to a voice announcement of the weather report.

## Features

- Search weather information by city name.
- Display temperature in Celsius.
- Display humidity and wind speed.
- Show sunrise and sunset times.
- Convert weather reports into speech.
- Simple and user-friendly interface.

## Technologies Used

- Python
- Streamlit
- OpenWeatherMap API
- gTTS (Google Text-to-Speech)
- Requests

## Requirements

- Python 3.9 or above
- OpenWeatherMap API key
- Internet connection
- Required Python libraries

### Python Libraries

Install the following libraries:

```bash
pip install streamlit requests gTTS
```

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/hemanthC6/Wheather_Announcement_System.git
```

### Step 2: Open the Project Folder

```bash
cd Wheather_Announcement_System
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API Key

Create a folder named `.streamlit` in the project directory.

Inside that folder, create a file named `secrets.toml`.

Add your OpenWeatherMap API key:

```toml
OPENWEATHER_API_KEY = "your_api_key"
```

Replace `your_api_key` with your actual API key.

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Expected Output

### 1. Home Page

The application displays the title:

**Weather Announcement System**

It provides a text input field to enter a city name and a button to get the weather report.

### 2. Weather Report

After entering a city name and clicking the Get Weather button, the application displays:

- City name and country
- Weather description
- Temperature in Celsius
- Humidity percentage
- Wind speed
- Sunrise time
- Sunset time

### 3. Voice Announcement

The application converts the weather report into speech and plays the audio announcement.

## Deployment

This application can be deployed using Streamlit Community Cloud.

Users can access the application through the public deployment URL.

## Author

Hemanth

## License

This project is created for educational purposes.
