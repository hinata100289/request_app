from django.shortcuts import render

from django.http import HttpResponse
import requests
import json

def index(request):

    return render(request, 'request/index.html')


def detail(request):

    # indem.htmlから送られてくるデータを取得
    nyuryoku1 = request.GET['location']
    # 取得したデータをAPIのURLにくっつける
    
    endpoint = "https://weather.tsukumijima.net/api/forecast"+"?city="+nyuryoku1
    
    # requests使ってAPIヲたたく
    response = requests.get(endpoint)
    print(response.text)
  
    # 辞書型に変換
    dic = response.json()
    # 必要なデータを取り出す
    

    context = {

    # 'dic': dic["date"],
    'dic': dic["forecasts"],
    }
    

    return render(request, 'request/detail.html', context)


