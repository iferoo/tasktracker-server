from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TaskViews(APIView):
    def post(self, request):
        serializer = TaskSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "task": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "task": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, id=None):
        if id != None:
            task = Task.objects.get(id=id)
            serializer = TaskSerilizer(task)
            return Response(
                {"status": "success", "task": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            tasks = Task.objects.all()
            serializer = TaskSerilizer(tasks, many=True)
            return Response(
                {"status": "success", "tasks": serializer.data},
                status=status.HTTP_200_OK,
            )

    def put(self, request, id=None):
        task = Task.objects.get(id=id)
        serializer = TaskSerilizer(
            task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "task": serializer.data})
        else:
            return Response({"status": "error", "task": serializer.errors})

    def delete(self, request, id=None):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return Response({"status": "success", "task": "Item Deleted"})