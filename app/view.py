from app import app



# {'/':'index', '/blog': 'index'}
@app.route('/')
@app.route('/blog')
def index():
    return '<h2>Hello World</h2>'

