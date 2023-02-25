import nlpcloud
import PyPDF2
from wordcloud import WordCloud
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

api_key = "211ced6886270c25c3a91ec5277aa320f755ea61"
#api_key = "7edefa0cd0d99468cc9d64a4cea93e0cd3490963"
# api_key = "b63ca4df943496fe98ef208580041f78a3667554"

def file_to_string(file):
  
    with open(file,'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        content = ""
        for page_num in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page_num]
            content += (page_obj.extract_text(0))[500:1500]
        print(content)
        return content
        
text= file_to_string("./testpdf3.pdf")

def imageResponse(api_key):
    client= nlpcloud.Client("stable-diffusion", api_key, gpu=True, lang="en")
    link = client.image_generation("""lions roller skating""")
    print(link)

def sentimentResponse(api_key,text):
    client = nlpcloud.Client("distilbert-base-uncased-finetuned-sst-2-english", api_key)
    sentiment_response = client.sentiment(text)
    # sentiment_response = {
    #     "scored_labels":[
    #         {
    #         "label":"POSITIVE",
    #         "score":0.9996881484985352
    #         }
    #     ]
    #     }

    labels = ["+ve", "-ve"]
    sizes = [sentiment_response.get("scored_labels")[0].get("score"), 1-sentiment_response.get("scored_labels")[0].get("score")]
    colors = ["green", "red"]
    # Create pie chart 
    fig = plt.figure(figsize=(2,2))
    ax = fig.add_axes([0,0,1,1])
    ax.axis('equal')
    ax.pie(sizes, labels = labels, colors = colors,autopct='%1.2f%%', labeldistance=0.9, pctdistance=0.4)
    plt.savefig('pie_chart.png')



def keywordsResponse(api_key,text):
    client = nlpcloud.Client("fast-gpt-j", api_key, True)
    response_json = client.kw_kp_extraction(text)
    # Extract key phrases from response
    key_phrases = [kp for kp in response_json["keywords_and_keyphrases"]]
    return key_phrases

def summarizationResponse(api_key,text):
    client = nlpcloud.Client("bart-large-cnn", api_key,gpu = True)
    response = client.summarization(text)
    return response.get('summary_text')

def blogPostResponse(api_key):
    text = file_to_string("./testpdf3.pdf")
    client = nlpcloud.Client("fast-gpt-j", api_key, True)
    # Returns a json object.
    summary = summarizationResponse(api_key).get('summary_text')
    lengthSummary = len(summary.split(" "))
    if lengthSummary > 50:
        summary = (summary.split(" "))[0:49]
    print(client.article_generation(summary))


#### CALL THIS FUNCTION #######
def infographicCreation(summary):
    keywords = keywordsResponse(api_key, summary)
    # keywords = ["hi","test","bye"]
    # Create word cloud from key phrases
    wordcloud = WordCloud(width=500, height=250).generate(" ".join(keywords))
    wordcloudnp =  np.array(wordcloud)
    # Generate summary from function
    #summary = summarizationResponse(api_key, text)
    #summary =  "modus ponsrejfnsons joiesrno aogjra woa hrahwoj ouagwgnowr hogwno gjojarwo oajrgoiawj iajgijowr oj worija oirj igo aojgiomwr "

    # Create a blank image to serve as the infographic background
    infographic = Image.new("RGB", (800, 1200), (0, 0, 0))


    # Paste the word cloud and image onto the infographic
    # infographic.paste(img, (0, 0))
    sentimentResponse(api_key,summary)
    infographic.paste(Image.fromarray(wordcloudnp.astype('uint8')), (10, 150))
    pie_chart_img = Image.open('pie_chart.png')
    infographic.paste(pie_chart_img, (600, 150))

    # Add a text box to the infographic and write the summary text inside it
    draw = ImageDraw.Draw(infographic)
    text_font1 = ImageFont.truetype("./arial.ttf", size=36)
    text_font2 = ImageFont.truetype("./arial.ttf", size=24)

    # Define text boxes
    text_boxes = [ ((380, 50, 50, 50), "Generated Report", text_font1),
                  ((390, 120, 400, 100), "Keywords from article and sentiment analysis (left to right):", text_font2),
                ((380, 500, 1150, 750), "Summarised Article:", text_font2)]

    # Draw rectangles and text
    for box, text, font in text_boxes:
        draw.rectangle(box, fill=(0, 0, 0))
        x = box[0] + 10
        y = box[1] + 10
        w = box[2] 
        h = box[3] 
        draw.text((x, y, w, h), text, font=font, fill=(255, 255, 255), align="center", anchor="mm")

    # text_box1 = (350, 50, 50, 50)
    # draw.rectangle(text_box1, fill=(255, 255, 255))
    # text_box2 = (350, 50, 400, 100)
    # draw.rectangle(text_box2, fill=(255, 255, 255))

    text_box2 = (0, 600, 900, 2000)
    draw.rectangle(text_box2, fill=(255, 255, 255))

    # draw.text((text_box1[0]+10, text_box1[1]+10), "Generated Report", font=text_font1, fill=(0, 0, 0))
    # draw.text((text_box1[0]+10, text_box2[1]+10), "Key phrases from article:", font=text_font2, fill=(0, 0, 0))

    draw.text((text_box2[0], text_box2[1]), summary, font=text_font2, fill=(0, 0, 0))

    # Save the infographic as an image file
    infographic.save("infographic.jpg")

    # Display the infographic
    plt.imshow(infographic)
    plt.show()

# if __name__ == '__main__':
    
#     # sentimentResponse(api_key)
#     #summarizationResponse(api_key)
#     # summary="hi im just testing ! "
#     infographicCreation(summary=summary)