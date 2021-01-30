from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/languages/$',
        views.add_language,
        name='add_language'
    )
]
