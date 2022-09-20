from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class BaseModel(models.Model):
    """
    Base model for this project.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class AbstractCreatedByModel(models.Model):
    """
    Store information of user responsible for object creation.
    """
    created_by = models.ForeignKey(
        User,
        related_name="created_%(class)s",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        abstract = True


class AbstractUpdatedByModel(models.Model):
    """
    Store information of user responsible for last object update.
    """
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="updated_%(class)s",
        null=True
    )

    class Meta:
        abstract = True
