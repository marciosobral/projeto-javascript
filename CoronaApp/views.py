from django.shortcuts import render
from django.http import HttpResponse


def mensagem(request):
    mensagem = "Hello World"
    return HttpResponse(mensagem)
