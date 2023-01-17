from django.shortcuts import render, HttpResponse

# Create your views here.
def helloword(request):
    return HttpResponse("<H1>Hello Word,This is my </H1"
                        "<H2>I Love Python and Django")
def firspage(request):
    return render(request, 'firstpage.html')
def secondpage(request):
    return render(request, 'secondpage.html')
def thirdpage(request):
    return render(request, 'thirdpage.html')
def hnyPage(request):
    return render(request, 'hnyPage.html')
def home(request):
    return render(request, 'home.html')
