from django.http import JsonResponse
from django.shortcuts import render
from api.models import Info
from rest_framework.response import Response

from rest_framework.decorators import api_view
# Create your views here.

from .serializers import InfoSerializer


@api_view(['GET'])
def index(request):
    infos = Info.objects.all()
    serialinfos = InfoSerializer(infos, many=True)
    return Response(serialinfos.data)


@api_view(['GET'])
def dataView(request, pk):
    info = Info.objects.get(id=pk)
    serialinfo = InfoSerializer(info, many=False)
    return Response(serialinfo.data)


@api_view(['POST'])
def dataAdd(request):
    serialdata = InfoSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()
    return Response(serialdata.data)


@api_view(['POST'])
def dataUpdate(request, pk):
    info = Info.objects.get(id=pk)
    serialinfo = InfoSerializer(instance=info, data=request.data)

    if serialinfo.is_valid():
        serialinfo.save()

    return Response(serialinfo.data)


@api_view(['DELETE'])
def datadelete(request, pk):
    info = Info.objects.get(id=pk)
    info.delete()

    students = Info.objects.all()
    serialinfos = InfoSerializer(students, many=True)
    return Response(serialinfos.data)
