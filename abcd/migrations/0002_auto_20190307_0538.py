# Generated by Django 2.1 on 2019-03-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='full_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='yashsharma', max_length=20),
        ),
    ]
