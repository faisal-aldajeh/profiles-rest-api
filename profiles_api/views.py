
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """ REturns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similer to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'hello!!','an_apiview':an_apiview})
