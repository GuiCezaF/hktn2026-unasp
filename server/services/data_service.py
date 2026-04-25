import json
import os
from typing import List, Optional
from ..models import Incident, Volunteer, RiskArea


class DataService:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.incidents: List[Incident] = []
        self.volunteers: List[Volunteer] = []
        self.risk_areas: List[RiskArea] = []
        self._load_data()

    def _load_data(self):
        incidents_path = os.path.join(self.data_dir, "incidentes_demo.json")
        if os.path.exists(incidents_path):
            with open(incidents_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.incidents = [Incident(**item) for item in data]

        volunteers_path = os.path.join(self.data_dir, "voluntarios.json")
        if os.path.exists(volunteers_path):
            with open(volunteers_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.volunteers = [Volunteer(**item) for item in data]

        risk_areas_path = os.path.join(self.data_dir, "areas_risco.json")
        if os.path.exists(risk_areas_path):
            with open(risk_areas_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.risk_areas = [RiskArea(**item) for item in data]

    def get_all_incidents(self) -> List[Incident]:
        return self.incidents

    def get_incident_by_id(self, incident_id: str) -> Optional[Incident]:
        for incident in self.incidents:
            if incident.id == incident_id:
                return incident
        return None

    def get_all_volunteers(self) -> List[Volunteer]:
        return self.volunteers

    def get_all_risk_areas(self) -> List[RiskArea]:
        return self.risk_areas

    def create_incident(self, request) -> Incident:
        new_id = f"inc-{len(self.incidents) + 1:03d}"
        
        now_str = "2026-04-25T14:30:00Z"
        location_obj = {
            "lat": -22.85,
            "lng": -47.22,
            "neighborhood": "Mock",
            "city": "Hortolandia",
            "address": request.location,
            "reference": ""
        }
        reporter_obj = {
            "name": "Agente wxO",
            "contact": "sistema"
        }
        
        incident_data = {
            "id": new_id,
            "title": f"Incidente Automático - {request.expected_severity}",
            "description": request.description,
            "location": location_obj,
            "reported_at": now_str,
            "reporter": reporter_obj,
            "expected_severity": request.expected_severity,
            "required_skills": request.required_skills,
            "affected_people": 0,
            "affected_buildings": 0,
            "weather_conditions": "unknown",
            "access_conditions": "unknown",
            "status": "open",
            "notes": "Criado via ferramenta do wxO."
        }
        incident = Incident(**incident_data)
        self.incidents.append(incident)
        
        # Persistência em JSON. Para evitar loops do uvicorn, comente isto 
        # se não usar a exclusão no --reload
        import json
        incidents_path = os.path.join(self.data_dir, "incidentes_demo.json")
        with open(incidents_path, "w", encoding="utf-8") as f:
            json.dump([i.model_dump() for i in self.incidents], f, indent=2, ensure_ascii=False)
            
        return incident
