from flask import render_template
from app import app

import random

ha=[]
hi=[]
icount=0
with open('js.txt','r', encoding='utf-8') as f:
    for i in f:
        if icount%2==0:
            a=i
        else:
            hi.append(a[:-1])
            hi.append(i[:-1])
            ha.append(hi)
            hi=[]
        icount=icount+1
    kil=len(ha)
                

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/mp3')
def audio():
    aud=[]
    ho={}
    for i in range(3):
        j =random.randint(-1,kil)
        ho['mp3']=ha[j][0]
        ho['text']=ha[j][1]
        ho['count']=i+1
        aud.append(ho)
        ho={}
    '''
    aud = [
        {
            'mp3': 'a heart of gold',
            'text': 'золоте серце',
            'count':'1'
        },
        {
            'mp3': 'a storm of applause',
            'text': 'шквал оплескiв',
            'count':'2'
        },
        {
            'mp3': 'about',
            'text': 'про, бiля',
            'count':'3'
        }
    ]
    '''
    return render_template("audio.html", aud=aud)