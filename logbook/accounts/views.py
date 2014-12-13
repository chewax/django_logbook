from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login
from accounts.forms import RegisterUserForm, AuthenticateUserForm

class LoginUserView(FormView):
    """
    Shows the user login form. Checks for an authenticated user. If so
    redirects him to the home page.
    """

    template_name = 'accounts/login.html'
    form_class = AuthenticateUserForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated():
            #Prevents the "previous page" after login
            #TODO Redirect to the profile page
            return redirect('pages:home')
        else:
            return super(LoginUserView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginUserView, self).form_valid(form)


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

