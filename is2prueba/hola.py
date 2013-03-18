import flask
app = flask.Flask(__name__)

@app.route('/')
class View ():
    def hello_world(self):
        return 'Hello World!'

if __name__ == '__main__':
    app.run()
 
print "hola"