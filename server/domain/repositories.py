from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Incident, Volunteer, RiskArea

class IIncidentRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Incident]:
        pass

    @abstractmethod
    def get_by_id(self, incident_id: str) -> Optional[Incident]:
        pass

    @abstractmethod
    def save(self, incident: Incident) -> Incident:
        pass

class IVolunteerRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Volunteer]:
        pass

    @abstractmethod
    def get_by_id(self, volunteer_id: str) -> Optional[Volunteer]:
        pass

    @abstractmethod
    def save(self, volunteer: Volunteer) -> Volunteer:
        pass

class IRiskAreaRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[RiskArea]:
        pass
