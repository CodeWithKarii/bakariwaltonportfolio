from flask import Flask, render_template, request 




app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():

    if request.method == 'POST':
        # Get the data from the POST request
        name= request.form['name']
        email = request.form['email']
        # print(name)
        # print(email)
    return  render_template('index.html')


@app.route("/roll")
def roll():
    return  render_template('roll.html')


@app.route("/chatbook")
def chatbook():
    return  render_template('chat.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
