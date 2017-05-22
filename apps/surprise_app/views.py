from django.shortcuts import render, redirect
from django.contrib import messages
import re
import random

VALUES = ['one','two','three','four','five','six','seven','eight','nine','ten']
NUM_REGEX = re.compile('^[0-9]+$')

def index(request):
    return render(request, 'surprise_app/index.html')

def process(request):
    num = request.POST['num']
    num = str(num)

    if not NUM_REGEX.match(num):
        messages.info(request, 'Num must be integer')
        return redirect('/')
    elif int(num) > 10 or int(num) < 1:
        messages.info(request, 'Num must be from 1-10')
        return redirect('/')
    else:
        num = int(num)
        for i in range(num):
            randomIndex = random.randint(0,9)
            VALUES[i], VALUES[randomIndex] = VALUES[randomIndex], VALUES[i]
        request.session['num'] = num
        return redirect('/results')

def results(request):
    context = {
        'num': range(request.session['num']),
        'values': VALUES
    }
    return render(request, 'surprise_app/result.html', context)
