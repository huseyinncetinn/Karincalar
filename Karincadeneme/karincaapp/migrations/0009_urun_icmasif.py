# Generated by Django 4.2.5 on 2023-09-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karincaapp', '0008_urun_urunkodu_en_urun_urunkodu_tr'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='icMasif',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
