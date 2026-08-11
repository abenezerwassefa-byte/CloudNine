# ☁️ CloudNine

CloudNine is a simple weather web application built with **Python, Flask, Jinja2, HTML, and CSS**.

The application allows a user to enter a city and retrieve its current temperature. Behind the scenes, CloudNine communicates with two external APIs: one to determine the geographic coordinates of the requested location, and another to retrieve the current weather data for those coordinates.

This project was built as a hands-on introduction to backend web development with Flask, HTTP requests, JSON data, API integration, error handling, and server-side rendering with Jinja2.

---

## 📸 Overview

CloudNine provides a simple interface where users can:

- Enter the name of a location
- Submit the location to the Flask backend
- Retrieve its geographic coordinates
- Request the current temperature for those coordinates
- Display the result dynamically on the webpage
- Receive an error message when a location cannot be found
- Receive a fallback error message when the weather API request fails

The interface uses a **matte-black theme with subtle white neon accents**, keeping the design simple while giving the application a more polished appearance.

---

## 🛠️ Technologies Used

### Backend

- **Python**
- **Flask**
- **Requests**

### Frontend

- **HTML**
- **CSS**
- **Jinja2**

### APIs

- **Open-Meteo Geocoding API**
- **Open-Meteo Weather Forecast API**

---

## 🔄 How CloudNine Works

### When a user enters a city, several things happen between the browser and the final result.</br>
 #### 1. First the user enters a location, and fetches the data with the api in use.</br>
 #### 2. If the user doesn't enter anything, but submits, the page responds with proper error handling. This creates better user experience.</br>
---
### Note on the Frontend

The CSS styling for this project was developed with the assistance of AI as part of the development process. The primary focus of CloudNine was to build a foundational understanding of **Flask, APIs, HTTP requests, routing, error handling, and backend architecture** for the author, while also experimenting with frontend presentation and UI design.

The styling was refined and integrated into the project by the author.

