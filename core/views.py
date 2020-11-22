import json

from bot.bot import shopping_assistant
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def chat_view(request):
    if "text" not in request.data:
        return Response(
            {"text": ['The attribute "text" is required.']}, status=400
        )
    response = shopping_assistant(request.data["text"])
    return Response({'response': response}, status=status.HTTP_200_OK)
