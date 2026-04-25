import os
from typing import List
from fastapi import FastAPI, HTTPException
from .models import Incident, Volunteer, RiskArea, ClassificationRequest, ClassificationResponse
from .services.data_service import DataService
from .services.matching_service import MatchingService

app = FastAPI(title="Incident Response Hub", version="1.0.0")

# Setup paths and services
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "dados")

data_service = DataService(DATA_DIR)
matching_service = MatchingService(data_service)

@app.get("/incidents", response_model=List[Incident])
def get_incidents():
    return data_service.get_all_incidents()

@app.get("/incidents/{incident_id}", response_model=Incident)
def get_incident(incident_id: str):
    incident = data_service.get_incident_by_id(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@app.get("/volunteers", response_model=List[Volunteer])
def get_volunteers():
    return data_service.get_all_volunteers()

@app.get("/volunteers/match/{incident_id}", response_model=List[Volunteer])
def match_volunteers(incident_id: str):
    incident = data_service.get_incident_by_id(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    return matching_service.match_volunteers_for_incident(incident_id)

@app.get("/risk-areas", response_model=List[RiskArea])
def get_risk_areas():
    return data_service.get_all_risk_areas()

@app.post("/incidents/classify", response_model=ClassificationResponse)
def classify_incident(request: ClassificationRequest):
    # Mock behavior: return a high severity if "landslide" or "collapse" is in description
    desc_lower = request.description.lower()
    if "landslide" in desc_lower or "collapse" in desc_lower:
        return ClassificationResponse(
            severity="critical",
            required_skills=["search_and_rescue", "first_aid", "structural_engineering"]
        )
    elif "erosion" in desc_lower or "crack" in desc_lower:
        return ClassificationResponse(
            severity="moderate",
            required_skills=["structural_engineering", "gis_mapping"]
        )
    
    return ClassificationResponse(
        severity="low",
        required_skills=["gis_mapping"]
    )
