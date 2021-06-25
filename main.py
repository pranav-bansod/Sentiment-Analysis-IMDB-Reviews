import os
from flask import Flask, request, render_template
import pickle





# routes
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    predict=request.form['text']
    file = open('word_vectorizer.pk', 'rb')
    vect = pickle.load(file)

    testing = [predict]
    testing1 = vect.transform(testing)

    file = open('svm.pk', 'rb')
    l = pickle.load(file)

    result = l.predict(testing1)
    if result==0:
        prediction="Sorry! It's a Negative Review!"
    else:
        prediction="Congrats! You've got a Positive Review! "
    print(result)


    return render_template('output.html', prediction_text=prediction)

@app.route('/contact')
def team():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)


