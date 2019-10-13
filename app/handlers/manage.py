def index():
    return 'Salam'


def register(app):
    app.add_url_rule('/', view_func=index, methods=['GET'])
