# Generated by Django 4.1.4 on 2023-01-02 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_doctor', models.BooleanField(default=False)),
                ('is_nurse', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('student_id', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('is_vaccined', models.CharField(choices=[('FULL', 'Fully Vaccinated'), ('FIRSTDOSE', 'First Dose'), ('NEVER', 'Never')], default='FULL', max_length=50)),
                ('is_boostered', models.CharField(choices=[('FULL', 'Fully Boostered'), ('FIRSTBOOST', 'First Boost'), ('NEVER', 'Never')], default='NEVER', max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('emergencyContact_person', models.CharField(max_length=255, null=True)),
                ('emergencyContact_phone', models.CharField(max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('nurse_id', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('emergencyContact_person', models.CharField(max_length=255, null=True)),
                ('emergencyContact_phone', models.CharField(max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('doctor_id', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('birthdate', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('emergencyContact_person', models.CharField(max_length=255, null=True)),
                ('emergencyContact_phone', models.CharField(max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]