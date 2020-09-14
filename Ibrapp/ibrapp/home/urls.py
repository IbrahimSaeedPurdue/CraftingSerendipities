from django.urls import path
from . import views
from .views import PostListView,PostCreateView,PostUpdateView,PostDeleteView,PostDetailView,UserPostListView

urlpatterns = [
    path('',views.home,name='home-main'),
    path('store/',views.store,name='store-main'),
    path('suggest/',PostListView.as_view(),name='suggest-main'),
    path('user<str:username>', UserPostListView.as_view(), name='suggest-userposts'),
    path('suggest/new/',PostCreateView.as_view(),name='suggest-create'),
    path('suggest/<int:pk>/update/',PostUpdateView.as_view(),name='suggest-update'),
    path('suggest/<int:pk>/delete/', PostDeleteView.as_view(), name='suggest-delete')
]