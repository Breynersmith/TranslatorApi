from django.urls import path
from .views import TranslateView, PronounceView

urlpatterns = [
    path('translate/', TranslateView.as_view(), name='text-translator'),
    path('pronounce/', PronounceView.as_view(), name='text-pronounce'),
]



