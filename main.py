from typing import Optional

from fastapi import FastAPI, Request

from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

from babel.dates import format_date, Locale

import datetime

from starlette.requests import Request

import requests



app = FastAPI()

template = Jinja2Templates(directory='template')

app.mount("/static", StaticFiles(directory="static"), name="static")
dictionary = {}

def apiWeather(location : str,language : str):
    
    URL="{BASE_URL}q={CITY}&appid={API_KEY}&units={Unit}&lang={lang}".format(BASE_URL = "https://api.openweathermap.org/data/2.5/weather?",CITY =location,API_KEY = "8073cf31515f3dcc7c38940bfc96a36f",Unit = "metric",lang=language)
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']


    dictionary = {"Temperature": temperature, "Humidity": humidity,
                    "Pressure": pressure, "Weather Report": {report[0]['description']},
                    "weather icon":{report[0]["icon"]}}

    return dictionary


@app.get("/")
# async  devant def ...
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request": request, })


@app.post("/obt")
async def add_todo(request: Request):
    locale = Locale('fr')

    Date = datetime.datetime.now().date()

    ladate = format_date(Date, format="MMMM dd, yyyy", locale=locale)

    formdata = await request.form()
    ville =formdata['ville']

    dictionary = apiWeather(ville.lower(),locale)
    print(dictionary)
    rapport =list(dictionary["Weather Report"])
    icon = list(dictionary["weather icon"])
    icon_URL = "http://openweathermap.org/img/wn/{icon}@2x.png".format(icon=icon[0])
    
    
    return template.TemplateResponse("ville.html", {"request": request, "date": ladate,

                                                    "temperature": dictionary["Temperature"], "Humidite": dictionary["Humidity"], "Pression": dictionary["Pressure"],

                                                    "Weather_Report": rapport[0], "ville": formdata['ville'],"urlicon":icon_URL})

