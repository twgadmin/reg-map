from django.views.generic import FormView


class RequestInjectMixin(FormView):
    """
    Provide request object to Django Form
    """

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
