from app import create_app

if __name__ == '__main__':
    app, celery = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False)
