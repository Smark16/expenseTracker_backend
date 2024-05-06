from django.contrib import admin
from .models import *
# Register your models here.
class catAdimn(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

class userAdimn(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'user']

class profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'image']

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','image', 'item', 'Amount', 'category', 'date']

admin.site.register(Categories, catAdimn)
admin.site.register(UserAccounts, userAdimn)
admin.site.register(Profile, profileAdmin)
admin.site.register(Expense, ExpenseAdmin)