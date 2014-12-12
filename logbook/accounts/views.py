# from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login
from accounts.forms import RegisterUserForm

class LoginUserView(TemplateView):
    template_name = 'accounts/login.html'

class RegisterUserView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        # Register the new user
        user = form.save()

        # Once it is registered it must be loged in
        # we can't take the password from the user.password because it is
        # hashed. The username is OK but is taken from the form for consistency
        username = self.request.POST['username']
        password = self.request.POST['password1']

        # Authenticate method creates backend variables for the user
        user_backend = authenticate(username=username, password=password)

        # Now we can log him in.
        login(self.request, user_backend)

        return super(RegisterUserView, self).form_valid(form)
