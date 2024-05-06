from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name", "image"]
class userSerilizer(serializers.ModelSerializer):
    class Meta:
        model = UserAccounts
        fields = ['id', 'user', 'mobile']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user','image', 'item', 'Amount', 'category', 'date']
