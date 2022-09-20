from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Submit
from django.urls import reverse_lazy

from apps.common.forms import CustomBaseModelForm
from apps.project.models import Project, Version, Register
from apps.project.validators import validate_hex_value


class ProjectForm(CustomBaseModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        submit_text = 'Update changes' if self.instance.id else 'Save changes'
        self.helper = FormHelper()

        # Change form action w.r.to create or update request.
        # Form action is required as we are using form in a pop-up
        if self.instance.id:
            self.helper.form_action = reverse_lazy(
                'project:update',
                kwargs={'pk': self.instance.id}
            )
        else:
            self.helper.form_action = reverse_lazy('project:create')

        self.helper.layout = Layout(
            'name',
            'description',
            Row(
                Column('address_size', css_class='form-group col-md-6 mb-0'),
                Column('word_size', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
                Submit('submit', submit_text),
                css_class='mt-3 text-right'
            ),
        )

    class Meta:
        model = Project
        fields = (
            'name', 'description',
            'address_size', 'word_size'
        )


class VersionForm(CustomBaseModelForm):

    def __init__(self, *args, **kwargs):
        project_field_disabled = kwargs.pop('project_field_disabled', False)
        super().__init__(*args, **kwargs)

        submit_text = 'Update changes' if self.instance.id else 'Save changes'
        self.helper = FormHelper()

        # Change form action w.r.to create or update request.
        # Form action is required as we are using form in a pop-up
        if self.instance.id:
            self.helper.form_action = reverse_lazy(
                'project:version-update',
                kwargs={'pk': self.instance.id}
            )
        else:
            self.helper.form_action = reverse_lazy('project:version-create')

        # Make project field readonly is project_field_disabled is passed
        if project_field_disabled:
            self.fields['project'].widget.attrs['readonly'] = True

        self.helper.layout = Layout(
            'project',
            'name',
            Div(
                Submit('submit', submit_text),
                css_class='mt-3 text-right'
            ),
        )

    class Meta:
        model = Version
        fields = ('project', 'name')


class RegisterForm(CustomBaseModelForm):
    address = forms.CharField(
        validators=[validate_hex_value],
        max_length=20
    )

    def __init__(self, *args, **kwargs):
        version_field_disabled = kwargs.pop('version_field_disabled', False)
        super().__init__(*args, **kwargs)

        submit_text = 'Update changes' if self.instance.id else 'Save changes'
        self.helper = FormHelper()

        # Change form action w.r.to create or update request.
        # Form action is required as we are using form in a pop-up
        if self.instance.id:
            self.helper.form_action = reverse_lazy(
                'project:register-update',
                kwargs={'pk': self.instance.id}
            )
        else:
            self.helper.form_action = reverse_lazy('project:register-create')

        # Make project field readonly is project_field_disabled is passed
        if version_field_disabled:
            self.fields['version'].widget.attrs['readonly'] = True

        self.helper.layout = Layout(
            'version',
            'name',
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                Column('size', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'description',
            Div(
                Submit('submit', submit_text),
                css_class='mt-3 text-right'
            ),
        )

    class Meta:
        model = Register
        fields = ('version', 'name', 'address', 'size', 'description')
