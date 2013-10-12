from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from contacts.models import *
from django.core.urlresolvers import reverse

class ListContactView(ListView):
    model = Contact
    template_name = "contacts/contacts_list.html"
    context_object_name = "contacts"

class CreateContactView(CreateView):
    model = Contact
    template_name = "contacts/edit_contact.html"
   
    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context
    
    def get_success_url(self):
        return reverse('contacts-list')

class UpdateContactView(UpdateView):
    model = Contact
    template_name = "contacts/edit_contact.html"

    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})
        return context
    
    def get_success_url(self):
        return reverse('contacts-list')

class DeleteContactView(DeleteView):
    model = Contact
    template_name = "contacts/delete_contact.html"
    
    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):
    model = Contact
    template_name = "contacts/contact.html"
