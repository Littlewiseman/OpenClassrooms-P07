import pickle
from flask import Flask, jsonify, request
import pandas as pd

filename = "C:/Users/BNP Leasing Solution/Documents/ProjetOC P07/final_model.sav"
data = pd.read_csv("C:/Users/BNP Leasing Solution/Documents/ProjetOC P07/dataset_norm_t.csv")
loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
#print(result)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<int:id_client>/')
def with_url_variables(id_client: int):
	#data[data["SK_ID_CURR"]==id_client]
	to_predict = data[data["SK_ID_CURR"]==id_client].drop("SK_ID_CURR", axis=1)
	score = loaded_model.predict(to_predict)
	return jsonify(message="My client score is " + str(score))
 
 
if __name__ == '__main__':
    app.run()