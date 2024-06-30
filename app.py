from flask import Flask, request, render_template
import tensorflow as tf
from utils import to_tingkat, to_yatidak, to_jenis

app = Flask(__name__)

model = tf.keras.models.load_model('HeartDataCNNModel.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict based on user inputs
    and render the result to the html page
    '''
    name,age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active = [x for x in request.form.values()]

    data = []

    data.append(int(age))
    data.append(int(gender))
    data.append(int(height))
    data.append(int(weight))
    data.append(int(ap_hi))
    data.append(int(ap_lo))
    data.append(int(cholesterol))
    data.append(int(gluc))
    data.append(int(smoke))
    data.append(int(alco))
    data.append(int(active))

    prediction = model.predict([data])

    prediction_text = 'Anda memiliki risiko tinggi penyakit jantung' if prediction[0][0] > 0.5 \
        else 'Anda memiliki risiko rendah penyakit jantung'

    return render_template(
        'index.html',
        prediction=prediction[0][0],
        prediction_text=prediction_text,
        name=name,
        age=age,
        gender=to_jenis(gender),
        height=height,
        weight=weight,
        ap_hi=ap_hi,
        ap_lo=ap_lo,
        cholesterol=to_tingkat(cholesterol),
        gluc=to_tingkat(gluc),
        smoke=to_yatidak(smoke),
        alco=to_yatidak(alco),
        active=to_yatidak(active)
    )


if __name__ == '__main__':
    app.run(debug=True)