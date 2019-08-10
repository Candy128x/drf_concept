from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('empinfo', views.EmpInfoView)
router.register('complist', views.CompListView)
router.register('com_emp_list', views.CompEmpListView)
router.register('comp_list_search', views.CompListSearchView)

urlpatterns = [
    path('', include(router.urls)),
]

