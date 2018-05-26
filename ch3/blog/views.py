from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.http import Http404


def post_list(request):
     qs = Post.objects.all()
     q = request.GET.get('q', '')
     if q:
        qs = qs.filter(content__icontains=q)
     return render(request, 'blog/post_list.html', {
        'post_list': qs,
 })

def post_detail(request, id):
    get_object_or_404(Post, id=id)
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html',{
        'post': post,
    })
