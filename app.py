from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def index():
    """Return Homepage of Form"""
    prompts = silly_story.prompts
    return render_template("questions.html", prompts=prompts)

# Display results on screen


@app.get('/results')
def generate_story():
    """Takes input from questions & returns the story"""
    inputs = request.args
    story_string = silly_story.generate(inputs)
    return render_template("results.html", story_string=story_string)
