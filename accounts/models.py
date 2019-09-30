from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_active=True, is_admin=False,is_staff=False,is_supplier=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.Staff = is_staff
        user_obj.Supplier = is_supplier
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,email,password=None):
        superuser =self.create_user(email,password=password,is_admin=True,is_staff=True)
        return superuser

    def create_staffuser(self,email,password=None):
        staffuser= self.create_user(email,password=password,is_staff=True)
        return staffuser

    def create_supplieruser(self,email,password=None):
        supplieruser = self.create_user(email,password=password,is_supplier=True)
        return supplieruser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    Staff = models.BooleanField(default=False)
    Supplier = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_email(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.Staff

    @property
    def is_supplier(self):
        return self.Supplier
