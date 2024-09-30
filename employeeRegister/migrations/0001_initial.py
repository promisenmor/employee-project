# Generated by Django 4.2.16 on 2024-09-30 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=250)),
                ('Emp_code', models.IntegerField(max_length=16)),
                ('mobile', models.IntegerField(max_length=16)),
                ('Address', models.CharField(max_length=250)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeRegister.position')),
            ],
        ),
    ]