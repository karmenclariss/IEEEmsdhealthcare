from flask_cors import CORS
from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)
cors = CORS(app)

@app.route("/pdf", methods=['GET', 'POST'])
def pdf():
    if (request.method == "POST"):
        actualPDF = request.files['file']
        actualPDF.save('packagedPDF.pdf')
        # return message
    return jsonify({"Message": "This is a test message"})

if __name__ == '__main__':
    app.run()