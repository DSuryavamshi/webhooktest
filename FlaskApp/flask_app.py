from flask import Flask, request
import subprocess
import json

app = Flask(__name__)
FILENAME = "flask_app.py"
@app.route('/webhook',methods=['POST'])
def webhook():
   data = json.loads(request.data)
   print("New commit by: {}".format(data['commits'][0]['author']['name']))
   if data["added"]:
      if FILENAME in data["added"]:
         resp = subprocess.Popen(["echo flask file updated"], stdout=subprocess.PIPE)
         output = resp.communicate()[0]
         print(output.decode("utf-8"))

   return "OK"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)