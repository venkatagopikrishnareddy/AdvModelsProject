# Generated by Django 4.1.7 on 2023-04-11 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApps1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=64)),
                ('f2', models.CharField(max_length=64)),
                ('f3', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='StandardModel',
            fields=[
                ('basicmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyApps1.basicmodel')),
                ('f4', models.CharField(max_length=64)),
                ('f5', models.CharField(max_length=64)),
            ],
            bases=('MyApps1.basicmodel',),
        ),
    ]