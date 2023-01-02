from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
# from datetime import datetime

"""Database models for the users [student/nurse/doctor]"""
class UserAccountManager(BaseUserManager):
    
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
        
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_doctor(self, email, name, password=None):
        user =self.create_user(email, name, password)
        user.is_doctor = True
        user.save()

        return user
    
    def create_nurse(self, email, name, password=None):
        user =self.create_user(email, name, password)
        user.is_nurse = True
        user.save()

        return user
    
    def create_student(self, email, name, password=None):
        user =self.create_user(email, name, password)
        user.is_student = True
        user.save()

        return user

"""Database models for the users"""
class UserAccount(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_doctor = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

"""Database model for Student Profile"""
class Student(models.Model):

    class Vaccined(models.TextChoices):
        FULL = "FULL", _("Fully Vaccinated")
        FIRSTDOSE = "FIRSTDOSE", _("First Dose")
        NEVER = "NEVER", _("Never")

    class Boostered(models.TextChoices):
        FULL = "FULL", _("Fully Boostered")
        FIRSTBOOST = "FIRSTBOOST", _("First Boost")
        NEVER = "NEVER", _("Never")

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    class CivilStatus(models.TextChoices):
        SINGLE = "S", _("Single")
        MARRIED = "M", _("Married")
        WIDOW = "W", _("Widow")
        OTHERS = "O", _("Others")

    class BloodTypes(models.TextChoices):
        A = "A", _("A")
        B = "B", _("B")
        AB = "AB", _("AB")
        O = "O", _("O")
        NA = "NA", _("No Answer")

    Hypertension = 'HT'
    Cancer = 'C'
    Hospitalization = 'HP'
    KidneyDisease = 'KD'
    DiabetesMellitus = 'DM'
    HeartDisease = 'HD'
    ThyroidDisease = 'TD'
    SurgicalOperation = 'SO'
    Stroke = 'S'
    BronchialAsthma = 'BA'
    Others = 'O'
    NA = 'NA'

    MedicalHistory = [
        (Hypertension, "Hypertension"),
        (Cancer, "Cancer"),
        (Hospitalization, "Hospitalization"),
        (KidneyDisease, "Kidney Disease"),
        (DiabetesMellitus, "Diabetes Mellitus"),
        (HeartDisease, "Heart Disease"),
        (ThyroidDisease, "Thyroid Disease"),
        (SurgicalOperation, "Surgical Operation"),
        (Stroke, "Stroke"),
        (BronchialAsthma, "Bronchial Asthma"),
        (Others, "Other Disease"),
        (NA, "None")
    ]

    FamilyHistory = [
        (Hypertension, "Hypertension"),
        (Cancer, "Cancer"),
        (KidneyDisease, "Kidney Disease"),
        (DiabetesMellitus, "Diabetes Mellitus"),
        (HeartDisease, "Heart Disease"),
        (ThyroidDisease, "Thyroid Disease"),
        (Stroke, "Stroke"),
        (BronchialAsthma, "Bronchial Asthma"),
        (Others, "Other Disease"),
        (NA, "None")
    ]

    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    student_id = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=255, unique=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True)
    civil_status = models.CharField(max_length=50, choices=CivilStatus.choices, default=CivilStatus.SINGLE)
    address = models.CharField(max_length=255, null=True)
    barangay = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    is_vaccined = models.CharField(
        max_length=50, choices=Vaccined.choices, default=Vaccined.FULL
    )
    is_boostered = models.CharField(
        max_length=50, choices=Boostered.choices, default=Boostered.NEVER
    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    emergencyContact_person = models.CharField(max_length=255, null=True)
    emergencyContact_address = models.CharField(max_length=255, null=True)
    emergencyContact_phone = models.CharField(max_length=15, null=True)

    blood_type = models.CharField(max_length=15, null=True, choices=BloodTypes.choices, default=BloodTypes.NA)
    past_medical_history = MultiSelectField(choices=MedicalHistory,null=True, blank=True, max_length=255)
    other_medical_history = models.CharField(max_length=255, null=True, blank=True)
    hospitalization_medical_history = models.CharField(max_length=255, null=True, blank=True)
    surgical_operation_medical_history = models.CharField(max_length=255, null=True, blank=True)
    family_history = MultiSelectField(choices=FamilyHistory, null=True, blank=True, max_length=255)
    allergies_medications = models.CharField(max_length=255, null=True, blank=True)
    allergies_food = models.CharField(max_length=255, null=True, blank=True)
    allergies_others = models.CharField(max_length=255, null=True, blank=True)

    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.name)


"""Database model for Doctor Profile"""
class Doctor(models.Model):

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    doctor_id = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=255, unique=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True)
    address = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    emergencyContact_person = models.CharField(max_length=255, null=True)
    emergencyContact_phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.name)


"""Database model for Nurse Profile"""
class Nurse(models.Model):

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    nurse_id = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=255, unique=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=Gender.choices, null=True)
    address = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    emergencyContact_person = models.CharField(max_length=255, null=True)
    emergencyContact_phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return str(self.name)

