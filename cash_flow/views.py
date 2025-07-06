from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from . import view
from cash_flow.models import CashFlow

@view(path='', name='')
def home(request: HttpRequest):
    cash_flows = CashFlow.objects.all()
    return render(request, "contents/home.html.j2", {"cash_flows": cash_flows})

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
    return render(request, 'contents/login.html.j2', {"clean": True } )

@view(path='dashboard', name='dashboard')
def dashboard(request: HttpRequest):
    return render(request, 'contents/dashboard.html.j2')

@view(path='contas', name='contas')
def contas(request: HttpRequest):
    return render(request, 'contents/contas.html.j2')

@view(path='transacoes', name='transacoes')
def transacoes(request: HttpRequest):
    return render(request, 'contents/transacoes.html.j2')

@view(path='metas', name='metas')
def metas(request: HttpRequest):
    return render(request, 'contents/metas.html.j2')

@view(path='relatorios', name='relatorios')
def relatorios(request: HttpRequest):
    return render(request, 'contents/relatorios.html.j2')

@view(path='investimentos', name='investimentos')
def investimentos(request: HttpRequest):
    return render(request, 'contents/investimentos.html.j2')

@view(path='alertas', name='alertas')
def alertas(request: HttpRequest):
    return render(request, 'contents/alertas.html.j2')

@view(path='configuracoes', name='configuracoes')
def configuracoes(request: HttpRequest):
    return render(request, 'contents/configuracoes.html.j2')