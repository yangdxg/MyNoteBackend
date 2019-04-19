from django.urls import path
from users.views import Register, Login, MyNotes

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('notes', MyNotes.as_view(), name='notes')
]
