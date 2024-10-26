from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    #Test API View
    serializer_class = serializers.HelloSerializer
    def get(self,request,format=None):
        #returns a list
        an_apiview=['hello','api world','sample testing for get']
        return Response({'dummy':'data','an_apiview':an_apiview})
    
    def post(self,request):
        #create a test message with name
        serializer1 = self.serializer_class(data=request.data)
        #doing validation
        if serializer1.is_valid():
            name = serializer1.validated_data.get('name') # 'name' defined in serializer file
            message = f' test {name}'
            return Response({'message':message})
        else:
            return Response(serializer1.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        #updates an object" eg:if lastname is provided , it will update it and delete the other fields
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        #updates an field in an object which is provided i.e;partial update eg:if lastname is provided , it will update it and keep other fields
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        #deletes an object
        return Response({'method':'DELETE'})