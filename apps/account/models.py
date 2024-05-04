from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager
from apps.company.models import Country


class User(AbstractBaseUser, PermissionsMixin):
    Company = 'C'
    Public = 'P'
    Association = 'A'
    Independent = 'I'
    OrganizationType = [
        (Company, 'Company'),
        (Public, 'Public'),
        (Association, 'Association'),
        (Independent, 'Independent')
    ]
    id = models.BigAutoField(primary_key=True, editable=False)
    email = models.EmailField(
        max_length=255, verbose_name=_("Email Address"), unique=True
    )
    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    phone_number = models.CharField(max_length=13)
    country = models.ForeignKey(Country, models.CASCADE)
    organization_type = models.CharField(
        max_length=50, choices=OrganizationType, default=Company)
    organization_name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number", 'country', 'organization_type', 'organization_name', 'website']
    objects = UserManager()

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"


class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    otp=models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.first_name} - otp code"
