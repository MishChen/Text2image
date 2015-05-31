#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
 
class PostForm(forms.Form):
    content = forms.CharField(max_length=256)
    created_at = forms.DateTimeField()