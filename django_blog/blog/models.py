from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.forms import TagWidget
from django import forms



# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  # oldest first (chronological)

    def __str__(self):
        return f'Comment by {self.author} on "{self.post}"'

    def get_edit_url(self):
        return reverse('blog:comment-update', kwargs={'post_pk': self.post.pk, 'pk': self.pk})

    def get_delete_url(self):
        return reverse('blog:comment-delete', kwargs={'post_pk': self.post.pk, 'pk': self.pk})
    

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # lets you type tags like "django, python"
        }
    
