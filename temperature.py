import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather_data(city, api_key, units='metric'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as errh:
        messagebox.showerror("HTTP Error", f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        messagebox.showerror("Connection Error", f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        messagebox.showerror("Timeout Error", f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Request Error", f"Error: {err}")
    return None

# Function to display weather information
def display_weather_info():
    city = city_entry.get().strip()  # Clean up the input
    if not city:
        messagebox.showerror("Input Error", "Please enter a valid city name")
        return

    units = 'metric' if temp_unit.get() == 'Celsius' else 'imperial'
    api_key = "9cfeb474614e6054f523937fc95332c4"
    
    weather_data = get_weather_data(city, api_key, units)

    if weather_data:
        city_name = weather_data.get("name")
        country = weather_data.get("sys", {}).get("country")
        temperature = weather_data.get("main", {}).get("temp")
        humidity = weather_data.get("main", {}).get("humidity")
        weather_desc = weather_data.get("weather", [])[0].get("description").capitalize()
        wind_speed = weather_data.get("wind", {}).get("speed")

        weather_info = f"""
        Weather in {city_name}, {country}:
        Temperature: {temperature}°{temp_unit.get()[0]}
        Humidity: {humidity}%
        Wind Speed: {wind_speed} m/s
        Condition: {weather_desc}
        """
        result_label.config(text=weather_info)
    else:
        result_label.config(text="Unable to fetch weather data. Please try again.")

# Creating the GUI window
root = tk.Tk()
root.title("Advanced Weather App")

# City input field
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Temperature unit selection
temp_unit = tk.StringVar(value="Celsius")
celsius_radio = tk.Radiobutton(root, text="Celsius", variable=temp_unit, value="Celsius")
fahrenheit_radio = tk.Radiobutton(root, text="Fahrenheit", variable=temp_unit, value="Fahrenheit")
celsius_radio.pack(pady=5)
fahrenheit_radio.pack(pady=5)

# Button to get weather information
get_weather_button = tk.Button(root, text="Get Weather", command=display_weather_info)
get_weather_button.pack(pady=10)

# Label to display weather results
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=20)

# Run the application
root.mainloop()
