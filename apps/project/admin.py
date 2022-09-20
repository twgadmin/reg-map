from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin
from nested_admin import NestedModelAdmin, NestedTabularInline

from django.db import models
from django.forms import Textarea

from apps.project.models import Project, Version, Register, Field, FieldChoice

User = get_user_model()


# ************************* Custom User Creation Start ********************** #

admin.site.unregister(User)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # These are not required fields by default
        # but are making them required while adding through django-admin
        required_fields = ['first_name', 'last_name', 'email']
        for field in required_fields:
            self.fields[field].required = True


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    # Remove permissions and groups from fieldset
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Added new fields for user creation
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email'),
        }),
    )


admin.site.register(User, CustomUserAdmin)


# ************************* Custom User Creation End ********************** #

#admin.site.register((Project, Version, Register, Field))

class FieldChoiceInline(NestedTabularInline):
    model = FieldChoice
    extra = 1

class FieldInline(NestedTabularInline):
    exclude = ('created_by','updated_by')
    extra = 0
    model = Field
    inlines = [FieldChoiceInline]


class RegisterInline(NestedTabularInline):
    exclude = ('created_by','updated_by')
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                           attrs={'rows': 1,
                                  'cols': 40,
                                  'style': 'height: 1em;'})},
    }
    extra = 0
    model = Register
    inlines = [FieldInline]
 

class VersionAdmin(NestedModelAdmin):
    inlines = [RegisterInline]

class RegisterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Register, RegisterAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Project)
admin.site.register(Field)
admin.site.register(FieldChoice)