
import numpy as np
#need to 'conda install flask' for this to work
from flask import Flask, abort, jsonify, request
import pickle as cpickle


predictions = cpickle.load(open("predictions.pkl", "rb"))

app = Flask(__name__)

@app.route('/predictions', methods=['POST'])
def make_predict():
    #all kinds of error checking should go here
    data = request.get_json(force=True)
    #convert our json to a numpy array
    predict_request = str(data['user_id'])
    
    print(predict_request)
    #predict_request = np.array(predict_request).reshape(1,-1)
    #np array goes into random forest, prediction comes out
    print(predictions)
    ypred = predictions[predictions.user_id == predict_request]['class']#predictions.iloc[predict_request,0]
    print(int(ypred))
    #ypred = ypred.to_numeric()
    #return our prediction
    output = {'class': int(ypred)}
    #print(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(port = 9000, debug = True)


