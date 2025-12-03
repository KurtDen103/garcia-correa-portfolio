# main_app/views.py

from django.shortcuts import render
# from django.http import HttpResponse # Hindi ito kailangan kung gagamit ka ng render

def home(request):
    # Tiyakin na ang 'index.html' ay nasa templates/main_app/index.html folder mo
   
    # Kung may data ka na ipapasa sa template
    return render(request, 'index.html', {})
    
# Kung nagdagdag ka ng 'about' sa urls.py:
# def about(request):
#     return render(request, 'about.html', {})