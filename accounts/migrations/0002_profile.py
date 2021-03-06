# Generated by Django 3.2 on 2021-10-06 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_custom_auth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='images/profile_pics/default_icon.jpg', force_format=None, keep_meta=True, null=True, quality=70, size=[320, 320], upload_to='images/profile_pics/')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('is_private_account', models.BooleanField(blank=True, null=True)),
                ('following', models.ManyToManyField(blank=True, related_name='followers', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
