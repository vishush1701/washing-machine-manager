from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .models import WashingMachine
from rest_framework.generics import ListAPIView,UpdateAPIView
from .serializers import WashingMachineSerializer

# Create your views here.

@api_view(['GET'])
def test(request):
    data = {
        'name':'vishwa',
        'age':24
    }
    return Response(data=data,status=HTTP_200_OK)

class WashingMachineListView(ListAPIView):
    '''
    To get all the washing machines and also option to filter based on availability
    '''
    model = WashingMachine
    # queryset = WashingMachine.objects.all()
    serializer_class = WashingMachineSerializer

    def get_queryset(self):
        queryset = WashingMachine.objects.all()
        if self.request.query_params.get('is_available'):
            queryset = queryset.filter(is_available = self.request.query_params.get('is_available'))
        return queryset

class WashingMachineUpdateView(UpdateAPIView):
    model = WashingMachine
    serializer_class = WashingMachineSerializer
    queryset = WashingMachine.objects.all()
