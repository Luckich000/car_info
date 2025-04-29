import requests

def getcar(id):
    url = f'http://localhost:8080/car/{id}'
    response = requests.get(url)
    data = response.json()
    print(data)

def loadcar(model,year,color,number,type):
    url = 'http://localhost:8080/car/create'
    data = {
        "model": model,
        "car_year": year,
        "color": color,
        "car_number": number,
        "car_type" : type
    }
    response = requests.post(url, json=data)
    result = response.json()
    print(result)

def deletecar(id):
    url = f'http://localhost:8080/car/delete/{id}'
    response = requests.delete(url)
    data = response.json()
    print(data)

def addaccident(accident_date,description,id):
    url = f'http://localhost:8080/accident/add/{id}'
    data = {
        "accident_date": accident_date, #yyyy-mm-dd
        "description": description
    }
    response = requests.post(url, json=data)
    result = response.json()
    print(result)


#проверка

loadcar("porshe",2000,"black","c812oc","coupe")
addaccident("2017-01-01","ехал я как-то ночью по трассе со скорость 200 км в час, к сожалению, была зима и холодно, я не справился с управлением и намотался на ясень",input(int()))
getcar(input(int()))
deletecar(input(int()))

