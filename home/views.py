from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm, CommentForm
from home.models import Post, Friend


class HomeView(TemplateView):
    template_name = 'home/home.html'
    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        args = {
            'form': form, 'posts': posts, 'users': users, 'friends': friends
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')

def single_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            post.comments.add(comment)
            text = form.cleaned_data['comment']
            form = CommentForm()
            print(pk)
            return redirect('home:single_post', pk )
        args = {'form': form, 'text': text}
        return render(request,'home/single_post.html', args)
    elif request.method =='GET' :
        form = CommentForm()
        comments = post.comments.all()
        args = {'form':form,'post':post,'comments':comments}
        return render(request,'home/single_post.html', args)
