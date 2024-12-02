from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            num3 = float(request.form['num3'])

            # Find the largest number
            result = max(num1, num2, num3)
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
