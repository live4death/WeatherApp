#!/usr/bin/env python3

import webview
import weatherNotification

class Api:
    def get_weather(self, city, day, time):
        return weatherNotification.get_weather()

webview.create_window(
    "Weather App",
    "index.html",
    width=900,
    height=720,
    resizable=False
)

webview.start()