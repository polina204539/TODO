from django.shortcuts import render
from .models import Todolist
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoModelSerializer

class TodolistView(APIView):

    def get(self, request):
        todo = Todolist.objects.all()
        todo_s = TodoModelSerializer(todo, many=True)
        return Response(todo_s.data)
    
    def post(self, request):
        serializer = TodoModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

class TodoDetailView(APIView):

    def get(self, request, id):
        todo = Todolist.objects.get(id=id)
        todo_s = TodoModelSerializer(todo)
        return Response(todo_s.data)
        
    def put(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        if not id:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Todolist.objects.get(id=id)
        except:
            return Response({"error": "Object does not exists"})

        serializer = TodoModelSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
    
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id", None)
        if not id:
            return Response({"error": "Method DELETE not allowed"})

        todo = Todolist.objects.get(id=id)
        todo.delete()

        return Response({"post": "delete post " + str(id)})




