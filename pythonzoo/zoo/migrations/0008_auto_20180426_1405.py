# Generated by Django 2.0.4 on 2018-04-26 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0007_auto_20180426_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='animals',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animalAtExhibit', to='zoo.Animal'),
        ),
    ]
