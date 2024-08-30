from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
     context = {"name": "aliya", "age": 27, "name2": "shaista", "age": 17, }

     return render(request,  'base.html', context)
     # return HttpResponse("hello home page")
def About(request):
     return HttpResponse("hello about page")
def Contact(request,data):
     return HttpResponse(data)
def Page(request):
     return render (request, "base.html")
def Page1(request):
     return render(request, "index.html")

