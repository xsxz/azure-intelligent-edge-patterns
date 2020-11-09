# Generated by Django 3.0.8 on 2020-10-28 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("azure_parts", "0001_initial"),
        ("cameras", "0008_remove_camera_send_video_to_cloud"),
    ]

    operations = [
        migrations.CreateModel(
            name="CameraTask",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=200)),
                ("send_video_to_cloud", models.BooleanField(default=False)),
                (
                    "camera",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cameras.Camera"
                    ),
                ),
                ("parts", models.ManyToManyField(blank=True, to="azure_parts.Part")),
            ],
        ),
    ]