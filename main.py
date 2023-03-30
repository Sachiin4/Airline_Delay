from flask import Flask,render_template,request
from app.utils import predictions
import CONFIG
app=Flask(__name__)
@app.route('/')
def start():
    return render_template("air.html")

@app.route('/predict',methods=["POST","GET"])
def predict_dep_delay():
    data=request.form
    print(data)
    pred_obj= predictions()
    predicted_delay=pred_obj.predict_dep_del(data)
    print(predicted_delay)

    return render_template("air.html",PREDICT_DELAY=predicted_delay)


if __name__ == "__main__":
    app.run(host=CONFIG.HOST_NAME,port=CONFIG.PORT_NUMBER,debug=True)