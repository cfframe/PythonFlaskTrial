from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!"


@app.route("/hello/<string:name>/")
def hello(name):
    # return render_template('test_template.html', name=name)
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. That's fine. It's not their journey to make sense of. Its yours.' -- Unknown"]
    random_number = randint(0, len(quotes) - 1)
    quote = quotes[random_number]

    # return render_template('test_template2.html', **locals())
    return render_template('test_template2.html', name = name, quote = quote)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)
