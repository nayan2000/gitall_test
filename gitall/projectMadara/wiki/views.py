from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from comments.models import Comment
from comments.forms import CommentForm
from accounts.models import UserAccount
from tags.models import *
from tags.forms import *

def wiki_home(request):
    n = Wiki.objects.all()
    context = {
        'wiki':n,
    }
    return render(request, 'wiki/wiki.html',context)


def wiki_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = WikiAddForm(request.POST)
            print('yes')
            if form.is_valid():
                print('valid')
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                # return redirect('wiki_home')
                # messages.success(request, "Bann gaya")
                return HttpResponseRedirect(f.get_absolute_url())
            # else:
            #     messages.error(request, "nahi ho paya sorry")
        else:
            form = WikiAddForm()
        return render(request, 'wiki/wiki_add.html', {'form': form})
    else:
        text = "Please Log-in to add a Wiki Page"
        return render(request, 'wiki/wiki_add.html',{'text':text})


def wiki_details(request,slug):
    # n = Wiki.objects.get(id=d)
    instance = get_object_or_404(Wiki, slug=slug)
    print(instance)
    comment = Comment.objects.all()
    tags = instance.tags.all()
    context = {
        # 'wiki':n,
        'tags': tags,
        'comment':comment,
        'instance':instance
    }
    return render(request, 'wiki/wiki_details.html', context)


def wiki_edit(request,slug):
    # n = Wiki.objects.get(id=d)
    instance = get_object_or_404(Wiki, slug=slug)
    if request.method == 'POST':
        form = WikiAddForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            # return redirect('wiki_home')
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = WikiAddForm(instance=instance)
    return render(request, 'wiki/wiki_add.html', {'form':form})

@login_required()
def wiki_community(request,slug):
    instance = get_object_or_404(Wiki, slug=slug)
    initial_data = {
        "content_type": instance.get_content_type,
        "object_id": instance.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)

    if comment_form.is_valid():
        if request.user.is_authenticated:

            c_type = comment_form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            obj_id = comment_form.cleaned_data.get('object_id')
            content_data = comment_form.cleaned_data.get("content")
            parent_obj = None

            try:
                parent_id = int(request.POST.get("parent_id"))

            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            new_comment, created = Comment.objects.get_or_create(
                user=request.user,
                content_type=content_type,
                object_id=obj_id,
                content=content_data,
                parent=parent_obj,
            )
            return HttpResponseRedirect(new_comment.content_object.get_absolute_url() + 'wiki_community')

        else:
            messages.error(request, "You must be logged in to comment!")

    comments = instance.comments

    context = {
        'instance': instance,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'wiki/wiki_community.html', context)


def wiki_resource(request,slug):
    instance = get_object_or_404(Wiki, slug=slug)
    # print(instance.title)
    resource = Resources.objects.all()
    # print(instance.id)
    # wiki_id = request.POST[instance.id]
    # wiki_obj = Community.objects.get(id=wiki_id)
    if request.method == 'POST':
        form = WikiResourceForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            print(f.resource)
            f.user = request.user
            f.wiki = instance.title
            f.save()
            return HttpResponseRedirect(instance.get_absolute_url() + 'wiki_resource/')
    else:
        form = WikiResourceForm()
    context = {
        'form':form,
        'instance':instance,
        'resource':resource,
        'text':'Please Log-in to Add Resource',
    }
    return render(request, 'wiki/wiki_resource.html', context)

def add_tag(request, slug):
	wiki = get_object_or_404(Wiki, slug=slug)
	if not request.user.is_authenticated():
		raise Http404
	add_tags_form =  AddTagsForm(data=request.POST)
	if add_tags_form.is_valid():
		form_instance = add_tags_form.save(commit=False)
		wiki_tags = add_tags_form.cleaned_data['tags']
		for tag in wiki_tags:
			if (len(tag.text.split(' '))>1):
				continue
			wiki.tags.add(tag)
	else:
		add_tags_form = AddTagsForm()


	form = TagForm(data=request.POST)
	text = form['text'].value()
	print(text)
	all = Tag.objects.all()
	flag = 0
	for a in all:
		if (text==a.text):
			flag = 1
			break
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
	else:
		form =  TagForm()
	context = {
		'title': "Create",
		'form' : form,
		'add_tags_form': add_tags_form,
		'instance': wiki,
	}
	return render(request, 'tags/add_wiki.html', context)

def delete_tag(request, slug, text):
	instance = get_object_or_404(Wiki, slug=slug)
	tag = get_object_or_404(Tag, text=text)
	print(instance.tags.all())
	instance.tags.remove(tag)
	print(instance.tags.all())
	instance.save()
	return redirect("wiki:wiki_details", slug=slug)
