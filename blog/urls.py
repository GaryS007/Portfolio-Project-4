from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('contact/', views.contact_form, name='contact'),
    path('contact/', views.contact_page, name='contact_page'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('like/<slug:slug>', views.post_like, name='post_like'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),  # noqa
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),  # noqa
    path('search_recipes', views.search_recipes, name='search_recipes'),
]
