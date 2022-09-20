from django.db import models

from apps.common.models import BaseModel, AbstractCreatedByModel, AbstractUpdatedByModel
from apps.project.validators import validate_hex_value


class Project(
    BaseModel,
    AbstractCreatedByModel,
    AbstractUpdatedByModel
):
    """
    Track different hardware - like a power supply, a radio, a sewing machine, etc.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    address_size = models.PositiveIntegerField()
    word_size = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class Version(
    BaseModel,
    AbstractCreatedByModel,
    AbstractUpdatedByModel
):
    project = models.ForeignKey(
        Project,
        related_name='versions',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta(BaseModel.Meta):
        unique_together = [('project', 'name'),]


class Register(BaseModel, AbstractCreatedByModel, AbstractUpdatedByModel ):
    version = models.ForeignKey(
        Version,
        related_name='registers',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)

    address = models.PositiveIntegerField()
    size = models.PositiveIntegerField(null=True, default=1)
    description = models.TextField()

    access = models.CharField(max_length=5, null=True, blank=True)
    default = models.PositiveIntegerField(null=True, blank=True)

    def address_to_hex(self):
        return "0x" + format(self.address, '04x').upper()


    class Meta:
        unique_together = [('version', 'name'), ('version','address')]

    def __str__(self):
        return str(self.version.project) +":"+ str(self.version) +":" + self.name


class Field(BaseModel, AbstractCreatedByModel, AbstractUpdatedByModel):
    register = models.ForeignKey(Register, related_name='fields', on_delete=models.CASCADE)

    # BITS 15:0
    range_upper = models.PositiveIntegerField()
    range_lower = models.PositiveIntegerField()

    # UINT
    FIELD_TYPES = [        
        ('INT', 'Signed Integer'),
        ('UINT', 'Unsigned Integer'),
        ('ASCII', 'Text'),
        ('RES', 'Reserved'),
        ('BCD', 'Binary Coded Decimal'),
        ('FLAG_AH', 'Flag, Active High'),
        ('FLAG_AL', 'Flag, Active Low'),
        ('DOUBLE', 'Double Floating Point'),
        ('FLOAT', 'Floating Point'),
        ('MUX', 'Multiplex'),
    ]
    type = models.CharField(
        max_length=10,
        choices=FIELD_TYPES,
        default='UINT' )

    # [1 ms]
    unit_scale = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=5,
        max_digits=10
    )
    unit_type = models.CharField(
        max_length=4,
        blank=True,
        null=True
    )

    # FALL_TIME
    name = models.CharField(max_length=10,
                            default="",
                            blank=True)

    description = models.CharField(max_length=200, default="", blank=True)
    #
    value_min = models.IntegerField(null=True, blank=True)
    value_max = models.IntegerField(null=True, blank=True)

class FieldChoice(models.Model):
    field = models.ForeignKey(Field, related_name='choices', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000, blank=True)

    value = models.BigIntegerField(null=True, blank=True)  # The option value (ie. a mux or binary option)

    def __str__(self):
        return str(self.field) + " : " + self.name + " : " + str(self.value)
