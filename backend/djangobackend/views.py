from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny

# Create your views here.

def index(request):
    return render(request, 'index.html')

class ReactView(APIView):
    permission_classes = [AllowAny,]
    def get(self, request):
        output =[{"student" : output.student, "branch": output.branch}
                 for output in Data.objects.all()]
        return Response(output)
    

    def post(self, request):
        serializer = ReactSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request):
        # Delete all records from the model
        Data.objects.all().delete()
        return Response({"message": "All records have been deleted."})