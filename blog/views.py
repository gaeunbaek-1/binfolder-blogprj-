from django.shortcuts import render, redirect, get_object_or_404 #import redirect
from .models import Post
from .forms import PostForm #forms.py에서 PostForm 가져오기

# Create your views here.
def main(request):
    posts = Post.objects 
    return render(request, 'post.html', {'posts':posts})

def create(request):
    if request.method == 'POST': #POST vs GET 분기
        form = PostForm(request.POST) #form 변수에 PostForm 할당
        if form.is_valid(): #form  유효성 검증
            form.save() #저장하고
            return redirect('main') #main 페이지로 가기
    else:
        form = PostForm() #빈 form 열기
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
    return render(request, 'update.html', {'form':form})

def detail(request, pk): 
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')