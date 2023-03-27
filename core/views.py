from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.serializer import OrganizationSerializer, OrganizationCreateSerializer
from .models import Holding, Organization, Department, MOL, Property, InventoryList


class OrganizationRetrieve(RetrieveAPIView):
    model = Organization
    serializer_class = OrganizationSerializer
    renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'organization.html'

    def retrieve(self, request, *args, **kwargs):
        queryset = Organization.objects.get(pk=kwargs['pk'])
        return Response({'organization': [queryset]}, template_name='organization.html')


class OrganizationList(ListAPIView):
    queryset = Organization.objects.all()
    model = Organization
    serializer_class = OrganizationSerializer
    renderer_classes = [TemplateHTMLRenderer]

    # template_name = 'organization.html'

    def list(self, request, *args, **kwargs):
        queryset = Organization.objects.all()
        holding_queryset = Holding.objects.all()#TODO мб придется переделывать,/
                                                # потому что 2 кверисета в одной вьюшке такое себе,/
                                                # либо не все поля возвращать

        return Response({'organizations': queryset, 'holdings': holding_queryset}, template_name='organization.html')


@method_decorator(csrf_exempt, name='dispatch')
class OrganizationCreate(CreateAPIView):
    model = Organization
    serializer_class = OrganizationCreateSerializer


# class OrganizationDelete(DestroyAPIView):
#     model = Organization
#     serializer_class = OrganizationSerializer
#
#
# class OrganizationUpdate(DestroyAPIView):
#     model = Organization
#     serializer_class = OrganizationSerializer

