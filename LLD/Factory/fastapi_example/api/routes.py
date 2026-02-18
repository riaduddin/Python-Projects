from fastapi import Depends, FastAPI
from api.dependencies import get_report_service

app = FastAPI()

@app.get("/report")
def get_report(service = Depends(get_report_service)):
    return {"report": service.generate()}