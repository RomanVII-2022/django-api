from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, phone, jobTitle, password, role, status, **other_fields):
        email = self.normalize_email(email)
        user = self.model(name=name, email=email, phone=phone, jobTitle=jobTitle, role=role, status=status, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, name, email, phone, jobTitle, password, role, status, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(name, email, phone, jobTitle, password, role, status, **other_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    jobTitle = models.CharField(max_length=100)
    role = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'jobTitle', 'role', 'status']

    def __str__(self):
        return self.name
    

class IncidentCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class IncidentType(models.Model):
    category = models.ForeignKey(IncidentCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Violation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    proposed = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Incident(models.Model):
    vehicle = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    incident = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    description = models.TextField()
    incidentAction = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    incidentDate = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle + ' ' + self.driver
    

class AuditCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class AuditMeasure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class AuditOrganization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class AuditType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class AuditStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Audit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    auditType = models.ForeignKey(AuditType, on_delete=models.CASCADE)
    organization = models.ForeignKey(AuditOrganization, on_delete=models.CASCADE)
    auditMeasure = models.ForeignKey(AuditMeasure, on_delete=models.CASCADE)
    auditCategory = models.ForeignKey(AuditCategory, on_delete=models.CASCADE)
    raisedBy = models.CharField(max_length=100)
    dateRaised = models.DateField()
    dateDue = models.DateField()
    assignedTo = models.CharField(max_length=100)
    auditStatus = models.ForeignKey(AuditStatus, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return self.name

