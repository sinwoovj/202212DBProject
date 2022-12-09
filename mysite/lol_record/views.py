from django.shortcuts import render
import requests
# Create your views here.

from . import models

def api(request):
    api_key = 'RGAPI-30af8374-70a0-4da2-888d-1nfa55d0cfed9'
    sohwan = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" +'sinutella' +'?api_key=' + api_key #https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/hide%20on%20bush?api_key=RGAPI-30af8374-70a0-4da2-888d-1fa55d0cfed9
    r = requests.get(sohwan)
    r.json()['id']
    tier_url = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + r.json()['id'] +'?api_key=' + api_key
    r2  = requests.get(tier_url)
    r2.json()
