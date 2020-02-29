from flask import Flask, render_template, request

app = Flask(__name__)

def responses():
   return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return request.form.get('value')

if __name__ == '__main__':
   app.run(debug = True)