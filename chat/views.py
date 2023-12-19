from django.shortcuts import render, redirect, get_object_or_404
from chat.forms import ChatMessageForm
from chat.models import Friend, ChatMessage
from profile_page.models import Profile


def chat(request ):
    user = request.user.profile
    friends = user.friends.all()
    context = {'user': user , 'friends' : friends ,}
    return render(request, 'chat/chat.html' , context)


def chat_view(request , pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    form = ChatMessageForm()
    if request.method == 'POST':
        form=ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect('chat_view' , pk=friend.profile.id)
    context = {'friend' : friend , 'form': form , 'user': user , 'profile': profile , 'chats' : chats}
    return render(request , 'chat/chat_view.html', context)
