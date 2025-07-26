import tkinter as tk
import requests
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
API_KEY = bd4a68047094ed3bfa302ff6d58ea82f
def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="City not found!", fg="red")
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        country = data["sys"]["country"]
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        output = (
            f"📍 {city}, {country}\n"
            f"🕒 {time}\n"
            f"🌡 Temperature: {temp}°C\n"
            f"💧 Humidity: {humidity}%\n"
            f"🌬 Wind Speed: {wind} m/s\n"
            f"⛅ Description: {desc}"
        )

        result_label.config(text=output, fg="black")
    except Exception as e:
        result_label.config(text="Error fetching data!", fg="red")

def search_weather():
    city = city_entry.get().strip()
    if city:
        get_weather(city)

# GUI Setup
root = tk.Tk()
root.title("Real-Time Weather Dashboard")
root.geometry("400x400")
root.config(bg="#e1f5fe")

tk.Label(root, text="Enter City Name:", bg="#e1f5fe", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=search_weather, bg="#03a9f4", fg="white", font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), bg="#e1f5fe", justify="left")
result_label.pack(pady=20)

root.mainloop()
