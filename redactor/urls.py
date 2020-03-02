from django.urls import re_path

from redactor.views import redactor_upload
from redactor.forms import FileForm, ImageForm


urlpatterns = [
    re_path('^upload/image/(?P<upload_to>.*)', redactor_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: '<img src="%s" alt="%s" />' % (url, name),
    }, name='redactor_upload_image'),

    re_path('^upload/file/(?P<upload_to>.*)', redactor_upload, {
        'form_class': FileForm,
        'response': lambda name, url: '<a href="%s">%s</a>' % (url, name),
    }, name='redactor_upload_file'),
]