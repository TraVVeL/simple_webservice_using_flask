from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>START PAGE</h1>
        <p><a href="/route?name=YourName&message=LetsBeFriend!">Simple url for...<a/></p>
    '''


@app.route('/route', methods=['GET', 'POST'])
def login():
    rules = ['No primary parameter', 'No secondary parameter']
    name = request.args.get('name')
    message = request.args.get('message')

    return f"{rules[0] if name is None or '' else 'Hello ' + name + '!'} " \
           f"{rules[1] if message is None else message + '!'}" \
           f"<p>You can easily change the reference names of " \
           f"<a href='/route?name=YourInput&message=LetsBeFriend!'>name</a> and " \
           f"<a href='/route?name=YourName&message=YourInput!'>message</a></p>"


@app.errorhandler(404)
def page_not_found(error):
    return 'Bad request'


if __name__ == '__main__':
    app.run(debug=True)
