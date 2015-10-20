from django.conf.urls import include, url
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token

from board.urls import router

from todo.api import ItemResource

item_resource = ItemResource()

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    #url(r'^api/', include(router.urls)),
    #url(r'^$', TemplateView.as_view(template_name='board/index.html')),
	url(r'^$', TemplateView.as_view(template_name='todo/index.html')),
	url(r'^api/', include(item_resource.urls)),	
]
