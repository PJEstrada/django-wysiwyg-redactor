from django.urls import path
from redactor.views import redactor_upload
from redactor.forms import FileForm, ImageForm


urlpatterns =[
    path('upload/image/<str:upload_to>', redactor_upload, {
        'form_class': ImageForm,
        'response': lambda name, url: '<img src="%s" alt="%s" />' % (url, name),
    }, name='redactor_upload_image'),

    path('upload/file/<str:upload_to>', redactor_upload,
        {
        'form_class': FileForm,
        'response': lambda name, url: '<a href="%s">%s</a>'.format(url, name)},
        name='redactor_upload_file'),
]
