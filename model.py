!pip install plotly
!pip install kaggle
from flask import  Flask,redirect,url_for,render_template,request,session
import os
import zipfile
import pandas as pd
import json
import plotly
import time
import numpy as np
from sklearn.linear_model import LinearRegression
from pymongo import MongoClient
import pickle
import kaggle
from pymongo import MongoClient

os.environ['KAGGLE_USERNAME'] = "avisaini"
os.environ['KAGGLE_KEY'] = "84bfd631fb4b1507f1a36687022e8fff"
!kaggle datasets download -d harlfoxem/housesalesprediction

zf = zipfile.ZipFile('housesalesprediction.zip')
df = pd.read_csv(zf.open('kc_house_data.csv'))
client = MongoClient("mongodb+srv://dbavisaini:dbqwertyuiop@cluster0-82quo.mongodb.net/test?retryWrites=true&w=majority")
collection=client["test"]
db = collection["final"]
db.drop()
records_ = df.to_dict(orient = "records")
result = db.insert_many(records_)
x=db.count_documents({})
print("number of records",x)
headData = db.find()
row_list = []
for i in headData:
    row_list.append(i)
    
df1=df.copy()

X = df1[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','sqft_above','sqft_basement','sqft_living15','sqft_lot15']]
y = df1[['price']]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X,y)
pickle.dump(regressor,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[4, 2, 5000,1500,1,1000,4000,1000,1100]]))