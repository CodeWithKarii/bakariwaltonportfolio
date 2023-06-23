from flask import Flask, render_template, request, url_for ,send_from_directory
from datetime import datetime 



app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    # get the current date and time
     post1 = datetime(2023, 6, 10, 12, 56, 54, 324893)
     post2 = datetime(2023, 6, 23, 12, 56, 54, 324893)
     date_element1 = post1.date()
     date_element2 = post2.date()


     if request.method == 'POST':
        # Get the data from the POST request
        name= request.form['name']
        email = request.form['email']
        # print(name)
        # print(email)
        return  render_template('index.html')
     return render_template('index.html' ,post1=date_element1, post2=date_element2)




@app.route("/roll")
def roll():
    return  render_template('roll.html')


@app.route("/chatbook")
def chatbook():
    return  render_template('chat.html')

# @app.route('/favicon.ico')
# def fav():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')



if __name__ == '__main__':
    # app.run()
    
    app.run(host='0.0.0.0', port=80)
