# Generated by Django 4.2.7 on 2023-11-28 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_session_session_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='attendance_records',
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendance_records', to='home.session'),
        ),
    ]
