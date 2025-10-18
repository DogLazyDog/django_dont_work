from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Привет!</h1><p>Добро пожаловать на главную страницу.</p>") 