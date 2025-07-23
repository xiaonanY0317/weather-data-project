import requests

def fetch_data(**kwargs):
    access_key = "d3591b4cfbf5d6d3f690875b47d40d49"
    City = "St. Louis"
    api_url = f"http://api.weatherstack.com/current?access_key={access_key}&query={City}"
    try:
        response =requests.get(api_url)
        response.raise_for_status()
        print("Wearther data fetched successfully!")  
        raw_data = response.json()
        kwargs['ti'].xcom_push(key='raw_data', value=raw_data)
        print("Raw data pushed to XCom.")
        print(raw_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# def mock_fetch_data(**kwargs):
#     raw_data = {'request': {'type': 'City', 'query': 'Saint Louis, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Saint Louis', 'country': 'United States of America', 'region': 'Missouri', 'lat': '38.627', 'lon': '-90.198', 'timezone_id': 'America/Chicago', 'localtime': '2025-07-15 23:19', 'localtime_epoch': 1752621540, 'utc_offset': '-5.0'}, 'current': {'observation_time': '04:19 AM', 'temperature': 25, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '05:49 AM', 'sunset': '08:24 PM', 'moonrise': '11:20 PM', 'moonset': '10:49 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 82}, 'air_quality': {'co': '382.95', 'no2': '24.975', 'o3': '21', 'so2': '4.81', 'pm2_5': '12.765', 'pm10': '12.765', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 9, 'wind_degree': 219, 'wind_dir': 'SW', 'pressure': 1013, 'precip': 0, 'humidity': 88, 'cloudcover': 0, 'feelslike': 28, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}
#     kwargs['ti'].xcom_push(key='raw_data', value=raw_data)
#     print("Raw data pushed to XCom.")