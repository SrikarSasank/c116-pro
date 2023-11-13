from flask import Flask , render_template

app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/1")
def home():

    name = "Alex" 
    age = "12" 

    return render_template('index.html', name = name, age = age)

@app.route("/2")
def a():

    name = "ABC" 
    age = "35" 

    return render_template('father.html', name = name, age = age)

@app.route("/3")
def b():

    name = "XYZ" 
    age = "12" 

    return render_template('friend.html', name = name, age = age)

@app.route("/4")
def c():

    name = "HIJ" 
    age = "33" 

    return render_template('mother.html', name = name, age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
