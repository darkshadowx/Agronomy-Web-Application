# Generated by Django 4.2.3 on 2023-07-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_question_account_question_answers_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='describe',
            field=models.CharField(max_length=7650, verbose_name='Describe'),
        ),
    ]