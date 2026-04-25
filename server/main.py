import os
from pathlib import Path
from typing import List
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from twilio.rest import Client

from .models import (
    Incident, Volunteer, RiskArea, ClassificationRequest, ClassificationResponse,
    IncidentCreateRequest, IncidentCreateResponse, NotifyRequest, NotifyResponse,
    VolunteerCreateRequest, VolunteerCreateResponse, ImageAnalysisRequest, ImageAnalysisResponse
)
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
    # Adicionado suporte a termos em português
    is_critical = any(word in desc_lower for word in ["landslide", "collapse", "deslizamento", "desabar", "soterramento"])
    is_moderate = any(word in desc_lower for word in ["erosion", "crack", "erosão", "rachadura", "fenda"])

    if is_critical:
        return ClassificationResponse(
            severity="critical",
            required_skills=["search_and_rescue", "first_aid", "structural_engineering"]
        )
    elif is_moderate:
        return ClassificationResponse(
            severity="moderate",
            required_skills=["structural_engineering", "gis_mapping"]
        )
    
    return ClassificationResponse(
        severity="low",
        required_skills=["gis_mapping"]
    )


@app.post("/incidents", response_model=IncidentCreateResponse)
def create_incident(request: IncidentCreateRequest):
    incident = data_service.create_incident(request)
    return IncidentCreateResponse(
        incident_id=incident.id,
        status="success"
    )


@app.post("/volunteers/notify", response_model=NotifyResponse)
def notify_volunteers(request: NotifyRequest):
    incident = data_service.get_incident_by_id(request.incident_id)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    volunteers_to_notify = []
    for identifier in request.volunteer_ids:
        found = False
        for v in data_service.get_all_volunteers():
            if v.id == identifier or v.name.lower() == identifier.lower():
                volunteers_to_notify.append(v)
                found = True
                break
        if not found:
            print(f"Aviso: Voluntário '{identifier}' não encontrado.")

    if not volunteers_to_notify:
        raise HTTPException(status_code=404, detail="No valid volunteers found")

    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_WHATSAPP_NUMBER")

    if not account_sid or not auth_token or not from_number:
        # Debug log
        missing = []
        if not account_sid: missing.append("TWILIO_ACCOUNT_SID")
        if not auth_token: missing.append("TWILIO_AUTH_TOKEN")
        if not from_number: missing.append("TWILIO_WHATSAPP_NUMBER")
        print(f"ERRO: Credenciais do Twilio incompletas no .env: {', '.join(missing)}")
        
        # Modo mock se não tiver credenciais
        return NotifyResponse(status="mock_success_missing_credentials", notified_count=len(volunteers_to_notify))

    client = Client(account_sid, auth_token)
    
    count = 0
    for v in volunteers_to_notify:
        msg_body = request.message_override or f"🚨 ALERTA DEFESA CIVIL 🚨\nOlá {v.name}, precisamos da sua ajuda para um incidente: {incident.title}\nLocal: {incident.location.address}\nPor favor, responda se estiver disponível."
        
        # Limpar telefone para formato E.164 (simplificado)
        # O telefone no JSON deve estar como +5511999999999
        to_phone = f"whatsapp:{v.phone}" if not v.phone.startswith("whatsapp:") else v.phone
        
        try:
            client.messages.create(
                body=msg_body,
                from_=from_number,
                to=to_phone
            )
            count += 1
        except Exception as e:
            print(f"Erro ao enviar para {v.name}: {e}")

    return NotifyResponse(
        status="success",
        notified_count=count
    )

@app.post("/volunteers", response_model=VolunteerCreateResponse)
def create_volunteer(request: VolunteerCreateRequest):
    volunteer = data_service.create_volunteer(request)
    return VolunteerCreateResponse(
        volunteer_id=volunteer.id,
        status="success"
    )

@app.post("/analyze-risk", response_model=ImageAnalysisResponse)
def analyze_risk(request: ImageAnalysisRequest):
    # Mock de análise de visão computacional
    url = request.image_url.lower()
    
    if "crack" in url or "rachadura" in url or "fenda" in url:
        return ImageAnalysisResponse(
            risk_level="high",
            confidence_score=0.89,
            detected_issues=["Structural cracks", "Wall instability"],
            technical_recommendation="Evacuar área imediatamente e acionar engenharia estrutural.",
            status="success"
        )
    elif "landslide" in url or "deslizamento" in url:
        return ImageAnalysisResponse(
            risk_level="critical",
            confidence_score=0.95,
            detected_issues=["Soil movement", "Slope instability"],
            technical_recommendation="Risco iminente de soterramento. Isolamento total do perímetro.",
            status="success"
        )
    else:
        return ImageAnalysisResponse(
            risk_level="low",
            confidence_score=0.75,
            detected_issues=["Minor erosion or no issues detected"],
            technical_recommendation="Monitorar em caso de chuva forte. Não há risco imediato.",
            status="success"
        )
