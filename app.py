from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    """
    CreatedBy: Tincharlie
    :return: Render the templates which we have created to show the home.
    """
    return render_template('index.html', title='index')


@app.route("/contact")
def contact():
    """
    CreatedBy: Tincharlie
    :return: Render templates which we have created to show the contact html.
    """
    return render_template('contact.html', title='contact')


if __name__ == "__main__":
    app.run(debug=True)
