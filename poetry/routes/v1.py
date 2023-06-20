from django.contrib import admin
from django.urls import path

from poetry.controllers import PoemByStatusCodeController, PoemController

urlpatterns = [
    path('statuses/<int:status_code>/', PoemByStatusCodeController.as_view(), name='status_poem'),
    path('poems/<uuid:poem_id>/', PoemController.as_view(), name='status_poem'),
]