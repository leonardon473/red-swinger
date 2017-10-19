from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password,
                     is_active, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)

        user = self.model(email=email,
                          is_active=is_active,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(
            email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email, password, True, True, is_staff=True, **extra_fields)

#Profile Photo
class Profile_photo(models.Model):
	#id_profile_photo = models.AutoField(primary_key=True,unique=True)
	profile_photo = models.URLField()

#Cover Photo
class Cover_photo(models.Model):
	#id_cover_photo = models.AutoField(primary_key=True,unique=True)
	cover_photo = models.URLField()

#Country and country_state
class Country(models.Model):
	#id_country = models.AutoField(primary_key=True,unique=True)
	name_country = models.CharField(max_length=100)

#Country_state
class Country_state(models.Model):
	#id_country_state = models.AutoField(primary_key=True,unique=True)
	id_country = models.ForeignKey(Country)
	state = models.CharField(max_length=100)

class User(AbstractBaseUser, PermissionsMixin, models.Model):
    # unique, no se van a repetir
    id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    nick_name = models.CharField(unique=True,max_length=30)
    email = models.CharField(unique=True, max_length=50)
    profile_swinger_choices = (
        ('A', 'Single Mujer'),
        ('B', 'Single Hombre'),        
        ('C', 'Pareja'),        
    )
    profile_swinger = models.CharField(        
        choices=profile_swinger_choices, max_length=1, blank=True, null=True  
    )
    id_profile_photo = models.ForeignKey(Profile_photo,blank=True, null=True)
    id_cover_photo = models.ForeignKey(Cover_photo,blank=True, null=True)
    biography = models.CharField(max_length=180)
    birdthday = models.DateField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    tattoo = models.BooleanField(default=False)
    piercing = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    '''
    language_choices = (
        (1, 'Español'),
        (2, 'Ingles'),        
        (3, 'Frances'),  
        (4, 'Portugues'),  
        (5, 'Aleman'),        
    )
    language = models.SelectMultipleField(choices = language_choices)
    '''
    street = models.CharField(max_length=50,blank=True, null=True)
    number_ext = models.CharField(max_length=10,blank=True, null=True)
    number_int = models.CharField(max_length=10,blank=True, null=True)
    col = models.CharField(max_length=50,blank=True, null=True)
    state = models.CharField(max_length=50,blank=True, null=True)
    country = models.ForeignKey(Country,blank=True, null=True)
    can_move_choices = (
        ('A', 'Todo el mundo'),
        ('B', 'Mismo país'),        
        ('C', 'Mismo Estado'),        
    )
    can_move = models.CharField(choices=can_move_choices, max_length=1,blank=True, null=True)
    can_host_people_choices = (
        ('A', 'Si, con previo acuerdo'),
        ('B', 'No por el momento'),            
    )
    can_host_people = models.CharField(choices=can_host_people_choices, max_length=1,blank=True, null=True)
    sexual_orientation_choices = (
        ('A', 'Heterosexual'),
        ('B', 'Bisexual'),        
        ('C', 'BiCurioso'),        
    )
    sexual_orientation = models.CharField(choices=sexual_orientation_choices, max_length=1,blank=True, null=True)
    couple_ht = models.BooleanField(default=False)
    couple_bi = models.BooleanField(default=False)
    couple_bi_her = models.BooleanField(default=False)
    couple_bi_him = models.BooleanField(default=False)
    women_ht = models.BooleanField(default=False)
    women_bi = models.BooleanField(default=False)
    men_ht = models.BooleanField(default=False)
    men_bi = models.BooleanField(default=False)
    complete_exchange = models.BooleanField(default=False)
    threesome = models.BooleanField(default=False)
    Cuckold = models.BooleanField(default=False)
    light_exchange = models.BooleanField(default=False)
    only_her = models.BooleanField(default=False)
    Bdsm = models.BooleanField(default=False)
    Gangbang = models.BooleanField(default=False)
    View = models.BooleanField(default=False)
    relation_open = models.BooleanField(default=False)

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.first_name

    def get_username(self):
        return self.email

