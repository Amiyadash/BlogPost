from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from PostApp.models import Post
from PostApp.forms import PostForm
from django.contrib import messages

# Create your views here.
def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request," <a href='#'>Posted</a>",extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())
    context_data={
        "form":form
    }
    return render(request, 'post_form.html', context_data)
def post_details(request,id=None):
    #instance=Post.objects.get(id=456) #It Shows An Error If Not Exist
    instance =get_object_or_404(Post,id=id)
    context_data = {
        "instance":instance,
        "title": instance.title,
    }
    return render(request, 'post_details.html',context_data)
def post_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context_data = {
        "title": instance.title,
        "instance": instance,
        "form":form
    }
    return render(request, 'post_form.html', context_data)
def post_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request,"Deleted")
    return redirect('post:list')

def post_list(request):
    queryset=Post.objects.all().order_by("-updated")
    # if request.user.is_authenticated():
    #     context_data={
    #         "name":"User Authenticated"
    #     }
    # else:
    #     context_data = {
    #         "name": "List"
    #     }
    context_data = {
        "object_list":queryset,
        "name": "List"
    }
    return  render(request,'index.html',context_data)   #HttpResponse("<h1>Delete</h1>")


