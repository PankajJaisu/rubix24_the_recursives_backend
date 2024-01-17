from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.decorators import api_view
from django.http import JsonResponse
@api_view(['GET'])
def hello(request):
    return JsonResponse({"error": "Hello"}, status=500)


@api_view(['POST'])
def talk(request):
    response = requests.post('https://api.d-id.com/talks',
                            headers={"Authorization":"Basic d29yay5wYW5rYWoyMUBnbWFpbC5jb20:FsLKEM_qNKEgM9Rn2LY7J"},
                            json={
                            "script":{
                                "type":"text",
                                "input":"Hello I am Pankaj from The Recursives"
                            },
                            "source_url":"https://clips-presenters.d-id.com/alex/tv2VbI8lXI/MeDU8rVHxW/image.png"
                            })
    print(response.text)
    return JsonResponse({"response":"hello"})
