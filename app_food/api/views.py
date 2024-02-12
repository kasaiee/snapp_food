from rest_framework import viewsets
from app_food.models import Food, Restaurant
from app_food.api.serializers import SearchSerializer, FoodSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def search(request):
    q = request.GET.get('q', '')
    foods = Food.objects.filter(title__icontains=q)
    restaurants = Restaurant.objects.filter(title__icontains=q)
    serializer = SearchSerializer(list(foods) + list(restaurants), many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def food_list(request):
    page_size = 3
    page = int(request.GET.get('page', 1))
    food = Food.objects.all()[(page - 1) * page_size: page * page_size]
    serializer = FoodSerializer(food, many=True)
    data = serializer.data
    return Response(data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    serializer = FoodSerializer(food)
    data = serializer.data
    return Response(data)