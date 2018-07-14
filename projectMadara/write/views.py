# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Responsible for converting description into sharable text.
from urllib.parse import quote_plus
from tags.forms import TagForm
from tags.models import *
from .forms import TotoForm, AddTagsForm
from .models import Toto
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Q
from comments.models import Comment
from comments.forms import CommentForm
from accounts.models import UserAccount

def toto_create(request):
	"""
		This makes sure that the form accpets a POST requests (of some data) or Nothing.
		Without this the form would even accept empty totos.
	"""
	if not request.user.is_authenticated():
		raise Http404

	form = TotoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		filter_content(instance.content)
		toto_tags = form.cleaned_data['tags']
		print(toto_tags)
		instance.user = request.user
		instance.save()
		for tag in toto_tags:
			if (len(tag.text.split(' '))>1):
				messages.error(request, "Tags cant contain spaces", extra_tags='')
				continue
			instance.tags.add(tag)
		tags = instance.tags.all()
		print(tags)
		messages.success(request, "Toto created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something went wrong", extra_tags="")
	context = {
		'title': "Create",
		'form' : form,
	}
	return render(request, 'write/write.html', context)

def toto_detail(request, slug):
	instance 		= get_object_or_404(Toto, slug=slug)


	if instance.publish > timezone.now() or instance.draft:
		if not request.user == instance.user:
			raise Http404

	tags = instance.tags.all()
	share_string = quote_plus("Hey! I've just started learning from gitall.tech. It's cool. Check them out!!!")
	add_tags_form = AddTagsForm(request.POST or None)

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
								user = request.user,
								content_type= content_type,
								object_id = obj_id,
								content = content_data,
								parent = parent_obj,
									)
			return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

		else:
			messages.error(request,"You must be logged in to comment!")




	comments = instance.comments

	context = {
		'instance'		: instance,
		'title'			: "Details",
		'share_string' 	: share_string,
		'comments' : comments,
		'comment_form' : comment_form,
		"tags":tags,
	}
	return render(request, 'write/detail.html', context)

def toto_edit(request, slug):
	# This retuns the data (for form) the particular toto
	instance = get_object_or_404(Toto, slug=slug)

	if not request.user == instance.user:
		raise Http404

	# if not request.user.is_superuser or not request.user.is_staff:
	# 	raise Http404

	"""
		without instance=instance part, the form would be an empty form
		instance=instance essentially adds value of the instance to the form
	"""
	form = TotoForm(request.POST or None, request.FILES or None, instance=instance)

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Edited nicely!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Something didn't edit.", extra_tags="")

	context = {
		'title': "Edit",
		'instance' : instance,
		'form': form,
	}
	return render(request, 'write/edit.html', context)

def toto_list(request):
	# queryset_list = Toto.objects.all().order_by("-timestamp")
	# queryset_list = Toto.objects.filter(draft=False).filter(publish__lte=timezone.now())
	# the above command is implemented by using
	queryset_list = Toto.objects.active()

	query = request.GET.get('query')
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query)|
				Q(user__last_name__icontains=query)).distinct()

	paginator = Paginator(queryset_list, 1)

	page = request.GET.get('page')

	try:
		queryset_list = paginator.page(page)
	except PageNotAnInteger:
		queryset_list = paginator.page(1)
	except EmptyPage:
		queryset_list = paginator.page(paginator.num_pages)

	context = {
		"toto_list" : queryset_list,
		"title" : "List",
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"tut_list" : queryset,
	# 		"title": "my list",
	# 	}
	# else:
	# 	context = {
	# 		'title' : "list"
	# 	}
	return render(request, 'write/list.html', context)

def toto_delete(request, slug):
	instance = get_object_or_404(Toto, slug=slug)
	if not request.user == instance.user:
		raise Http404
	instance.delete()
	context = {
		'title': "Delete",
	}
	# messages.success(request, "Deteted")
	return redirect("toto:list")

def toto_draft(request):
	query = Toto.objects.draft()

	context = {
		'draft_list' : query,
	}

	return render(request, 'write/draft_list.html', context)

def filter_content(content):
	print(content)

def add_tag(request, slug):
	toto = get_object_or_404(Toto, slug=slug)
	if not request.user.is_authenticated():
		raise Http404
	add_tags_form =  AddTagsForm(data=request.POST)
	if add_tags_form.is_valid():
		form_instance = add_tags_form.save(commit=False)
		toto_tags = add_tags_form.cleaned_data['tags']
		for tag in toto_tags:
			if (len(tag.text.split(' '))>1):
				continue
			toto.tags.add(tag)
	else:
		add_tags_form = AddTagsForm()


	form = TagForm(data=request.POST)
	text = form['text'].value()
	print(text)
	toto = get_object_or_404(Toto, slug=slug)
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
		'instance': toto,
	}
	return render(request, 'tags/add.html', context)

def delete_tag(request, slug, text):
	instance = get_object_or_404(Toto, slug=slug)
	tag = get_object_or_404(Tag, text=text)
	print(instance.tags.all())
	instance.tags.remove(tag)
	print(instance.tags.all())
	instance.save()
	return redirect("toto:detail", slug=slug)
