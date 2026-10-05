from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = [
        ("admin", "Administrator"),
        ("manager", "Manager"),
        ("cashier", "Cashier"),
        ("supervisor", "Supervisor"),
        ("driver", "Driver"),
        ("staff", "Staff"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="staff")
    phone = models.CharField(max_length=25, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    
        
    def save(self, *args, **kwargs):
        if not self.pk: 
            if self.user.is_superuser:
                self.role = "admin"
        super(Profile, self).save(*args, **kwargs)
        
    
    

