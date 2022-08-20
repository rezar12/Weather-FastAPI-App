# Weather-FastAPI-App

## Description

This is a weather app that uses the OpenWeatherMap API.
I conbined the weather app with the FastAPI framework to create a fast and lightweight weather app.

### Presentation
![Home screen ](Readme/page1.jpg "Home screen")

This is the home screen of the app .This page contains a drop-down menu of cities in my country.

![Home screen Ville ](Readme/selectville.jpg "Home screen Ville")

Always on the home screen you select a city to display the temperature of it.

![view temperature ](Readme/viewvilletemp.jpg "temperature view")

This is the temperature view of the app. Click on toggle button to see the ligth mode and the dark mode.

![app mode ](Readme/changemode.jpg "temperature view")


## Installation

Install FastAPI and OpenWeatherMap API
- install python and pip

```bash
sudo apt-get update
sudo apt-get install python3.8 python3-pip
```	
- clone repository

```bash
git clone https://github.com/rezar12/Weather-FastAPI-App.git
```	
- install dependencies

```bash
pip install -r requirements.txt
```
- run the app

```bash
uvicorn main:app --reload
```

