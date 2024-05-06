from django.shortcuts import render
from .models import *
from .serializer import *
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
def cats(request):
    cats = Categories.objects.all()
    serializer = CatSerializer(cats, many=True)
    return JsonResponse(serializer.data, safe=False)

#get data
#serialize
#return json
@csrf_exempt
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:     
        msg = {
            "bool":True,
            'user':user.username,
            'user_id':user.id
        }
    else:
        msg = {
            'bool':False,
            'msg':'Please provide correct credentials!!'
        }
    return JsonResponse(msg)

@csrf_exempt
def user_register(request):
    first = request.POST.get('first')
    last = request.POST.get('last')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')

    user = User.objects.create(
        first_name = first,
        last_name = last,
        username = username,
        email = email
    )
    
    user.set_password(password)
    user.save() 

    if user:   
        newUser = UserAccounts.objects.create(
            user = user,
            mobile = mobile
        )   

        user_serializer = userSerilizer(newUser)

        msg = {
            'bool':True,
            'user':user.id,
            'newUser':user_serializer.data,
            'msg':'Registration successfull, You can now login'
        }
    else:
        msg = {
            'bool':False,
            'msg':'Please fill in al the credentials'
        }
    return JsonResponse(msg)

class AllExpenses(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class AppendExpense(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
           return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        
@api_view(['GET'])
def userExpense(request, user):
   try:
     userExpenses = Expense.objects.filter(user=user)
   except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method == 'GET':
        serialize = ExpenseSerializer(userExpenses, many=True)
        return Response(serialize.data)

class deleteExpense(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
