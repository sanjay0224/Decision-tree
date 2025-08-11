from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('day_predictor.pkl', 'rb') as f:
    model, weekday_map = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            day = int(request.form['day'])
            month = int(request.form['month'])
            year = int(request.form['year'])

            prediction = model.predict([[day, month, year]])[0]
            result = weekday_map[prediction]

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
