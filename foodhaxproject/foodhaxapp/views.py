from django.shortcuts import render

def basic_view(request):
    return render(request, 'foodhaxapp/basic.html')
