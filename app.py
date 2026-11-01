!pip install requests SpeechRecognition gTTS pydub -q
import requests
import speech_recognition as sr
from gtts import gTTS
from IPython.display import Audio, display, Javascript
from google.colab import output
from pydub import AudioSegment
import base64
import io

def speak(text):
    tts = gTTS(text=text, lang="en")

    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    display(Audio(audio_file.read(), autoplay=True))
  from gtts import gTTS
from IPython.display import Audio, display

def speak(text):

    tts = gTTS(text=text, lang="en")

    tts.save("speech.mp3")

    display(Audio("speech.mp3", autoplay=True))

text = input("Enter text: ")

speak(text)
import requests
from gtts import gTTS
from IPython.display import Audio, display

api_key = input("Enter Your_API_KEY")

def GetWeather(city):
    
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(weather_url).json()
    print(response)

    if response.get("cod") != 200:
        return "Weather information not available for " + city

    description = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    wind_speed = response["wind"]["speed"]
    Sunrise = response["sys"]["sunrise"]
    Sunset = response["sys"]["sunset"]
    weather_text = (
        f"\n\nWeather report for {city}.\n"
        f"Description: {description}.\n"
        f"Temperature: {temperature} degrees Celsius.\n"
        f"Humidity: {humidity} percent.\n"
        f"Wind speed: {wind_speed} meters per second.\n"
        f"System: {response['sys']['country']}.\n"
        f"Sunrise: {Sunrise}.\n"
        f"Sunset: {Sunset}."
    )

    return weather_text
  
city_input = input("Enter City Name: ")

report = GetWeather(city_input)

print(report)

tts = gTTS(text=report, lang="en")

tts.save("weather_report.mp3")

display(Audio("weather_report.mp3"))
