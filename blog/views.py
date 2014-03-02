from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from blog.models import Post
from blog.forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('-posted')
    return render(request, 'blog/post_list.html', {'posts': posts })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post })

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect(reverse('post_detail', kwargs={'pk': post.pk }))

    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})