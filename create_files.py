#Импорт всех необходимых модулей
import pandas as pd
import dash
import csv
from dash.dependencies import Input, Output   
from dash import dcc
from dash import html

#АДреса csv с курсами валют
url_eur = 'https://bhom.ru/on-line/currency/eur_quotes.csv'
url_usd = 'https://bhom.ru/on-line/currency/usd_quotes.csv'

# Открываем csv по адресу что бы начать с ними работать
data_usd = pd.read_csv(url_usd, delimiter = ";")
data_eur = pd.read_csv(url_eur, delimiter = ";")    

#Открываем уже готовые csv файлы для работы с ними
data_vvp = pd.read_csv('data/vvp.txt', delimiter = '/')
data_vvp_usa = pd.read_csv('data/vvp_usa.txt', delimiter = '–')
data_peoples = pd.read_csv('data/naselenie.csv', delimiter = '\t')