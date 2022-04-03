#5
from flask import Flask,jsonify,request

#6
from classifier import get_prediction

#7
app = Flask(__name__)

#8
@app.route("/predict-digit", methods=["POST"])

#9
def predict_data(): 
    #10
     image = request.files.get("digit") 
     prediction = get_prediction(image) 
     return jsonify({ "prediction": prediction }), 200