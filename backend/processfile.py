import os

import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import openai
from flask import Flask, request

#app = Flask(__name__)
#openai.api_key_path = 'IEEEmsdhealthcare/backend/.env'
openai.api_key = ""

#@app.route("/", methods=("GET", "POST"))
def index():
    if True:
    #if request.method == "POST":
        article = file_to_string("/Users/nicholas/Desktop/IEEE_2023/sample_article.pdf")
        #article = file_to_string(request.files("aricle"))
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(article),
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text

def generate_prompt(article):
    return """Summarise this article such that it will be easy to understand and consume no less than 200 words. 
    The summary should not lose important details and data.
    The article: {}""".format(article)

def file_to_string(file):
    with open(file,'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        content = ""
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            content += page_obj.extract_text(0)

        return content

def string_to_file(string):
    pdf = canvas.Canvas("sample_output.pdf", pagesize=A4)
    pdf.setFont("Helvetica", 12)

    width, height = A4

    textobject = pdf.beginText()
    textobject.setTextOrigin(inch, height - inch)
    textobject.setWordSpace(0.2)
    textobject.setLeading(14)

    words = string.split()
    print(words)
    string = ' '.join([' '.join(words[i:i+10])+'\n' for i in range(0, len(words), 10)])
    print(string)
    lines = string.split('\n')
    if lines is not None:
        for line in lines:
            textobject.textLine(line)
    else:
        print("Error: Text could not be split into lines")

    pdf.drawText(textobject)
    pdf.save()
        
if __name__ == '__main__':
    result = index()
    string_to_file(result)
    print(result)