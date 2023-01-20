from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer
from django.http import HttpResponse
from django.shortcuts import redirect, render


class AlunoViewSet (viewsets.ModelViewSet):
            queryset = Aluno.objects.all()
            serializer_class = AlunoSerializer

def home(request):
    if request.session.get('usuario'):
        
        class AlunoViewSet (viewsets.ModelViewSet):
            queryset = Aluno.objects.all()
            serializer_class = AlunoSerializer
    else:
        return redirect('/auth/login/?status=2')


