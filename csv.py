import json                                                     
import os
from flask import Flask, request
from werkzeug import secure_filename
import panda as pd
import numpy as np

app = Flask(__name__)                                           
@app.route('/')    
def upload_file():
  uploaded_file = request.files['document']
  # data = json.load(request.files['data'])
  filename = secure_filename(uploaded_file.filename)
  uploaded_file.save(os.path.join('/', filename))
  return 'success'

@app.route('/')
def uploaded_file(i,k,filename):
    if(os.path.exists(filename)):
      myfile = send_from_directory('/',filename)
      myarr = pd.read_csv(filename ,skiprows = i, nrows = k).to_numpy()
      return myarr
    else:
      return 'FILE DOESNT EXIST'

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
