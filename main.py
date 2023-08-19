from markets.skinport import getSkinportPrice
from markets.lootfarm import getLootFarmPrice
from markets.swap import getSwapPrice
from markets.buff import Buff
from flask import Flask, render_template, request
import pandas as pd
import json

with open("config.json", "r") as f:
    config = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = "nameSecret"

@app.route('/',methods=['GET','POST'])
def mainpage():
    skins = pd.read_csv('csv/csSkins.csv') # rustSkins.csv для раста
    results = []    
    error = ""
    if request.method == 'POST':
        skin = str(request.form.get('skinName'))
        if(skin):
            try:
                sp = getSkinportPrice(skin)
                buff = b.getBuffPrice(skin)
                lf = getLootFarmPrice(skin)
                sw = getSwapPrice(skin)
                afterFees = round((buff * 0.975),2) # С учётом комиссии Buff
                profit = round(afterFees - lf,2)
                gain = round((profit / lf) * 100,6)
                results = [skin, '$'+str(sp), '$'+str(buff), '$'+str(afterFees), '$'+str(profit), str(gain)+'%', '$'+str(lf), '$'+str(sw)]
            except:
                error = "Prices can't be found, try another skin"
        else:
            error = "Please enter a value"
    return render_template('index.html',skinNames=skins.skinNames.values.tolist(), results = results, error = error)

if(config["Cookies"] == ""):
    print("enter cookie in config.json")
else:
    b = Buff(config["Cookies"])
    app.run()

