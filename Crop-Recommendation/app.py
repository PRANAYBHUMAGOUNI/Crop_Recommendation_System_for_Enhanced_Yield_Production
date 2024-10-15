import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
 
app = Flask(__name__)
model = pickle.load(open('classifier.pkl', 'rb'))

b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

a = ['Apple','Banana','blackgram','chickpea','coconut','coffee',
     'cotton','grapes','jute','kidney beans','lentil','maize','mango',
     'moth beans','mung bean','muskmelon','orange','papaya','pigeonpeas',
     'pomegranate','Rice','Watermelon']

a = pd.DataFrame(a,columns=['label'])
b = pd.DataFrame(b,columns=['encoded'])
classes = pd.concat([a,b],axis=1).sort_values('encoded').set_index('label')


@app.route('/')
def welcome():
    return render_template('crop_predict.html')

@app.route('/predict',methods=['POST'])
def predict():

    temp = request.form.get('Temperature')
    humid = request.form.get('Humidity')
    ph = request.form.get('PH')
    rain = request.form.get('rain_fall')
    n = request.form.get('n')
    p = request.form.get('p')
    k = request.form.get('k')
    data = [[n,p,k,temp,humid,ph,rain]]
    pred = model.predict(data)

    for i in range(0,len(classes)):
        if(classes.encoded[i]==pred):
            output = classes.index[i].upper()
    return render_template('crop_predict.html', prediction_text='Recomended Crop is {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

