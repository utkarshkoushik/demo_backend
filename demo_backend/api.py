from rest_framework import generics, permissions,viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import userData
from .serializers import userSerializer

class userDataApi(APIView):

    def get_object(self,pk):
        try:
            return userData.objects.get(pk=pk)
        except userData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        userDetail = self.get_object(pk)
        serialzer = userSerializer(userDetail)
        return Response(serialzer.data)

    def post(self,request,fomrat = None):
        username = userData.objects.filter(pathname = request.data['pathname'])
        email = userData.objects.filter(email = request.data['email'])
        if username and email :
            return Response({
                'msg1' : 'Username already taken',
                'msg2' : 'Email already exists'
            })
        if username :
            return Response({
                'msg1':'Username already taken'
            })
        if email :
            return Response({
                'msg2' : 'Email already exists'
            })
        serializer = userSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
