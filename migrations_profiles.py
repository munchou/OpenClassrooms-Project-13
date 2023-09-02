# Generated by Django 3.0 on 2023-08-30 06:08

from django.db import migrations


def move_data_from_old_to_new_model(apps, schema_editor):
    OldModel = apps.get_model("oc_lettings_site", "Profile")
    NewModel = apps.get_model("profiles", "Profile")

    for old_obj in OldModel.objects.all():
        new_obj = NewModel(
            user=old_obj.user,
            favorite_city=old_obj.favorite_city,
        )
        new_obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(move_data_from_old_to_new_model),
    ]
