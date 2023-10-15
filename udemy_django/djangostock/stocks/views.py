from django.shortcuts import render
# from django.http import HttpResponse
import requests
import json

token = 'pk_bcf05ba64dc2436dbae943b6a8f0ff5d'

def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get(f'https://api.iex.cloud/v1/data/core/quote/{ticker}?token=pk_bcf05ba64dc2436dbae943b6a8f0ff5d')
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ['']

    content = {'stock' : stock[0]}
    return render(request, 'stocks/home.html', content) 
    # stocks > template 가 아닌 이유 : django에서는 자동으로 templates를 먼저 조회하기 때문
    # template > stocks 처럼 app이름과 동일한 폴더를 넣은 이유는 한 프로젝트 내 여러 app을 생성할 수 있기 때문에, 혼선을 방지하기 위함
# pk_bcf05ba64dc2436dbae943b6a8f0ff5d