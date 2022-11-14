from flask import Flask,render_template,request,url_for

app = Flask(__name__)

# @app.route('/')
# @app.route('/<name>')
# def hello(name):
#     return "Hi {}".format(name)


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=="POST":
        name = request.form.get('nm')
        print(name)
        return name
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)