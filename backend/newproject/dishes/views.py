from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MenuItem
from .serializer import MenuItemSerializer


class MenuApiView():
    @api_view(['GET'])
    def dishes_list(request):
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def dishes_create(request):
        serializer = MenuItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)