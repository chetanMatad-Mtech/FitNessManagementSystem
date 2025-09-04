from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store registered members
members = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            members.append({'name': name, 'email': email})
            return redirect(url_for('list_members'))
        else:
            return render_template('register.html', error="Please Enter name and email.")

    return render_template('register.html')

@app.route('/members')
def list_members():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
