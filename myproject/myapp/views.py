from django.shortcuts import render
from myapp.models import (MyUser, IncidentCategory, IncidentType, Violation, 
                          Incident, AuditCategory, AuditMeasure, AuditOrganization, 
                          AuditType, AuditStatus, Audit)
from myapp.serializers import (MyUserSerializer, IncidentCategorySerializer, IncidentTypeSerializer, 
                               ViolationSerializer, IncidentSerializer, AuditCategorySerializer,
                               AuditMeasureSerializer, AuditOrganizationSerializer, AuditTypeSerializer,
                               AuditStatusSerializer, AuditSerializer)
from rest_framework import viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['email'] = user.email

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    lookup_field = 'id'


class IncidentCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncidentCategory.objects.all()
    serializer_class = IncidentCategorySerializer
    lookup_field = 'id'


class IncidentTypeViewSet(viewsets.ModelViewSet):
    queryset = IncidentType.objects.all()
    serializer_class = IncidentTypeSerializer
    lookup_field = 'id'


class ViolationViewSet(viewsets.ModelViewSet):
    queryset = Violation.objects.all()
    serializer_class = ViolationSerializer
    lookup_field = 'id'


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    lookup_field = 'id'


class AuditCategoryViewSet(viewsets.ModelViewSet):
    queryset = AuditCategory.objects.all()
    serializer_class = AuditCategorySerializer
    lookup_field = 'id'


class AuditMeasureViewSet(viewsets.ModelViewSet):
    queryset = AuditMeasure.objects.all()
    serializer_class = AuditMeasureSerializer
    lookup_field = 'id'


class AuditOrganizationViewSet(viewsets.ModelViewSet):
    queryset = AuditOrganization.objects.all()
    serializer_class = AuditOrganizationSerializer
    lookup_field = 'id'


class AuditTypeViewSet(viewsets.ModelViewSet):
    queryset = AuditType.objects.all()
    serializer_class = AuditTypeSerializer
    lookup_field = 'id'


class AuditStatusViewSet(viewsets.ModelViewSet):
    queryset = AuditStatus.objects.all()
    serializer_class = AuditStatusSerializer
    lookup_field = 'id'


class AuditViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    lookup_field = 'id'



