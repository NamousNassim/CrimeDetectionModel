from pydantic import BaseModel

class PredictRequest(BaseModel):
    Longitude: float
    latitude: float
    year: int

class PredictResponse(BaseModel):
    prediction: list