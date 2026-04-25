from typing import List, Optional
from pydantic import BaseModel


class Location(BaseModel):
    lat: float
    lng: float
    neighborhood: str
    city: str
    address: Optional[str] = None
    reference: Optional[str] = None


class Reporter(BaseModel):
    name: str
    contact: str


class Incident(BaseModel):
    id: str
    title: str
    description: str
    location: Location
    reported_at: str
    reporter: Reporter
    expected_severity: str
    required_skills: List[str]
    affected_people: int
    affected_buildings: int
    weather_conditions: str
    access_conditions: str
    status: str
    notes: Optional[str] = None


class Volunteer(BaseModel):
    id: str
    name: str
    age: int
    phone: str
    email: str
    skills: List[str]
    certifications: List[str]
    location: Location
    available: bool
    availability_hours: str
    experience_years: int
    past_deployments: int
    languages: List[str]
    transport: str
    notes: Optional[str] = None


class RiskHistoryEvent(BaseModel):
    date: str
    event: str
    severity: str


class RiskArea(BaseModel):
    id: str
    name: str
    location: Location
    risk_score: float
    risk_level: str
    slope_angle_degrees: int
    soil_type: str
    vegetation_cover_percent: int
    drainage_condition: str
    population_density: str
    buildings_in_area: int
    people_in_area: int
    history: List[RiskHistoryEvent]
    last_inspection: str
    recommended_actions: List[str]
    notes: Optional[str] = None


class ClassificationRequest(BaseModel):
    description: str


class ClassificationResponse(BaseModel):
    severity: str
    required_skills: List[str]
