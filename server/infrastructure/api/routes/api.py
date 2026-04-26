from typing import List
from fastapi import APIRouter, HTTPException, Depends
from server.application.dtos.api_dtos import (
    ClassificationRequest, ClassificationResponse,
    IncidentCreateRequest, IncidentCreateResponse,
    NotifyRequest, NotifyResponse,
    VolunteerCreateRequest, VolunteerCreateResponse,
    ImageAnalysisRequest, ImageAnalysisResponse
)
from server.domain.entities import Incident, Volunteer, RiskArea
from server.infrastructure.database.repositories.json_repository import (
    JsonIncidentRepository, JsonVolunteerRepository, JsonRiskAreaRepository
)
from server.infrastructure.services.twilio_service import TwilioService
from server.application.use_cases.match_volunteers import MatchVolunteersUseCase
from server.application.use_cases.notify_volunteers import NotifyVolunteersUseCase
from server.application.use_cases.create_incident import CreateIncidentUseCase
from server.application.use_cases.classify_incident import ClassifyIncidentUseCase
from server.application.use_cases.analyze_image_risk import AnalyzeImageRiskUseCase
from server.application.use_cases.create_volunteer import CreateVolunteerUseCase
import os

router = APIRouter()

# Dependency Injection Setup
# api.py está em src/infrastructure/api/routes/ -> precisamos subir 4 níveis para chegar na raiz
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
DATA_DIR = os.path.join(BASE_DIR, "dados")

incident_repo = JsonIncidentRepository(DATA_DIR)
volunteer_repo = JsonVolunteerRepository(DATA_DIR)
risk_area_repo = JsonRiskAreaRepository(DATA_DIR)
twilio_service = TwilioService()

@router.get("/incidents", response_model=List[Incident])
def get_incidents():
    return incident_repo.get_all()

@router.get("/incidents/{incident_id}", response_model=Incident)
def get_incident(incident_id: str):
    incident = incident_repo.get_by_id(incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident

@router.get("/volunteers", response_model=List[Volunteer])
def get_volunteers():
    return volunteer_repo.get_all()

@router.get("/volunteers/match/{incident_id}", response_model=List[Volunteer])
def match_volunteers(incident_id: str):
    use_case = MatchVolunteersUseCase(incident_repo, volunteer_repo)
    return use_case.execute(incident_id)

@router.get("/risk-areas", response_model=List[RiskArea])
def get_risk_areas():
    return risk_area_repo.get_all()

@router.post("/incidents/classify", response_model=ClassificationResponse)
def classify_incident(request: ClassificationRequest):
    use_case = ClassifyIncidentUseCase()
    return use_case.execute(request)

@router.post("/incidents", response_model=IncidentCreateResponse)
def create_incident(request: IncidentCreateRequest):
    use_case = CreateIncidentUseCase(incident_repo)
    incident = use_case.execute(request)
    return IncidentCreateResponse(incident_id=incident.id, status="success")

@router.post("/volunteers/notify", response_model=NotifyResponse)
def notify_volunteers(request: NotifyRequest):
    use_case = NotifyVolunteersUseCase(incident_repo, volunteer_repo, twilio_service)
    try:
        return use_case.execute(request)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/volunteers", response_model=VolunteerCreateResponse)
def create_volunteer(request: VolunteerCreateRequest):
    use_case = CreateVolunteerUseCase(volunteer_repo)
    volunteer = use_case.execute(request)
    return VolunteerCreateResponse(volunteer_id=volunteer.id, status="success")

@router.post("/analyze-risk", response_model=ImageAnalysisResponse)
def analyze_risk(request: ImageAnalysisRequest):
    use_case = AnalyzeImageRiskUseCase()
    return use_case.execute(request)
