from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from registration.forms import UserCreationForm
from django.views import View
from django.contrib.auth import get_user_model

User = get_user_model()


def person_view(request):

    return render(request, 'registration/person.html' , )


class Register(View):
    template_name = 'registration/registration.html'


    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)


            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

