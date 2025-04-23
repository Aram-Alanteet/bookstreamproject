from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import BookTable
from .forms import UserRegistrationForm, BookForm

    
def display_home_page(request):
    return render(request, 'index.html')


def get_bookstreammission(request):
    return render(request, 'bookstreammission.html')


def create_account(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'create_account.html', {'form': form})
   

@login_required
def view_book_entries(request):
    list_of_books = BookTable.objects.all()
    return render(request, 'list_of_books.html', {'list_of_books': list_of_books})


@login_required
def view_book_entry_details(request, book_id):
    book = get_object_or_404(BookTable, pk=book_id)
    return render(request, 'book_details.html', {'book': book})


@login_required
def request_book(request, pk):
    book = get_object_or_404(BookTable, pk=pk)
    if request.user not in book.bk_requesters.all():
        book.bk_requesters.add(request.user)
    return redirect('allocated_books')
    

@login_required
def cancel_book_request(request, pk):
    book = get_object_or_404(BookTable, pk=pk)
    if request.user in book.bk_requesters.all():
        book.bk_requesters.remove(request.user)
    return redirect('allocated_books')
    
      
@login_required
def get_allocated_book_entries(request):
    requested_bks = request.user.requested_bks.all()
    return render(request, 'allocated_books.html', {'requested_bks': requested_bks})


class NewBookEntry(LoginRequiredMixin, CreateView):
    model = BookTable
    form_class = BookForm
    template_name = 'new_book_entry.html'
    success_url = reverse_lazy('list_of_books')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'A new book has been successfully added.')
        return response


class EditBookEntry(LoginRequiredMixin, UpdateView):
    model = BookTable
    form_class = BookForm
    template_name = 'edit_book_entry.html'
    success_url = reverse_lazy('list_of_books')


class DropBookEntry(LoginRequiredMixin, DeleteView):
    model = BookTable
    template_name = 'drop_book_entry.html'
    success_url = reverse_lazy('list_of_books')

    
