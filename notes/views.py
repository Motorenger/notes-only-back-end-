from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .models import Note

# todo add such thing that you can choose some of question and delete all of them at one time


class NoteListView(LoginRequiredMixin, ListView):
    template_name = 'notes/note_list.html'
    login_url = 'account_login'
    context_object_name = 'all_users_notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('id')


class NoteCreateView(CreateView):
    model = Note
    fields = ['note_text', 'day_planned']
    template_name = 'notes/note_create.html'
    # success_url = 'notes:note_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdateView(UpdateView):
    model = Note
    fields = ['note_text', 'day_planned']
    template_name = 'notes/note_update.html'
    # success_url = 'notes:note_list'


def delete(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()

    return HttpResponseRedirect(reverse('notes:note_list'))


