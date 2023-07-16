from django.urls import path
from demo.views import PersonOptions

urlpatterns = [
    path('', PersonOptions.as_view()),
    path('add/', PersonOptions.as_view()),
    path('modify/<int:id>/', PersonOptions.as_view()),
    path('delete/', PersonOptions.as_view()),
]
