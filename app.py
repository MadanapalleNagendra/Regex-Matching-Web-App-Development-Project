from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', test_string=test_string, regex=regex_pattern, matches=matches)

@app.route('/validate-email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        # Regex for validating an email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = bool(re.match(email_regex, email))
        return render_template('validate_email.html', email=email, is_valid=is_valid)
    return render_template('validate_email.html')

if __name__ == '__main__':
    app.run(debug=True)