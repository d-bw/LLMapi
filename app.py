from flask import Flask
import config
from controller.modelController import model_bp






app = Flask(__name__)

app.config.from_object(config)
app.register_blueprint(model_bp)




@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    #debug mode on
    app.run()
