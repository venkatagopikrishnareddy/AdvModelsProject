# Generated by Django 4.1.7 on 2023-04-11 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApps1', '0002_basicmodel_standardmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyApps1.person')),
                ('eno', models.IntegerField()),
                ('esal', models.FloatField()),
            ],
            bases=('MyApps1.person',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MyApps1.employee')),
                ('exp', models.IntegerField()),
                ('team_size', models.IntegerField()),
            ],
            bases=('MyApps1.employee',),
        ),
    ]
