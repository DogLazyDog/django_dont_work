from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Привет!</h1><p>Добро пожаловать на главную страницу.</p>") 

def employee_info(request):
    return HttpResponse("<p>Здесь будет полезная информация для сотрудников.</p>") 

def employee_id(request, employee_id):
    response = f"<p>ID сотрудника: {employee_id}</p>"

    return HttpResponse(response)

