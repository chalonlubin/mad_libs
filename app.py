from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/questions")
def show_question_form():
    prompts = silly_story.prompts
    return render_template("questions.html", questions=prompts)

@app.get("/results")
def view_results():
    answers = request.args
    story = silly_story.generate(answers)
    return render_template("results.html", story=story)


