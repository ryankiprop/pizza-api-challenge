from server import create_app, db

app = create_app()

@app.route('/')
def home():
    return {'message': 'Pizza Restaurant API'}

if __name__ == '__main__':
    app.run(port=5555, debug=True)