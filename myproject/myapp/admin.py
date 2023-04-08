from django.contrib import admin
from myapp.models import (MyUser, IncidentCategory, IncidentType, Violation, 
                          Incident, AuditCategory, AuditMeasure, AuditOrganization, 
                          AuditType, AuditStatus, Audit)

admin.site.register(MyUser)
admin.site.register(IncidentCategory)
admin.site.register(IncidentType)
admin.site.register(Violation)
admin.site.register(Incident)
admin.site.register(AuditCategory)
admin.site.register(AuditMeasure)
admin.site.register(AuditOrganization)
admin.site.register(AuditType)
admin.site.register(AuditStatus)
admin.site.register(Audit)