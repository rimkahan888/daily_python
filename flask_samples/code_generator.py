# app.py
from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        # Get form data
        length = int(request.form.get('length', 12))
        uppercase = 'uppercase' in request.form
        lowercase = 'lowercase' in request.form
        numbers = 'numbers' in request.form
        symbols = 'symbols' in request.form
            
        # Validate at least one option is selected
        if not any([uppercase, lowercase, numbers, symbols]):
            return render_template('index.html', error="Select at least one option")
        
        # Create character set
        characters = []
        if uppercase: characters.extend(string.ascii_uppercase)
        if lowercase: characters.extend(string.ascii_lowercase)
        if numbers: characters.extend(string.digits)
        if symbols: characters.extend(string.punctuation)
           
        # Generate secure password
        while True:
            password = ''.join(secrets.choice(characters) for _ in range(length))
            # Ensure meets security requirements (at least 3 types)
            has_upper = any(c.isupper() for c in password) if uppercase else True
            has_lower = any(c.islower() for c in password) if lowercase else True
            has_num = any(c.isdigit() for c in password) if numbers else True
            has_sym = any(c in string.punctuation for c in password) if symbols else True
            if has_upper and has_lower and has_num and has_sym:
                break

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
