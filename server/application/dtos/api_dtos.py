from typing import List, Optional
from pydantic import BaseModel

class ClassificationRequest(BaseModel):
    description: str

class ClassificationResponse(BaseModel):
    severity: str
    required_skills: List[str]

class IncidentCreateRequest(BaseModel):
    description: str
    location: str
    expected_severity: str
    required_skills: List[str]
    affected_people: Optional[int] = 0
    affected_buildings: Optional[int] = 0

class IncidentCreateResponse(BaseModel):
    incident_id: str
    status: str

class NotifyRequest(BaseModel):
    incident_id: str
    volunteer_names_or_ids: str
    message_override: Optional[str] = None

class NotifyResponse(BaseModel):
    status: str
    notified_count: int

class VolunteerCreateRequest(BaseModel):
    name: str
    age: int
    phone: str
    email: str
    skills: List[str]
    neighborhood: str
    city: str = "Hortolandia"

class VolunteerCreateResponse(BaseModel):
    volunteer_id: str
    status: str

class ImageAnalysisRequest(BaseModel):
    image_url: str

class ImageAnalysisResponse(BaseModel):
    risk_level: str
    confidence_score: float
    detected_issues: List[str]
    technical_recommendation: str
    suggested_incident_title: Optional[str] = None
    suggested_incident_description: Optional[str] = None
    status: str
