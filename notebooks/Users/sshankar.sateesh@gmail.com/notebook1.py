# Databricks notebook source
import urllib, json
import requests
import pandas as pd
url = "https://api.stlouisfed.org/fred/sources?api_key=ee8afb7752f0cf5dea9bb634737b7c50&file_type=json"
r = requests.get(url)
print(r.json())
data1 = pd.json_normalize(r.json())
print(data1['sources'][0])
data2 = pd.json_normalize(data1['sources'][0])
print(data2)
