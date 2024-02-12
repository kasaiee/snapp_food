from rest_framework import viewsets
from app_food.models import Food, Restaurant
from app_food.api.serializers import SearchSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def search(request):
    q = request.GET.get('q', '')
    foods = Food.objects.filter(title__icontains=q)
    restaurants = Restaurant.objects.filter(title__icontains=q)
    serializer = SearchSerializer(list(foods) + list(restaurants), many=True)
    data = serializer.data
    return Response(data)