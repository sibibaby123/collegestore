from django.urls import path
from . import views

app_name= 'authentication'

urlpatterns=[
    path('home/',views.allCourse,name="allCourse"),
    path('',views.login_page,name="login_page"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),
    path('dataform/',views.dataform,name="dataform"),
    path('department/<slug>/',views.department,name="department"),
    path('purpose/enquiry/',views.enquiry,name="enquiry"),
    path('purpose/place-order/',views.placeorder,name="placeorder"),
    path('purpose/return/',views.breturn,name="breturn"),
    ]

