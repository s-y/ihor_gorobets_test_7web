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



class AjaxableResponseMixin(object):

    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = form.errors
            data['_error'] = True
            return self.render_to_json_response(data)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = dict(form.data)
            del data['csrfmiddlewaretoken']
            data['_error'] = False
            return self.render_to_json_response(data)
        else:
            return HttpResponse("Request is not ajax")


class ListNoteView(ListView):
    model = Note
    paginate_by = 10
    template_name = 'base/notes.html'


class CreateNoteView(AjaxableResponseMixin, CreateView):
    model = Note
    form_class = AddNoteForm
    template_name = 'base/form.html'
    success_url = '/'
