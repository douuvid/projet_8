# Generated by Django 4.2.4 on 2023-09-28 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentification", "0003_book_reviewrequest_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Billet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titre", models.CharField(max_length=200)),
                ("contenu", models.TextField()),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "auteur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="review",
            name="book",
        ),
        migrations.RemoveField(
            model_name="review",
            name="user",
        ),
        migrations.RemoveField(
            model_name="reviewrequest",
            name="book",
        ),
        migrations.RemoveField(
            model_name="reviewrequest",
            name="user",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
        migrations.DeleteModel(
            name="ReviewRequest",
        ),
    ]