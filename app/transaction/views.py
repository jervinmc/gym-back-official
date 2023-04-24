from django.shortcuts import render
from rest_framework import viewsets,generics
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


class TransactionNotif(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        res = request.data
        try:
            conn = http.client.HTTPSConnection("api.itexmo.com")
            payload = json.dumps({
            "Email": "jmacalawapersonal@gmail.com",
            "Password": "wew123WEW",
            "Recipients": [
                # f"{res.get('contact_number')}"
                "09056949242"
            ],
            "Message": "Your Order with COD request is accepted, now we are preparing to ship your order Thank you!",
            "ApiCode": "TR-JERVI771273_W0L8V",
            "SenderId": "ITEXMO SMS"
            })
            headers = {
            'Content-Type': 'application/json'
            }
            conn.request("POST", "/api/broadcast", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data)

            # api_code = "TR-JERVI771273_W0L8V"

            # # Replace 09xxxxxxxxx with the recipient's mobile number
            # mobile_number = "09056949242"

            # # Replace MESSAGE_HERE with the message you want to send
            # message = "yes"

            # # Send SMS
            # response = requests.get(f"https://www.itexmo.com/php_api/api.php?apikey={api_code}&number={mobile_number}&message={message}")
            # print(data.decode("utf-8"))
            # serializers = NotificationSerializer(data={"user_id":res.get('user_id'),"descriptions":res.get('descriptions'),"image":res.get('image'),"viewed":"no"})
            # serializers.is_valid(raise_exception=True)
            # serializers.save()
            # print(response.text)
            # pusher_client.trigger('notif', 'my-test', {'message': f'Item status : {res.get("status")}','user_id':res.get("user_id")})
        except Exception as e:
            print(e)
        return Response()