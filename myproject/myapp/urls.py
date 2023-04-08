"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from myapp.views import (UserViewSet, MyTokenObtainPairView, IncidentCategoryViewSet, IncidentTypeViewSet, ViolationViewSet, 
                          IncidentViewSet, AuditCategoryViewSet, AuditMeasureViewSet, AuditOrganizationViewSet, 
                          AuditTypeViewSet, AuditStatusViewSet, AuditViewSet)
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename="users")
router.register('incident-category', IncidentCategoryViewSet, basename="incidentCategory")
router.register('IncidentTypeViewSet', IncidentTypeViewSet, basename="IncidentTypeViewSet")
router.register('ViolationViewSet', ViolationViewSet, basename="ViolationViewSet")
router.register('IncidentViewSet', IncidentViewSet, basename="IncidentViewSet")
router.register('AuditCategoryViewSet', AuditCategoryViewSet, basename="AuditCategoryViewSet")
router.register('AuditMeasureViewSet', AuditMeasureViewSet, basename="AuditMeasureViewSet")
router.register('AuditTypeViewSet', AuditTypeViewSet, basename="AuditTypeViewSet")
router.register('AuditStatusViewSet', AuditStatusViewSet, basename="AuditStatusViewSet")
router.register('AuditViewSet', AuditViewSet, basename="AuditViewSet")
router.register('AuditOrganizationViewSet', AuditOrganizationViewSet, basename="AuditOrganizationViewSet")


urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
