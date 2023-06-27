from flask import Flask, render_template 
app = Flask(__name__)


@app.route ('/play', defaults={'x': 3, 'color':'blue'})
@app.route ('/play/<x>', defaults= {'color': 'blue'})
@app.route ('/play/<x>/<color>')
def nivel3(x, color):
    num_times = int(x)
    return render_template('index3.html', num_times=num_times, color=color)


if __name__=="__main__":
    app.run(debug=True)