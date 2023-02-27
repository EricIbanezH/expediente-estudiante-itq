from django.shortcuts import render

def index(request): #{METODO REQUEST DE HTTP}
    
    return render(request,'base/index.html') #{DEVUELVE EL HTML (REQUEST)}
