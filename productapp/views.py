
from django.shortcuts import render, HttpResponse

def testbt (request):
    return render(request, 'productapp/testbt.html')