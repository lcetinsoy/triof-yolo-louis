import io
from operator import truediv
import os
import json
from tabnanny import verbose
from PIL import Image
import sys

import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "a_secret_key"

RESULT_FOLDER = os.path.join('static')
app.config['RESULT_FOLDER'] = RESULT_FOLDER

def find_model_name():
    for f in os.listdir():
        if f.endswith(".pt"):
            return f
    
    sys.exit("Je n'ai pas trouvé de modèle dans le dossier !")

    
model_name = find_model_name()
model = torch.hub.load("WongKinYiu/yolov7", 'custom', model_name, verbose=False)
model.eval()

def get_prediction(model, img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]  
    results = model(imgs, size=320)
    return results

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files.get('file')
        
        img_bytes = file.read()
        results = get_prediction(model, img_bytes)
        results.save(save_dir='static')
        filename = 'image0.jpg'
        
        return render_template('result.html', result_image=filename, model_name=model_name)

    return render_template('index.html')



#on lance le serveur pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True)
