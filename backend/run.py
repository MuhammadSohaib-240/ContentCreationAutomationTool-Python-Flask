from flask_cors import CORS
from app import create_app

app = create_app()
CORS(app, origins='http://localhost:5173')  # Replace with your ReactJS app's origin

if __name__ == "__main__":
    app.run(debug=True)
