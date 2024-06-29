from flask import Flask, request, render_template
import pickle
from utils import switch
import random

app = Flask(__name__)

model_file = open('DTRModel.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', output='')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict based on user inputs
    and render the result to the html page
    '''
    nama,jeniskelamin,jeniskendaraan,jenistransmisi,tahunkendaraan,merekkendaraan,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10 = [x for x in request.form.values()]

    data = []

    ret, Q1 = switch(Q1)
    data.append(ret)

    ret, Q2 = switch(Q2)
    data.append(ret)

    ret, Q3 = switch(Q3)
    data.append(ret)

    ret, Q4 = switch(Q4)
    data.append(ret)

    ret, Q5 = switch(Q5)
    data.append(ret)

    ret, Q6 = switch(Q6)
    data.append(ret)

    ret, Q7 = switch(Q7)
    data.append(ret)

    ret, Q8 = switch(Q8)
    data.append(ret)

    ret, Q9 = switch(Q9)
    data.append(ret)

    ret, Q10 = switch(Q10)
    data.append(ret)

    prediction = model.predict([data])

    if prediction == 1:
      output='Sangat Tidak Puas'
    elif prediction == 2:
      output='Tidak Puas'
    elif prediction == 3:
      output='Agak Tidak Puas'
    elif prediction == 4:
      output='Netral'
    elif prediction == 5:
      output='Agak Puas'  
    elif prediction == 6:
      output='Puas' 
    elif prediction == 7:
      output='Sangat Puas'                  
    else:
        output='Tidak Terprediksi'

    return render_template('index.html', 
        output=output,
        nama=nama,
        jeniskelamin=jeniskelamin,
        jeniskendaraan=jeniskendaraan,
        jenistransmisi=jenistransmisi,
        tahunkendaraan=tahunkendaraan,
        merekkendaraan=merekkendaraan,
        Q1=Q1,
        Q2=Q2,
        Q3=Q3,
        Q4=Q4,
        Q5=Q5,
        Q6=Q6,
        Q7=Q7,
        Q8=Q8,
        Q9=Q9,
        Q10=Q10
    )


if __name__ == '__main__':
    app.run(debug=True)