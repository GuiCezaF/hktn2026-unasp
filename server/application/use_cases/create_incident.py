from server.domain.repositories import IIncidentRepository
from server.domain.entities import Incident, Location, Reporter
from server.application.dtos.api_dtos import IncidentCreateRequest

class CreateIncidentUseCase:
    def __init__(self, incident_repo: IIncidentRepository):
        self.incident_repo = incident_repo

    def execute(self, request: IncidentCreateRequest) -> Incident:
        all_incidents = self.incident_repo.get_all()
        new_id = f"inc-{len(all_incidents) + 1:03d}"
        
        now_str = "2026-04-25T14:30:00Z" # Mocked date
        
        location = Location(
            lat=-22.85,
            lng=-47.22,
            neighborhood="Mock",
            city="Hortolandia",
            address=request.location,
            reference=""
        )
        
        reporter = Reporter(
            name="Agente wxO",
            contact="sistema"
        )
        
        incident = Incident(
            id=new_id,
            title=f"ALERTA DE EMERGÊNCIA: {request.location} - Nível {request.expected_severity.upper()}",
            description=request.description,
            location=location,
            reported_at=now_str,
            reporter=reporter,
            expected_severity=request.expected_severity,
            required_skills=request.required_skills,
            affected_people=request.affected_people,
            affected_buildings=request.affected_buildings,
            weather_conditions="unknown",
            access_conditions="unknown",
            status="open",
            notes="Criado via ferramenta do wxO."
        )
        
        return self.incident_repo.save(incident)
