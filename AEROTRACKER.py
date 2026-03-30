# AeroTrack - Real-Time Air Quality Monitoring
import requests

# ────────────────────────────────────────────────────────────────
# CONFIGURATION
# ────────────────────────────────────────────────────────────────

API_KEY = "4e90d1f8233547db8db139beeb50e10f"  # Your API key
GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
AIR_QUALITY_URL = "https://api.openweathermap.org/data/2.5/air_pollution"

# ────────────────────────────────────────────────────────────────
# GEOCODING FUNCTION
# ────────────────────────────────────────────────────────────────

def get_coordinates(place_name):
    """Fetches latitude and longitude for a given place name."""
    params = {"q": place_name, "limit": 1, "appid": API_KEY}
    response = requests.get(GEOCODING_URL, params=params)

    if response.status_code == 200 and response.json():
        data = response.json()[0]
        return data["lat"], data["lon"]
    else:
        print("❌ Error: Invalid place name or API issue.")
        return None, None

# ────────────────────────────────────────────────────────────────
# AQI INTERPRETATION FUNCTION
# ────────────────────────────────────────────────────────────────

def interpret_aqi(aqi):
    """Returns a descriptive interpretation of AQI."""
    descriptions = {
        1: "Good – The air quality is satisfactory, and pollution poses little or no risk.",
        2: "Fair – Air quality is acceptable; however, some pollutants may be a concern for sensitive individuals.",
        3: "Moderate – Air quality is unhealthy for sensitive groups, such as children, the elderly, and those with respiratory conditions.",
        4: "Poor – Health effects may be experienced by the general public, with more serious concerns for sensitive groups.",
        5: "Very Poor – Air pollution levels are hazardous, and everyone is at risk of severe health effects."
    }
    return descriptions.get(aqi, "Unknown – Unable to determine air quality at the moment.")

# ────────────────────────────────────────────────────────────────
# AIR QUALITY FETCH FUNCTION
# ────────────────────────────────────────────────────────────────

def fetch_air_quality(place_name):
    """Fetches air quality data and prints a report."""
    lat, lon = get_coordinates(place_name)

    if lat is None or lon is None:
        return

    params = {"lat": lat, "lon": lon, "appid": API_KEY}
    response = requests.get(AIR_QUALITY_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        air_quality_index = data["list"][0]["main"]["aqi"]
        components = data["list"][0]["components"]
        aqi_description = interpret_aqi(air_quality_index)

        print("\n════════════════════════════════════════════════════")
        print("                 AIR QUALITY REPORT")
        print("════════════════════════════════════════════════════")
        print(f"📍 Location: {place_name} (Lat: {lat}, Lon: {lon})")
        print("----------------------------------------------------")
        print(f"📊 Air Quality Index (AQI): {air_quality_index}")
        print("----------------------------------------------------")
        print("🔬 Pollutant Concentrations (in µg/m³):")
        print(f"   • Carbon Monoxide (CO): {components['co']}")
        print(f"   • Nitrogen Dioxide (NO2): {components['no2']}")
        print(f"   • Ozone (O3): {components['o3']}")
        print(f"   • Sulfur Dioxide (SO2): {components['so2']}")
        print(f"   • Particulate Matter (PM2.5): {components['pm2_5']}")
        print(f"   • Particulate Matter (PM10): {components['pm10']}")
        print(f"   • Ammonia (NH3): {components['nh3']}")
        print("----------------------------------------------------")
        print(f"📝 Assessment: Since the AQI is {air_quality_index}, the air quality can be classified as **{aqi_description}**.")
        print("════════════════════════════════════════════════════")
    else:
        print(f"❌ Error fetching air quality data: {response.status_code}")

# ────────────────────────────────────────────────────────────────
# MAIN PROGRAM
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    place_name = input("Enter place name: ")
    fetch_air_quality(place_name)
