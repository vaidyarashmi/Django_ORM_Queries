from django.urls import path,include
from testapp import views
urlpatterns = [
    path('orm_view/', views.orm_view),
]
