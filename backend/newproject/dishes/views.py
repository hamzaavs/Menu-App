from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from dishes.models import MenuItem
from dishes.serializer import MenuItemSerializer


class DishesList(APIView):
    def get(self, request):
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        return Response(serializer.data)


class DishesCreate(APIView):
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Dish(APIView):
    def get_dish_pk(self, unique_id):
        try:
            return MenuItem.objects.get(unique_id=unique_id)
        except MenuItem.DoesNotExist:
            return None

    def get(self, request, unique_id):
        dish = self.get_dish_pk(unique_id)
        if not dish:
            return Response({
                'message': 'Yemek bulunamadı'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuItemSerializer(dish)
        return Response(serializer.data)

    def put(self, request, unique_id):
        dish = self.get_dish_pk(unique_id)
        serializer = MenuItemSerializer(dish, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, unique_id):
        try:
            dish = self.get_dish_pk(unique_id)
            dish.delete()
            return Response({
                'message': 'Yemek silindi'
            }, status=status.HTTP_204_NO_CONTENT)
        except MenuItem.DoesNotExist:
            return Response({
                'message': 'Yemek bulunamadı'
            }, status=status.HTTP_404_NOT_FOUND)

