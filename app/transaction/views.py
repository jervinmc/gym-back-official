from django.shortcuts import render
from rest_framework import viewsets,generics

from product.models import Product
from product.serializers import ProductSerializer
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
import json
from users.models import User
import requests
from users.serializers import GetUserSerializer
import pusher
import http.client
from decouple import config
class TransactionView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['location']
    queryset=Transaction.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class=TransactionSerializer
    
    def list(self,request):
        instances = Transaction.objects.all()
        serializer_response = TransactionSerializer(instances, many=True)
        for x in serializer_response.data:
            user_instance = User.objects.filter(id = x['user_id']) 
            user_serializer_response = GetUserSerializer(user_instance, many = True)
            print(user_serializer_response.data[0])
            x['firstname'] = user_serializer_response.data[0].get('firstname')
            x['lastname'] = user_serializer_response.data[0].get('lastname')
        
        for x in serializer_response.data:
                p_instance = Product.objects.filter(id=x['product_id'])
                serializer_p = ProductSerializer(p_instance, many=True)
                x['product'] = serializer_p.data[0]
        
        return Response(data = serializer_response.data)
    


class TransactionNotif(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        try:
            conn = http.client.HTTPSConnection("api.itexmo.com")
            payload = json.dumps({
            "Email": "jmacalawa.work@gmail.com",
            "Password": "wew123WEW ",
            "Recipients":[
                "09056949242",
                "09774802231",
                "09053180021"

            ],
            "Message": "Your Order with COD request is accepted, now we are preparing to ship your order Thank you!",
            "ApiCode": "TR-JERVI801969_5IY78",
            "SenderId": "ITEXMO SMS"
            })
            headers = {
            'Content-Type': 'application/json'
            }
            conn.request("POST", "/api/broadcast", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))

            # if response.status_code == requests.codes.ok:
            #     print('Message sent successfully!')
            # else:
            #     print(f'Error sending message: {response.text}')

            # api_code = "TR-JERVI801969_5IY78"

            # # Replace 09xxxxxxxxx with the recipient's mobile number
            # mobile_number = "09056949242"

            # # Replace MESSAGE_HERE with the message you want to send
            # message = "yes"

            # # Send SMS
            # response = requests.get(f"https://www.itexmo.com/php_api/api.php?apikey={api_code}&number={mobile_number}&message={message}")
            # # print(response.decode("utf-8"))
            # # serializers = NotificationSerializer(data={"user_id":res.get('user_id'),"descriptions":res.get('descriptions'),"image":res.get('image'),"viewed":"no"})
            # # serializers.is_valid(raise_exception=True)
            # # serializers.save()
            # print(response.text)
            # pusher_client.trigger('notif', 'my-test', {'message': f'Item status : {res.get("status")}','user_id':res.get("user_id")})
        except Exception as e:
            print(e)
        return Response()
    


class TransactionAllByUser(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        try:
            instance = Transaction.objects.filter(user_id = res.get('user_id'))
            print(instance)
            serializer = TransactionSerializer(instance, many = True)
            
            for x in serializer.data:
                p_instance = Product.objects.filter(id=x['product_id'])
                serializer_p = ProductSerializer(p_instance, many=True)
                x['product'] = serializer_p.data[0]

            print()
            return Response(data = serializer.data)
        except Exception as e:
            print(e)
        return Response()