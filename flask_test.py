from flask import Flask
app =Flask(_name_)
@app.route("/")
def home():
    return '''
    <html>
    <head><title>This is my flask app</title></head>
    <body><h1>Hello from flask</h1>
    <h2>This is added from github</h2></body>
    </html>
    '''
if _name_ == "_main_":
    app.run(debug=True)
