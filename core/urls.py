from django.urls import path

from bot.views import chat_view

app_name = "learn"
urlpatterns = [
    path(r"chat", chat_view, name="chat"),
]
