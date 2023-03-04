from django.shortcuts import render

def index(request): #{METODO REQUEST DE HTTP}
    
    return render(request,'index.html') #{DEVUELVE EL HTML (REQUEST)}
