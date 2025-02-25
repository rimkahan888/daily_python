from flask import Flask,request, render_template

app = Flask(__name__)

# what happens inside the app
# decorator
@app.route('/', methods=['GET', 'POST'])
def rootpage():
	# catching the name
	name = ''

	if request.method == 'POST' and 'name' in request.form:
		name = request.form.get('name')

	return render_template("index.html",
						name=name)

# initiate app
app.run(debug=True)

