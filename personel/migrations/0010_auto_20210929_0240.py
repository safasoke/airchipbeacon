# Generated by Django 2.2.17 on 2021-09-28 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personel', '0009_auto_20210324_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personeller',
            name='tc_kimlik_no',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Hakkımda')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Profil Fotoğrafı')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Kullanıcı Profilleri',
            },
        ),
    ]
