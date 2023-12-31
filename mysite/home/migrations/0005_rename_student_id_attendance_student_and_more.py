# Generated by Django 4.2.3 on 2023-11-24 11:45

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_professor_user_alter_student_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='class',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='session',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='class',
            name='attendance_records',
            field=models.ManyToManyField(related_name='classes', to='home.attendance'),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='session',
            name='attendance_records',
            field=models.ManyToManyField(related_name='sessions', to='home.attendance'),
        ),
        migrations.AlterField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Course name must be greater than 2 characters')]),
        ),
        migrations.AlterField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(related_name='professors', to='home.course'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 2 characters')]),
        ),
        migrations.AlterField(
            model_name='session',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='home.course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 2 characters')]),
        ),
    ]
