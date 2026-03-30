AeroTrack -- Real-Time Air Quality Monitoring

## Overview

AeroTrack is a Python-based tool that retrieves real-time Air Quality
Index (AQI) and pollutant data using the OpenWeatherMap API. It converts
a place name into geographic coordinates and displays a detailed
environmental report.

## Features

-   Real-time AQI fetching
-   Detailed pollutant concentration report (CO, NOâ‚‚, Oâ‚ƒ, SOâ‚‚, PM2.5,
    PM10, NHâ‚ƒ)
-   Human-friendly AQI interpretation
-   Error handling for invalid inputs and API failures
-   Clean and structured console output

## Technologies Used

-   *Python 3*
-   *requests* library
-   *OpenWeatherMap Geocoding API*
-   *OpenWeatherMap Air Pollution API*

## Installation & Setup

1.  Install Python 3.x\

2.  Install required dependencies:

        pip install requests

3.  Insert your OpenWeatherMap API key inside the script:

     python
    API_KEY = "your_api_key_here"
    

4.  Run the program:

        python 01.py

  ##  Usage:

Run the script and enter any place name when prompted:

    Enter place name: Mumbai

The program will display the AQI and pollutant levels.

## Testing Instructions:

Test with: - Valid places (e.g., Delhi, London) - Small towns (e.g.,
Lonavala) - Invalid entries (e.g., asdasdasd) - Names with spaces or
hyphens (e.g., New York, Rio-de-Janeiro)

## Screenshots 
## Program
<img width="250" height="250" alt="Screenshot 2026-03-30 at 3 36 23 PM" src="https://github.com/user-attachments/assets/105fb12a-97d1-42b9-b657-e964cc1a69de" />
<img width="250" height="250" alt="Screenshot 2026-03-30 at 3 37 26 PM" src="https://github.com/user-attachments/assets/0febd0c8-0ee7-4a23-82fd-26044b82297d" />
<img width="250" height="218" alt="Screenshot 2026-03-30 at 3 37 48 PM" src="https://github.com/user-attachments/assets/0e9e61bd-8f67-49c4-b623-5af6c48f5203" />
## Outputs
<img width="250" height="293" alt="Screenshot 2026-03-30 at 3 38 42 PM" src="https://github.com/user-attachments/assets/9c32427e-d0c5-4f3e-859b-e3670faea50a" />
<img width="250" height="295" alt="Screenshot 2026-03-30 at 3 39 28 PM" src="https://github.com/user-attachments/assets/857085dd-d667-467e-b338-20ac57445d73" />



