from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('user_login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='user_login'),
    path('user_logout/', auth_views.LogoutView.as_view(next_page='user_login'), name='user_logout'),
    path('availbks', views.view_book_entries, name='list_of_books'),
    path('bk/<int:book_id>/', views.view_book_entry_details, name='book_details'),
    path('bk/new/', views.NewBookEntry.as_view(), name='new_book_entry'),
    path('bk/<int:pk>/edit/', views.EditBookEntry.as_view(), name='edit_book_entry'),
    path('bk/<int:pk>/drop/', views.DropBookEntry.as_view(), name='drop_book_entry'),
    path('bk/<int:pk>/request/', views.request_book, name='request_book'),
    path('bk/<int:pk>/cancelrequest/', views.cancel_book_request, name='cancel_request'),
    path('allocatedbks/', views.get_allocated_book_entries, name='allocated_books'),
    path('', views.display_home_page, name='homepage'),
    path('bookstreammission', views.get_bookstreammission, name='bookstreammission'),
]