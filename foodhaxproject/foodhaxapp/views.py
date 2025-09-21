from django.shortcuts import render

def basic_view(request):
    return render(request, 'foodhaxapp/basic.html')

def bread_view(request):
    return render(request, 'foodhaxapp/pantries/bread.html')

def jubileepantry_view(request):
    return render(request, 'foodhaxapp/pantries/jubileepantry.html')

def jubileekitch_view(request):
    return render(request, 'foodhaxapp/pantries/jubileekitch.html')