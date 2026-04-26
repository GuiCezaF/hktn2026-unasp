import json
import os
from typing import List, Optional
from server.domain.entities import Incident, Volunteer, RiskArea
from server.domain.repositories import IIncidentRepository, IVolunteerRepository, IRiskAreaRepository

class JsonIncidentRepository(IIncidentRepository):
    def __init__(self, data_dir: str):
        self.file_path = os.path.join(data_dir, "incidentes_demo.json")
        self._incidents = self._load()

    def _load(self) -> List[Incident]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Incident(**item) for item in data]
        return []

    def get_all(self) -> List[Incident]:
        return self._incidents

    def get_by_id(self, incident_id: str) -> Optional[Incident]:
        return next((i for i in self._incidents if i.id == incident_id), None)

    def save(self, incident: Incident) -> Incident:
        # Check if updating or creating
        existing = self.get_by_id(incident.id)
        if existing:
            self._incidents = [i if i.id != incident.id else incident for i in self._incidents]
        else:
            self._incidents.append(incident)
        
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([i.model_dump() for i in self._incidents], f, indent=2, ensure_ascii=False)
        return incident

class JsonVolunteerRepository(IVolunteerRepository):
    def __init__(self, data_dir: str):
        self.file_path = os.path.join(data_dir, "voluntarios.json")
        self._volunteers = self._load()

    def _load(self) -> List[Volunteer]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Volunteer(**item) for item in data]
        return []

    def get_all(self) -> List[Volunteer]:
        return self._volunteers

    def get_by_id(self, volunteer_id: str) -> Optional[Volunteer]:
        return next((v for v in self._volunteers if v.id == volunteer_id), None)

    def save(self, volunteer: Volunteer) -> Volunteer:
        existing = self.get_by_id(volunteer.id)
        if existing:
            self._volunteers = [v if v.id != volunteer.id else volunteer for v in self._volunteers]
        else:
            self._volunteers.append(volunteer)
        
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([v.model_dump() for v in self._volunteers], f, indent=2, ensure_ascii=False)
        return volunteer

class JsonRiskAreaRepository(IRiskAreaRepository):
    def __init__(self, data_dir: str):
        self.file_path = os.path.join(data_dir, "areas_risco.json")
        self._risk_areas = self._load()

    def _load(self) -> List[RiskArea]:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [RiskArea(**item) for item in data]
        return []

    def get_all(self) -> List[RiskArea]:
        return self._risk_areas
