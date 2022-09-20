from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView

from apps.project.models import Project


class HomePageView(ListView):
    queryset = Project.objects.all()
    template_name = 'home.html'
    context_object_name = 'projects'
    paginate_by = 10


class LoginPageView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'

    def get_success_message(self, cleaned_data):
        return f'Successfully Logged In as {self.request.user}'
