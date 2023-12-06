from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from profile_page.models import Profile
from registration.forms import UserCreationForm
from django.views import View
from django.contrib.auth import get_user_model

User = get_user_model()


def person_view(request):
    return render(request, 'registration/person.html', )


class Register(View):
    template_name = 'registration/registration.html'


    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                Profile.objects.create(user=user)
                return render(request,
                              'home.html',
                              {'user': user})


                return redirect('home')
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        else:
            form = UserCreationForm()
        return render(request,
                      'registration/registration.html',
                      {'form': form})

