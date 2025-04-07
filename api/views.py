from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Logger
from .serializer import LoggerSerializer

@api_view(['GET'])
def get_logs(request):
    logs = Logger.objects.all()
    serializer = LoggerSerializer(logs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_log(request):

    serializer = LoggerSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)