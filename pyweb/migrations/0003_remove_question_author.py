# Generated by Django 3.2.4 on 2021-08-08 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyweb', '0002_rename_subject_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
    ]
