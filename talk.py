# -*- coding: utf-8 -*-
import urllib,urllib2
import json

def talk_to_chii(word,uid):
    word = word.encode('utf-8')
    key = "33101887353a60f377a49dfb59f6e280"
    data = urllib.urlencode({'key' : key,'info':word,'userid':'1'})
    api_url="http://www.tuling123.com/openapi/api?"+data
    print api_url,word
    resp = urllib2.urlopen(api_url)
    resp = resp.read()
    resp = json.loads(resp)
    return resp['text']

