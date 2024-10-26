from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

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
            name =serializer1.validated_data.get('name1') # 'name' defined in serializer file
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

class HelloViewSet(viewsets.ViewSet):
    # testing API ViewSet
    serializer_class = serializers.HelloSerializer #using same serializer

    def list(self,request):
        #returns a general message hello
        #<p>hello world<p>
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        # example of rendering with html
        # car_names = ["Tesla Model S", "Ford Mustang", "Chevrolet Camaro"]
        
        # # Build HTML content
        # html_content = "<html><head><style>"
        # html_content += "h1 { color: blue; } ul { font-family: Arial; }"
        # html_content += "</style></head><body>"
        # html_content += "<h1>Car Names</h1><ul>"
        
        # for car in car_names:
        #     html_content += f"<li>{car}</li>"
        
        # html_content += "</ul></body></html>"

        # # Return HTML response
        # return Response(html_content, content_type="text/html")
        return Response({'msg':'hello','a_viewset':a_viewset})

    def create(self,request):
        #creating a general msg
        serializer2 = self.serializer_class(data=request.data)
        if serializer2.is_valid():
            name1 = serializer2.validated_data.get('name') # 'name' defined in serializer file
            message = f' test2 {name1}'
            return Response({'message':message})
        else:
            return Response(serializer2.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
