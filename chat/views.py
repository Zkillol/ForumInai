from django.contrib import messages
from django.shortcuts import render, redirect
from chat.forms import ChatMessageForm
from chat.models import Friend, ChatMessage
from profile_page.models import Profile

def chat(request):
    if request.user.is_authenticated:
        user = request.user

        if hasattr(user, 'profile'):
            profile = user.profile
            friends = profile.friends.all()
            context = {'user': user, 'friends': friends}
            return render(request, 'chat/chat.html', context)
        else:
            return render(request, 'error_template.html', {'error_message': 'User profile not found'})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')


def chat_view(request ,pk):
    if request.user.is_authenticated:

        friend = Friend.objects.get(profile_id=pk)
        user = request.user
        profile = Profile.objects.get(id=friend.profile.id)
        chats = ChatMessage.objects.all()
        form = ChatMessageForm()
        if request.method == 'POST':
            form = ChatMessageForm(request.POST)
            if form.is_valid():
                chat_message = form.save(commit=False)
                chat_message.msg_sender = user.profile
                chat_message.msg_receiver = profile
                chat_message.save()
                return redirect('chat_view' , pk=friend.profile.id)
        # print(user.is)
        context = {'friend' : friend , 'form': form , 'user': user , 'profile': profile , 'chats' : chats}
        return render(request , 'chat/chat_view.html', context)
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')