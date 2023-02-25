from flask_cors import CORS
from flask import Flask, request, jsonify
import base64
import os
import processfile as pf
import nlpcloud_test as nlpt

app = Flask(__name__)
cors = CORS(app)

@app.route("/pdf", methods=['GET', 'POST'])
def pdf():
    if (request.method == "POST"):
        actualPDF = request.files['file']
        summary = pf.summarise(actualPDF)
        nlpt.infographicCreation(pf.split_lines(summary))
        return pf.string_to_file(summary)
        # summary_pdf.save('packagedPDF.pdf')
        # return message
    return jsonify({"Message": "This is a test message"})

if __name__ == '__main__':
    app.run()