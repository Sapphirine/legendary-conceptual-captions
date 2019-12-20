from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from . import forms
from model import decoder, image_encoder, get_vocab_dictionaries
from tensorflow.keras import models
import cv2
import numpy as np
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings


def hello(request):
    context = {}
    context['content'] = 'Hello world'
    return render(request, 'index.html', context)


def run_model(image_file):
    path = os.path.join(settings.BASE_DIR, 'uploaded_images', str(image_file))
    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(image_file.read()))
    img = cv2.imread(path)
    enc_img = image_encoder.encode_images(img)
    model = models.load_model(os.path.join(settings.BASE_DIR, 'model/model_data/weights_best.hdf5'))
    sentence = decoder.greedy_decoder(
        model,
        enc_img[0],
        get_vocab_dictionaries.get_word_dictionary(),
        get_vocab_dictionaries.get_id_dictionary(),
        40)
    data = dict()
    data['caption'] = sentence
    return data


@csrf_exempt
def predict(request):
    json_response = []
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("POST method")
            print(form.cleaned_data['image'])
            json_response = run_model(form.cleaned_data['image'])
            # json_response['image'] = form.cleaned_data['image']
            # json_response['caption'] = "Hello World 122"

    return JsonResponse(json_response)
