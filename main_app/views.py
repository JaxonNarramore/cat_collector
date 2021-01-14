from django.shortcuts import render
from .models import Cat


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# cats = [
#     Cat('Stella', 'tuxedo', 'demon kitty', 1),
#     Cat('Piper', 'simese', 'angel kitty', 1.5),
#     Cat('bella', 'calico', 'mama kittys kitten', 0)
# ]


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})
