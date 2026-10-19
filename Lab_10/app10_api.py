
import streamlit as st
import requests

st.title("Weather API Demo")

API_KEY = st.secrets.get("API_KEY", "")
city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):
    if not API_KEY:
        st.error("Please add your API key in secrets.toml")
    else:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            with st.spinner("Fetching weather..."):
                response = requests.get(
                    url, params=params, timeout=10
                )
                response.raise_for_status()
                resp = response.json()

            st.json(resp)

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Temperature",
                f"{resp['main']['temp']} °C"
            )
            c2.metric(
                "Condition",
                resp["weather"][0]["description"].title()
            )
            c3.metric(
                "Humidity",
                f"{resp['main']['humidity']}%"
            )

        except requests.exceptions.Timeout:
            st.error("Request timed out. Try again.")

        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                st.error("Invalid or inactive API key. Check your key.")
            elif response.status_code == 404:
                st.error("City not found. Check the city name.")
            else:
                st.error(f"HTTP error: {e}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

st.markdown("---")
st.subheader("HTTP Methods")

st.markdown("""
- **GET** - Retrieve data
- **POST** - Send data
- **PUT** - Update data
- **DELETE** - Delete data
""")
