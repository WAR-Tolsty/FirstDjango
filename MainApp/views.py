from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов", 
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Стукалов М.Н.</i>" \
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author["телефон"]}</b><br>
    email: <b>{author["email"]}</b><br>

    """
    return HttpResponse(text)

def getitem(request, item_id):
    """ По указаному id возвращаем имя элемента"""
    for item in items:
        if item['id'] == item_id:
            result = f"""
            <h2> Имя: {item["name"]}<h2>
            <p> Количество {item['quantity']}</p>
            <p> <a href="/items"> Назад к списку товаров </a>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f"Item with id={item_id} not found")

def getitems(request):
    result = "<h1> Список товаров <h1><ol>"
    for item in items:
        result += f""" <li><a href="/item/{item['id']}"> {item['name']} </li> """
    result += "</ol>"
    return HttpResponse(result)