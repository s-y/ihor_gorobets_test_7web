#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function, unicode_literals

import json
import random

from django.http import HttpResponse
from django.template import Context, Template
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, UpdateView)

from forms import *

from .models import *

# from django.core.urlresolvers import reverse_lazy
# from django.shortcuts import render, get_object_or_404



class CreateNoteView(CreateView):
    model = Note
    form_class = AddNoteForm
    template_name = 'base/form.html'
    success_url = '/'

