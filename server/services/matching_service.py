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
            matching_skills = required_skills.intersection(volunteer_skills)
            
            if matching_skills:
                # Skill match ratio (weight 0.7)
                skill_score = len(matching_skills) / len(required_skills)
                
                # Proximity (weight 0.3) - Bonus if same neighborhood
                proximity_score = 1.0 if volunteer.location.neighborhood == incident.location.neighborhood else 0.5
                
                total_score = (skill_score * 0.7) + (proximity_score * 0.3)
                
                matched_volunteers.append({
                    "volunteer": volunteer,
                    "score": total_score
                })

        # Sort by score descending and return Volunteer objects
        matched_volunteers.sort(key=lambda x: x["score"], reverse=True)
        return [item["volunteer"] for item in matched_volunteers]
