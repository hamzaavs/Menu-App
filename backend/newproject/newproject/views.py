from django.http import HttpResponse

def error_404_view(request, exception):
    return HttpResponse("<h1>404 Sayfa Bulunamadı :.(</h1>")