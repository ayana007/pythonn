from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
def home(request):
    obj=Place.objects.all()
    team=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':team})

















# def home(request):
#     return HttpResponse("Welcome Home")
# def about(request):
#     return render(request, "about.html")
#
# def contact(request):
#     return HttpResponse("Ready to contact")
# def detail(request):
#     return render (request,"detail.html")
# def Thanks(request):
#     return HttpResponse("hello thankyou")
# def home(request):
#     name = "india"
#     return render(request, "detail.html", {'obj': name})
#
#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     addition = x + y
#     subtraction = x - y
#     division = x / y
#     multiplication = x * y
#     return render(request, "result.html",
#                   {'result1': addition, 'result2': subtraction, 'result3': division, 'result4': multiplication})
