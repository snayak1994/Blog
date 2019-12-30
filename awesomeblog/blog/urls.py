from django.conf.urls import url
from .views import IndexView,PostDetailView,CreatePostView,PostEditView,PostDeleteView
urlpatterns = [
    url(r'^$',IndexView.as_view(),name='home'),
    url(r'^article/(?P<pk>\d+)/$',PostDetailView.as_view(), name='post-detail'),
    url(r'^article/new/$',CreatePostView.as_view(), name='post-new'),
    url(r'^article/edit/(?P<pk>\d+)/$',PostEditView.as_view(), name='post-edit'),
    url(r'^article/(?P<pk>\d+)/remove$',PostDeleteView.as_view(), name='post-delete'),
]