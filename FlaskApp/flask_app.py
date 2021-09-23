from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
   data = json.loads(request.data)
   print("New commit by: {}".format(data['commits'][0]['author']['name']))
   return "OK"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)