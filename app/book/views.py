from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from datetime import datetime

from rest_framework import status, viewsets
from users.models import User
from users.serializers import GetUserSerializer
import pusher
from decouple import config
class BookView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Book.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=BookSerializer

    def list(self,request):
        instances = Book.objects.all()
        serializer_response = BookSerializer(instances, many=True)
        print(serializer_response.data)
        for x in serializer_response.data:
            user_instance = User.objects.filter(id = x['user_id'])
            user_serializer_response = GetUserSerializer(user_instance, many = True)
            print(user_instance)
            x['firstname'] = user_serializer_response.data[0].get('firstname','Anonymous')
            x['lastname'] = user_serializer_response.data[0].get('firstname','Anonymous')
        return Response(data = serializer_response.data)



class CheckBook(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        date = res.get('date')
        date1 = datetime.strptime(date[:10], "%Y-%m-%d")
        # formatted_date = date1.strftime("YYYY-MM-DD")
        instance = Book.objects.filter(appointment_date__date=date1)
        # instance = Book.objects.all()
        serializer_response = BookSerializer(instance,many=True)
        total_response = len(serializer_response.data)
        print(total_response)
        return Response(status=status.HTTP_200_OK,data=total_response)




