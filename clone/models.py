from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True,max_length=30)
    profile_pic = models.ImageField(default='default.png',upload_to="images/profile/")
    following = models.ManyToManyField("self",symmetrical = False,blank=True)
    followers = models.ManyToManyField('self',symmetrical = False,blank=True,related_name='followers_profile_test')

    def __str__(self):
        return str(self.user)

    
    
    @property
    def profile_picURL(self):
        try:
            url = self.profile_pic.url
        except:
            url = " "
        return url
    
    def get_absolute_url(self):
        return reverse("home")
    
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name = "blog_posts",blank=True)

    def __str__(self):
        return self.content
    
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_post_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=255)

    def __str__(self):
        return self.comment


