# Generated by Django 4.2.7 on 2023-11-27 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_student_id_attendance_student_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('late', 'Late'), ('absent', 'Absent')], default='absent', max_length=10),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
