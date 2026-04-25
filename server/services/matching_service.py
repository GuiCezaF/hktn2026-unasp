from typing import List
from .data_service import DataService
from ..models import Volunteer


class MatchingService:
    def __init__(self, data_service: DataService):
        self.data_service = data_service

    def match_volunteers_for_incident(self, incident_id: str) -> List[Volunteer]:
        incident = self.data_service.get_incident_by_id(incident_id)
        if not incident:
            return []

        required_skills = set(incident.required_skills)
        all_volunteers = self.data_service.get_all_volunteers()
        matched_volunteers = []

        for volunteer in all_volunteers:
            if not volunteer.available:
                continue

            volunteer_skills = set(volunteer.skills)
            # Match if they have at least one required skill
            if required_skills.intersection(volunteer_skills):
                matched_volunteers.append(volunteer)

        return matched_volunteers
