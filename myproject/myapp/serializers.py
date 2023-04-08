from rest_framework import serializers
from myapp.models import (MyUser, IncidentCategory, IncidentType, Violation, 
                          Incident, AuditCategory, AuditMeasure, AuditOrganization, 
                          AuditType, AuditStatus, Audit)

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'name', 'email', 'phone', 'jobTitle', 'password', 'role', 'status', 'created_on']

    def create(self, validated_data):
        user = MyUser(name = validated_data['name'], 
                      email = validated_data['email'], 
                      phone = validated_data['phone'], 
                      jobTitle = validated_data['jobTitle'],
                      role = validated_data['role'],
                      status = validated_data['status'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class IncidentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentCategory
        fields = '__all__'


class IncidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentType
        fields = '__all__'


class ViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Violation
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'


class AuditCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditCategory
        fields = '__all__'


class AuditMeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditMeasure
        fields = '__all__'


class AuditOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditOrganization
        fields = '__all__'


class AuditTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditType
        fields = '__all__'


class AuditStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditStatus
        fields = '__all__'


class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audit
        fields = '__all__'