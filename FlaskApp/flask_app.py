from flask import Flask, request
import subprocess
import json

app = Flask(__name__)
ROOTFOLDER = "FlaskApp"
FILENAME = f"{ROOTFOLDER}/flask_app.py"
@app.route('/webhook',methods=['POST'])
def webhook():
   data = json.loads(request.data)
   if data["ref"] == "refs/heads/master":
      print("New commit by: {}".format(data['commits'][0]['author']['name']))
      if data["commits"][0]["added"]:
         if FILENAME in data["commits"][0]["added"]:
            resp = subprocess.Popen(["echo ", '"flask file updated"'], shell=True, stdout=subprocess.PIPE)
            output = resp.communicate()[0]
            print(output.decode("utf-8"))
      elif data["commits"][0]["modified"]:
         if FILENAME in data["commits"][0]["modified"]:
            resp = subprocess.Popen(["echo ", '"flask file updated"'], shell=True, stdout=subprocess.PIPE)
            output = resp.communicate()[0]
            print(output.decode("utf-8"))
   return "OK"

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5000)