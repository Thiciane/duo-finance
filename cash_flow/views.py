from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import view
from cash_flow.models import CashFlow

@view(path='', name='')
def home(request: HttpRequest):
    cash_flows = CashFlow.objects.all()
    return render(request, "home.html.j2", {"cash_flows": cash_flows})

@view(path='post_cashflow', name='post_cashflow')
def post_cashflow(request: HttpRequest):
    created_at = request.POST.get("created_at")
    name = request.POST.get("name")
    value = request.POST.get("value")
    description = request.POST.get("description")
    type = request.POST.get("type")
    CashFlow.objects.create(created_at=created_at, name=name, value=value, description=description, type=type)
    
    response = HttpResponse()
    response["HX-Redirect"] = ""
    return response
    
@view(path='login', name='login')
def login(request: HttpRequest):
    return render(request, 'login.html.j2', {"clean": True } )