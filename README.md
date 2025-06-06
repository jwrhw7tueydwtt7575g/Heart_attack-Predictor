# Heart Attack Predictor

This is a machine learning-based web application built with **FastAPI** that predicts the risk of a heart attack based on user input data. The backend serves a pre-trained Random Forest classifier model for prediction.

## Features

- Fast and lightweight API built with FastAPI
- Predicts heart attack risk using a trained machine learning model
- Simple HTML frontend with form inputs to collect user health data
- Dockerized for easy deployment and portability
- Model persistence with a `.sav` file (pickle)

## Project Structure

app_folder/
│
├── main.py # FastAPI app with routes and prediction logic
├── trained-MODEL/
│ └── heart_attack_model.sav # Trained ML model saved with pickle
├── templates/
│ └── index.html # Frontend HTML form for user input
├── Dockerfile # Docker configuration for containerizing the app
├── requirements.txt # Python dependencies
└── README.md # This file

markdown
Copy
Edit

## Installation & Usage

### Prerequisites

- Python 3.7+
- Docker (optional but recommended)

### Running Locally

1. Clone the repository:
git clone https://github.com/jwrhw7tueydwtt7575g/Heart_attack-Predictor.git
cd Heart_attack-Predictor/app_folder

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

3. Run the FastAPI server:
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

markdown
Copy
Edit

4. Open your browser at `http://localhost:8000`

### Running with Docker

1. Build the Docker image:
docker build -t fastapi-heart .

markdown
Copy
Edit

2. Run the container:
docker run -d -p 8000:8000 --name fastapi-heart-container fastapi-heart

pgsql
Copy
Edit

3. Access the app at `http://localhost:8000`

## Model

The model used is a **Random Forest Classifier** trained on heart attack prediction data and serialized with Python’s `pickle` module.

## Notes

- Make sure the model file path in `main.py` matches the location of the saved model.
- The app uses Jinja2 templates for the HTML frontend.
- The Dockerfile installs all necessary dependencies and copies the model and code into the container.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is open source and available under the MIT License.

---

If you want me to generate the actual markdown file for you or help add badges, just ask!







