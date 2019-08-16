# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Business, Community, Resident 
from django.contrib.auth.decorators import login_required
from .forms import NewBusinessForm, NewCommunityForm, NewCommentForm
from django.contrib.auth.models import User


def welcome(request):
    community = Community.objects.all()
    return render(request,'home.html',{"community": community})

def businesses(request, hood_id):
    business = Business.objects.filter(community_id=hood_id)
    print([x.details for x in business])
    return render(request,'businesses.html',{"business": business})

def residents(request):
    residents = Resident.objects.all()
    return render(request,'residents.html',{"residents":residents})

def comments(request):
    comments = Comment.objects.all()
    return render(request,'businesses.html',{"comments":comments})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user
    if request.method =='POST':
        form = NewBusinessForm(request.POST, request.FILES)

        if form.is_valid():
            business = form.save(commit=False)
            business.resident = current_user
            business.save()
            return redirect('welcome')


    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form":form})
    

@login_required(login_url='/accounts/login/')
def new_community(request):
    current_user = request.user
    if request.method =='POST':
        form = NewCommunityForm(request.POST, request.FILES)

        if form.is_valid():
            community = form.save(commit=False)
            community.resident = current_user
            community.save()
        return redirect('welcome')


    else:
        form = NewCommunityForm()
    return render(request, 'new_community.html', {"form":form})

@login_required(login_url='/accounts/login/')
def new_comment(request):
    current_user = request.user
    if request.method =='POST':
        form = NewCommentForm(request.POST, request.FILES)

        if form.is_valid():
            community = form.save(commit=False)
            community.resident = current_user
            community.save()
        return redirect('welcome')


    else:
        form = NewCommentForm()
    return render(request, 'newcomments.html', {"form":form})
