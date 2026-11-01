
import streamlit as st
import requests
from gtts import gTTS
from io import BytesIO
from datetime import datetime, timezone

st.set_page_config(
    page_title="Weather Announcement System",
    page_icon="🌦️"
)

st.title("🌦️ Weather Announcement System")
st.write("Enter a city name to get the weather report.")

# OpenWeatherMap API key
api_key = st.secrets["OPENWEATHER_API_KEY"]


def GetWeather(city):
    weather_url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(weather_url, timeout=15)
    data = response.json()

    if response.status_code != 200:
        return None

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    country = data["sys"]["country"]

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"], timezone.utc
    ).strftime("%H:%M UTC")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"], timezone.utc
    ).strftime("%H:%M UTC")

    report = (
        f"Weather report for {city}, {country}. "
        f"Description: {description}. "
        f"Temperature: {temperature} degrees Celsius. "
        f"Humidity: {humidity} percent. "
        f"Wind speed: {wind_speed} meters per second. "
        f"Sunrise: {sunrise}. Sunset: {sunset}."
    )

    return {
        "description": description,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "country": country,
        "sunrise": sunrise,
        "sunset": sunset,
        "report": report
    }


city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if city.strip():
        try:
            weather = GetWeather(city.strip())

            if weather is None:
                st.error("Weather information not available for this city.")
            else:
                st.subheader(f"Weather Report: {city}")

                st.write("Description:", weather["description"])
                st.metric(
                    "Temperature",
                    f'{weather["temperature"]} °C'
                )
                st.write("Humidity:", weather["humidity"], "%")
                st.write("Wind Speed:", weather["wind_speed"], "m/s")
                st.write("Country:", weather["country"])
                st.write("Sunrise:", weather["sunrise"])
                st.write("Sunset:", weather["sunset"])

                st.subheader("Weather Announcement")
                st.write(weather["report"])

                # Convert weather report to speech
                audio_file = BytesIO()
                tts = gTTS(text=weather["report"], lang="en")
                tts.write_to_fp(audio_file)
                audio_file.seek(0)

                st.audio(audio_file, format="audio/mp3")

        except requests.exceptions.RequestException:
            st.error("Unable to connect to the weather service.")

    else:
        st.warning("Please enter a city name.")
