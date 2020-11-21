import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.chatbot import bot


@api_view(["GET"])
def chat_view(request):
    input_data = json.loads(request.body.decode("utf-8"))
    if "text" not in input_data:
        return Response(
            {"text": ['The attribute "text" is required.']}, status=400
        )
    response = bot.get_response(input_data)
    return Response(response.serialize(), status=status.HTTP_200_OK)
