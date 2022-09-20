from django.forms import ModelForm


class CustomBaseModelForm(ModelForm):
    """
    Common ModelForm that handles created_by and updated_by logic
    """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        assert self.request is not None, """
        Should pass request object through form kwargs, Please use RequestInjectMixin in View Class
        """
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.instance.id:
            # If being updated and model has updated_by field
            # add current user as updated_by user
            if hasattr(instance, 'updated_by'):
                instance.updated_by = self.request.user
        else:
            # If being created and model has created_by field
            # add current user as created_by user
            if hasattr(instance, 'created_by'):
                instance.created_by = self.request.user

        if commit:
            instance.save()
        return instance
