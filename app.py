from flask import Flask, render_template, redirect, request
from keras.models import load_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense
import ann_model




#app = Flask(__name__)
res=""
app=Flask(__name__,template_folder='template')
@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def marks():
    global res
    if request.method == 'POST':
        text_inputs = [request.form[f'input{i}'] for i in range(1, 9)]
        dropdowns = [request.form[f'dropdown{i}'] for i in range(1, 6)]
        print(text_inputs)
        res = ann_model.predict_input(float(text_inputs[0]), dropdowns[0], dropdowns[1], dropdowns[2],float(text_inputs[1]), float(text_inputs[2]), dropdowns[3], dropdowns[4], float(text_inputs[3]), float(text_inputs[4]), float(text_inputs[5]), float(text_inputs[6]), float(text_inputs[5])+50, float(text_inputs[7]))
        path = ""
        if(res >5):state ='Good'
        else: state ='Worst'
        result_dic ={
            'status' :state,
            'caption' :res,
            'audiopath': path
        }
    return render_template("index.html", result_c = result_dic)


if __name__ == '__main__':
    app.run(debug=True)
