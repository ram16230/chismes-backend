# Generated by Django 2.1.2 on 2018-10-17 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chismes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chismes',
            name='content',
            field=models.TextField(),
        ),
    ]
