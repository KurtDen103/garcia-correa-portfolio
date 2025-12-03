from django.shortcuts import render

# Create your views here.
def home(request):
    # Ipagpalagay na ito ang portfolio template mo
    return render(request, 'index.html', {})