# Generated by Django 4.2.4 on 2023-09-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=500)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
