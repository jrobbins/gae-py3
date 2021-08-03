from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    logging.info('In hello()  !')
    print('primative logging')
    return 'Hello World!'

@app.route('/crash')
def crash():
    """Cause an exception and see what happens."""
    print('watch out for the KeyError')
    print({1: 10}[2])
    return 'Farewell World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

