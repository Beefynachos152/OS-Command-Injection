from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        user_input = request.form['command']
        try:
            output = subprocess.check_output(user_input, shell=False, text=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Command Execution Demo</title>
            <style>
                body {
                    background-color: #121212;
                    color: #e0e0e0;
                    font-family: Arial, sans-serif;
                }
                h2 {
                    color: #bb86fc;
                }
                form {
                    margin: 20px 0;
                }
                label, input[type="text"], input[type="submit"] {
                    display: block;
                    margin: 10px 0;
                }
                input[type="text"] {
                    width: 300px;
                    padding: 8px;
                    background-color: #333;
                    border: 1px solid #333;
                    color: #e0e0e0;
                }
                input[type="submit"] {
                    padding: 8px 16px;
                    background-color: #3700b3;
                    color: #fff;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #6200ee;
                }
                pre {
                    background-color: #242424;
                    padding: 10px;
                    border: 1px solid #333;
                }
            </style>
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
