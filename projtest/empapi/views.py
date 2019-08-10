from django.shortcuts import render
from django.db.models import Min, Max
from rest_framework import viewsets, filters
from .models import EmpInfo, CompanyList
from .serializers import EmpInfoSerializer, CompListSerializer

# Create your views here.


class EmpInfoView(viewsets.ModelViewSet):
    queryset = EmpInfo.objects.all().order_by('-id')
    serializer_class = EmpInfoSerializer


class CompListView(viewsets.ModelViewSet):
    queryset = CompanyList.objects.all().order_by('-id')
    serializer_class = CompListSerializer


class CompEmpListView(viewsets.ModelViewSet):
    # queryset = CompanyList.objects.all().order_by('-id')

    # queryset = CompanyList.objects.distinct("emp_id").all()

    # queryset2 = CompanyList.objects.order_by('-id').distinct("emp_id").all()
    # queryset = CompanyList.objects.filter(id__in=queryset2).order_by('-id')

    # actions_id = CompanyList.objects.all() \
    #                  .annotate(action_id=Max('emp')) \
    #                  .order_by('-action_id')[:10] \
    #                  .values_list('action_id', flat=True)
    # queryset = CompanyList.objects.filter(id__in=actions_id).order_by('-id')

    queryset = CompanyList.objects.raw('''select distinct on (emp_id) 'def', cl.*, ei.*
                                from empapi_companylist as cl
                                inner join empapi_empinfo as ei on (cl.emp_id = ei.id)
                                order by emp_id desc;''')

    serializer_class = CompListSerializer


class CompListSearchView(viewsets.ModelViewSet):
    # queryset = CompanyList.objects.filter(name='LTI') # OR
    queryset = CompanyList.objects.all()
    serializer_class = CompListSerializer
    # print(str(queryset.query))
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'salary', 'date_of_join', 'experience']