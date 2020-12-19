from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment,Profile
from .forms import PostForm,CommentForm,EditProfileForm
from django.contrib import messages
from django.views.generic import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def HomeView(request):
	User = get_user_model()
	users = User.objects.all()
	profile,created = Profile.objects.get_or_create(user=request.user)
	object_list = Post.objects.filter(author=request.user).order_by('-date_posted')
	
	return render(request,'clone/home.html',{'object_list':object_list,'users':users})

def CreateTweetView(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			messages.info(request,'incorrect info')
			return redirect('create-tweet')
	return render(request,'clone/tweet.html',{'form':form})

def DeletePostView(request,id):
	post = Post.objects.filter(id=id)
	post.delete()
	return redirect('home')


def EditPostView(request,id):
	current_post = Post.objects.get(id=id)
	form = PostForm(instance=current_post)
	
	if request.method == 'POST':
		form = PostForm(request.POST,instance=current_post)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			messages.info(request,'incorrect info')
			return redirect('home')
	return render(request,'clone/edit_post.html',{'form':form})

def CommentView(request,id):
	current_post = Post.objects.filter(id=id)[0]
	form = CommentForm()
	all_comments = Comment.objects.filter(post=current_post)
	
	#object_list = Post.objects.all()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			messages.info(request,'incorrect info')
			return redirect('home')
	
	return render(request,'clone/comment.html',{'form':form,'current_post':current_post,'all_comments':all_comments})

def LikeView(request,pk):
	
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	liked=False 
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked=False
		return redirect('home')
	else:
		post.likes.add(request.user)
		liked = True
		return redirect('home')
	
	return redirect('home')

def EditProfileView(request,pk):
	profile = get_object_or_404(Profile,id=pk)
	form = EditProfileForm(instance=profile)
	if request.method == 'POST':
		form = EditProfileForm(request.POST,request.FILES,instance=profile)
		if form.is_valid():
			print('FORM VALID')
			form.save()
			return redirect('home')
			
		else:
			print('FORM INVALID')
			messages.info(request,'incorrect info')
			return redirect('registration/edit_profile.html')

	return render(request,'registration/edit_profile.html',{'form':form})


def CreateProfileView(request):
	form = EditProfileForm()
	if request.method == 'POST':
		form = EditProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			messages.info(request,'incorrect info')
			return redirect("registration/create_profile.html")
	return render(request,"registration/create_profile.html",{'form':form})

def ShowProfileView(request,pk):
	user_profile = Profile.objects.filter(id=pk)
	print(request.user.profile.id)
	return render(request,'registration/show_profile.html',{'user_profile':user_profile})

def FollowView(request,pk):
	user = User.objects.get(id=pk)
	profile,created = Profile.objects.get_or_create(user=user)
	current_user_profile,created = Profile.objects.get_or_create(user=request.user)
	if profile.followers.filter(id=request.user.id).exists():
		profile.followers.remove(current_user_profile)
		request.user.profile.following.remove(profile)
		return redirect('home')
	else:
		profile.followers.add(current_user_profile)
		request.user.profile.following.add(profile)
		return redirect('home')
	return render(request,'registration/home.html')

def DisplaySearchedUserView(request,pk):
	user = User.objects.get(id=pk)
	post= Post.objects.filter(author=user).order_by('-date_posted')
	profile,created = Profile.objects.get_or_create(user=user)
	return render(request,'clone/searched-user.html',{'user':user,'post':post,"profile":profile})

def LikeSearchedUserView(request,pk):
    	
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	liked=False 
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked=False
		return HttpResponseRedirect(reverse('view-user',kwargs={'pk':int(post.author.id)}))
	else:
		post.likes.add(request.user)
		liked = True
		
		return HttpResponseRedirect(reverse('view-user',kwargs={'pk':int(post.author.id)}))
	
	return redirect('home')