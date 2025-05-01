from fastapi import APIRouter, UploadFile, Form
from io import StringIO
import pandas as pd
from automl.trainer import train_model
from automl.predictor import predict

router = APIRouter()

@router.post("/automl/train")
async def train(file: UploadFile, target: str = Form(...)):
    df = pd.read_csv(StringIO((await file.read()).decode()))
    status = train_model(df, target)
    return {"status": status}

@router.post("/automl/predict")
async def make_prediction(file: UploadFile):
    df = pd.read_csv(StringIO((await file.read()).decode()))
    result = predict(df)
    return {"predictions": result}
