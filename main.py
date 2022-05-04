from create_files import * 
#Импорт всех библиотек из второго файла

app = dash.Dash(__name__)
#Инициализация
app.layout = html.Div( 
    #создание того, что будет отображаться ан странице
    children = [
        #Создание первой таблицы
        dcc.Graph(
            figure=dict(
                #Здесь мы определяем точки графика
                data=[
                    {
                        #можно просто присвоить переменной массив данных, она сама соотнесет данные из другой переменной по индексу
                        'x' : data_usd['updated'],
                        'y': data_usd['price'],
                        #название нашей линии
                        'name' : 'Доллар'
                    },
                    {
                        'x' : data_eur['updated'],
                        'y' : data_eur['price'],
                        'name' : 'Евро'
                    }
                ],
                # Заголовов над графиком
                layout=dict(
                    title='Курс Евро и Доллара к рублю',
                )
            ),
            # Ниже можно ограничить график в высоте и ширине, так же добавляем его айди
            style={'height': 600},
            id='money-table'
        ), 
        dcc.Graph(
            figure=dict(
                data=[
                    {
                        'x' : data_peoples['Год'],
                        'y': data_peoples['Численность населения'],
                        'name' : 'Количество населения'
                    },
                ],
                layout=dict(
                    title='Количество населения',
                )
            ),
            style={'height': 600},
            id='people-table'
        ), 
        dcc.Graph(
            figure=dict(
                data=[
                    {
                        'x' : data_vvp['year'],
                        'y': data_vvp['usd'],
                        'name' : 'ВВП РОСИИИ'
                    },
                    {
                        'x' : data_vvp_usa['year'],
                        'y' : data_vvp_usa['usd'],
                        'name' : 'ВВП США'
                    }                    
                ],
                layout=dict(
                    title='ВВП РОСИИ И США в долларах США',
                )
            ),
            style={'height': 600},
            id='vvp-table'
        )        
])

#Инициализация начала нашей программы
if __name__ == '__main__':
    app.run_server(debug=True)