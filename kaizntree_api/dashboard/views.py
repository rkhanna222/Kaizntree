from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer, UserSerializer

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        stock_status = self.request.query_params.get('stock_status')

        if category:
            queryset = queryset.filter(category=category)
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)

        return queryset
    
# User Registration View
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            data['response'] = "Successfully registered a new user."
            data['username'] = user.username
            data['email'] = user.email
            data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED if serializer.is_valid() else status.HTTP_400_BAD_REQUEST)

