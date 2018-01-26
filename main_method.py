from flask import json
from flask import request
from flask import Flask, Response
from flask_cors import CORS

import extractor2
 
app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['GET','POST'])
def foo():
    data = request.form.to_dict()
    print(data['value'])
    return (extractor2.url(data['value'])) 
    
    #dictionary = request.json
    #temp_arr = request.form
    #print(temp_arr)
    #print (request.json['key'])
    #return json.dumps(request.json)
    #print(request.form)
    #print ( request.form[0][1])
    #print(request.form['key'])
    #return json.dumps(extractor2.url(request.form[0][1]))
 
 
if __name__ == '__main__':
    app.run(debug=True)
