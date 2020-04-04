from django.contrib import admin
from django.urls import path
import session_2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', session_2.views.index, name="index")
]
