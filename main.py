from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import pickle

app = FastAPI(title="Heart Attack Prediction API with UI")

templates = Jinja2Templates(directory="templates")

# Load model once
model_path = "trained-MODEL/heart_attack_model.pkl"
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request,
            age: int = Form(...),
            sex: int = Form(...),
            chest_pain: int = Form(...),
            resting_bp: int = Form(...),
            cholesterol: int = Form(...),
            fasting_blood_sugar: int = Form(...),
            resting_ecg: int = Form(...),
            max_heart_rate: int = Form(...),
            exercise_angina: int = Form(...),
            oldpeak: float = Form(...),
            st_slope: int = Form(...)):
    
    input_array = np.array([[age, sex, chest_pain, resting_bp,
                             cholesterol, fasting_blood_sugar, resting_ecg,
                             max_heart_rate, exercise_angina, oldpeak, st_slope]])
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        result = "Heart Attack Detected! Immediate attention is required."
        status = "danger"
    else:
        result = "No Heart Attack! Continue monitoring health."
        status = "success"

    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result,
        "status": status
    })

