from app import app
from app.utl import build_db

if __name__ == '__main__':
    build_db()
    app.run(debug=True)
