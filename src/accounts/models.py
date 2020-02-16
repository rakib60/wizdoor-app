from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username')
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **kwargs):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **kwargs
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin




class Customer(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.customer.username

    def get_full_name(self):
        return ' '.join([self.customer.first_name, self.customer.last_name])

    def get_short_name(self):
        return self.customer.first_name

    @property
    def name(self):
        return self.customer.username
        
    @property
    def full_name(self):
        return ' '.join([self.customer.first_name, self.customer.last_name])