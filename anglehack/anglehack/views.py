"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from anglehack import app
import requests
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1



@app.route('/')
@app.route('/home')
def home():
  return """
        <html>
            <body>
                <h1>Transform a file demo</h1>

                <form action="/contact" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                  
                    
                    <input type="submit" />
                </form>
            </body>
        </html>
    """
    

@app.route('/contact',methods=["POST"])
def contact():
    audio_file = request.files['data_file']
    speech_to_text = SpeechToTextV1(
    username='fb6cf138-8ea6-4622-b599-42c7d3236269',
    password='zJeR3643oG5g',
    x_watson_learning_opt_out=False
    )

    #print(json.dumps(speech_to_text.models(), indent=2))

    #print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

   
    s = json.dumps(speech_to_text.recognize(
            audio_file, content_type='audio/wav', timestamps=True,
            speaker_labels=True,
            word_confidence=True),
            indent=2)
    return s

@app.route('/about')
def about():
    """Renders the about page."""
    return """lol"""
    
