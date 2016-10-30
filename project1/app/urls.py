from django.conf.urls import url
from .views import index, contact,PostList, PostDetail
#from . import views
#from app.views import index

urlpatterns = [
    url('^$', PostList.as_view()), #t7awel fnct as view
    url('^contact/?$', contact), #AUCUN ACCEPTE DE N'import quel caractere dans google chrome
    url(r'^post/(?P<pk>\d+)$' , PostDetail.as_view(),
        name="post_detail")
]
