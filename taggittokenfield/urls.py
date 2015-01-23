from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^tags/', 'taggittokenfield.views.filter_tags'),
)