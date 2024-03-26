from flask import flask, render_template, request

app = flask (__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/html')
def houseinputs():
    return render_template ('html')

@app.route('/action', methods = ['POST', 'GET'])
def houseform():
    # data = list(request.form)
    # line

    # print(x)
    # line = request.form.get()
    # return render_template(html)

    if __name__ == '__main__':
        app.run(debug=True)