import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')

def home():
    return render_template('index.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_feature = [np.array(int_features)]
    prediction = model.predict(final_feature)
    output=round(prediction[0][0],2)
    return render_template('index.html', prediction_text='Amount of the property should be $ {}'.format(output))

    
if __name__=='__main__':
    app.run(debug=True, use_reloader=False)