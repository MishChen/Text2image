#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import random
import jieba
import cgi
import webbrowser
import jieba.posseg as pseg
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from excute.models import Excuse
import html2text

def home(request):
  
  
  value = [
      "It was working in my head",
      "I thought I fixed that",
      "Actually, that is a feature",
      "It works on my machine",
  ]
  
  output = ""
    #{excuse}
    #""".format(excuse=random.choice(value))
    
  return render(request, "index.html", {'excuse1': output})
  #return HttpResponse(excuses[0])
def jiebaCut1(request):
  return render(request, "index.html", {'excuse1': "1"})
  
def jiebaCut(request):
    #webbrowser.open('http://umkkaea539e4.mish.koding.io/eyeinfo/eyeinfo.html', new=1, autoraise=False)
  form = cgi.FieldStorage()
  #textG = form['text'].value
  textG = request.GET['para']
  #textG = request.GET['para']
  textTurn = html2text.html2text(textG)
  #textTurn = html2text.html2text(textG).encode('utf-8')
  Excuse.objects.create(content=textTurn)
  #print textTurn
  #f = open("/home/mish/Web/B.txt", "w+")  
 # f.write( textTurn )
 #f.close()
  
  
  #f = file("/home/mish/Web/B.txt")  # 預設是 r
 # dataHTML = ''
 # while True :
  #   line = f.readline()
 #    if( len( line ) == 0 ) :
 #       break
  #   dataHTML += line
  #f.close()
 ############################################################## Excuse.objects.create(content=textG)
  
  #contentHTML = "<div>"+textG+"</div>"
  #textG = "我是映翎成功了嗎?"
  if textG is None:
    textG = "NONE..."

  #print textG
 #seg_list = jieba.cut(textTurn.decode('utf-8'), cut_all=False)
  #print seg_list
  #a = "/".join(seg_list).encode('utf-8')
  
  #words = pseg.cut(textTurn.decode('utf-8'))
  words = pseg.cut(textG.encode('utf-8'))
  output=""" """

  mylist=[]
  for w in words:
    #if( (cmp(w.flag,'n')>= 0)
    tag = cmp(w.flag,"n")
    if tag == 0:
      mylist.append(w.word.encode('utf-8'))
      
      #print mylist
   # output = '//'
      output = output + w.word + '//'
    #if(cmp(w.flag,'n')==0)
    if len(mylist)<=0:
      excuse1 = "No Recommend!!!"
    else:
      excuse1 = random.choice(mylist)
  
  
    #print randomOut
  
  #return render(request, "index.html", {'excuse': a})
  #return render_to_response('index.html', {'excuse': output},  RequestContext(request))
  return render_to_response('index.html', {'excuse': textTurn , 'excuse1': excuse1},  RequestContext(request))
  

  
def my_view(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response("index.html", c)
    
  
  
    
def profile(request):

  DBconList=Excuse.objects.all()
    
  # ... view code here
 # return {'DBcon': DBconList}   
  return render(request, "profile.html", {'DBcon': DBconList})
    #http://stackoverflow.com/questions/16595653/how-to-read-javascript-values-from-python-with-pyv8
    
def post(request):


  form = cgi.FieldStorage()
  #textG = form['text'].value
  textG = request.GET['para']
  textTurn = html2text.html2text(textG).encode('utf-8')
  
    
  # ... view code here
 # return {'DBcon': DBconList}   
  return render(request, "profile.html", {'DBcon': DBconList})