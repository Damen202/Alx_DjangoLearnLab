# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Post
from rest_framework import generics

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')



class PostListview(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = None  # Add your serializer here
    

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = None  # Add your serializer here
    

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = None  # Add your serializer here

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = None  # Add your serializer here
 

class PostDeleteView(generics.DeleteAPIView):
    queryset = Post.objects.all()
    serializer_class = None  # Add your serializer here

    