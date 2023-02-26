# Generated by Django 4.1.7 on 2023-02-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('superuser', 'Super admin'), ('admin', 'Enterprise admin'), ('employee', 'Enterprise employee')], max_length=20)),
            ],
        ),
    ]