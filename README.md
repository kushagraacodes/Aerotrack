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

