from django.urls import path

from core.views import chat_view

app_name = "core"
urlpatterns = [
    path(r"chat", chat_view, name="chat"),
]
