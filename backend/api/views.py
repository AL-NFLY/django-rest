# from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.serializers

from products.models import Product
from products.serializers import ProductSerializer

import json

# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    Django REST API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=400)