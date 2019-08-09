from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmer', views.ProgrammerView)
router.register('prog_lang', views.ProgLangView)

urlpatterns = [
    path('', include(router.urls)),
]

