from flask import Flask, render_template
app = Flask(__name__) #create a Flask application instance

@app.route('/') #route decorator to define the URL route for the home page
def home():
#return a simple response when the home page is accessed
    # return "Hello, world! this is my first flask app"

#render the 'index.html' template when the home page is accessed
    return render_template('index.html')

@app.route('/about') #route decorator to define the URL route for the about page
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) #run the Flask application in debug mode