# Generated by Django 2.0.4 on 2018-04-26 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoo', '0004_auto_20180426_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbor',
            name='fromExhibit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fromExhibit', to='zoo.Exhibit'),
        ),
        migrations.AddField(
            model_name='neighbor',
            name='toExhibit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toExhibit', to='zoo.Exhibit'),
        ),
    ]