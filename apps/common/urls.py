from django.urls import path

from .api_endpoints import FrontendTranslationView

urlpatterns = [
    path("FrontendTranslations/", FrontendTranslationView.as_view(), name="frontend-translations"),
]
