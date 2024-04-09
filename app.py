from flask import Flask, request, render_template_string
import os
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        user_input = request.form['command']
        try:
            output = subprocess.check_output(user_input, shell=True, text=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Command Execution Demo</title>
        </head>
        <body>
            <h2>OS Command Injection Demo</h2>
            <form method="POST">
                <label for="command">Enter your command:</label>
                <input type="text" id="command" name="command" />
                <input type="submit" value="Execute" />
            </form>
            <pre>{{output}}</pre>
        </body>
        </html>
    ''', output=output)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
