from app import app

@app.route('/')
@app.route('/coba', methods=['GET'])
def home():
    return "<h1>Hai</h1><p>test aja</p>"

# @app.route('/test', methods=['GET'])

app.run()