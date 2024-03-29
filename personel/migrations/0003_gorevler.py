# Generated by Django 2.2.16 on 2020-10-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0002_auto_20201028_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gorevler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gorev_adi', models.CharField(blank=True, max_length=50, null=True, verbose_name='Görev İsmi')),
                ('gorev', models.TextField(max_length=1000, null=True, verbose_name='Görev Giriniz')),
                ('personel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personel.Personeller')),
            ],
        ),
    ]
