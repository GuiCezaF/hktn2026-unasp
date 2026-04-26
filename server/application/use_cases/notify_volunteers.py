from typing import List, Optional
from server.domain.repositories import IIncidentRepository, IVolunteerRepository
from server.infrastructure.services.twilio_service import TwilioService
from server.application.dtos.api_dtos import NotifyRequest, NotifyResponse

class NotifyVolunteersUseCase:
    def __init__(
        self, 
        incident_repo: IIncidentRepository, 
        volunteer_repo: IVolunteerRepository,
        notification_service: TwilioService
    ):
        self.incident_repo = incident_repo
        self.volunteer_repo = volunteer_repo
        self.notification_service = notification_service

    def execute(self, request: NotifyRequest) -> NotifyResponse:
        incident = self.incident_repo.get_by_id(request.incident_id)
        if not incident:
            raise ValueError("Incident not found")

        identifiers = [i.strip() for i in request.volunteer_names_or_ids.split(",") if i.strip()]
        all_volunteers = self.volunteer_repo.get_all()
        
        volunteers_to_notify = []
        for identifier in identifiers:
            for v in all_volunteers:
                name_match = v.name.lower() == identifier.lower() or identifier.lower() in v.name.lower()
                if v.id == identifier or name_match:
                    volunteers_to_notify.append(v)
                    break

        if not volunteers_to_notify:
            raise ValueError("No valid volunteers found")

        count = 0
        for v in volunteers_to_notify:
            msg_body = request.message_override or (
                f"CONVOCACAO VOLUNTARIA - CrisisCoordinator\n"
                f"Ola {v.name}, precisamos da sua ajuda voluntaria para um incidente: {incident.title}\n"
                f"Local: {incident.location.address}"
            )
            
            if self.notification_service.send_whatsapp(v.phone, msg_body):
                count += 1

        return NotifyResponse(
            status="success",
            notified_count=count
        )
