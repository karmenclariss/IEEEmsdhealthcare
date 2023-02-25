import nlpcloud

api_key = "b63ca4df943496fe98ef208580041f78a3667554"
client = nlpcloud.Client("stable-diffusion", api_key, gpu=True, lang="en")

print(client.image_generation("""an infographic"""))