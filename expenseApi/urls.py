from django.urls import path
from . import views
urlpatterns = [
    path("", views.cats, name="cats"),
    path('user_login', views.user_login, name='user_login'),
    path('user_register', views.user_register, name='user_register'),

    #expense urls
    path('expenses', views.AllExpenses.as_view()),
    path('post_expense', views.AppendExpense.as_view()),
    path('delete/<int:pk>', views.deleteExpense.as_view()),
    path('user_expense/<int:user>', views.userExpense),
]