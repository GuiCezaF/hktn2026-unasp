from typing import List
from server.domain.repositories import IIncidentRepository, IVolunteerRepository
from server.domain.entities import Volunteer

# Slugs em inglês (ex.: wxO / OpenAPI) alinhados ao vocabulário de dados/voluntarios.json
_SKILL_ALIASES = {
    "search_and_rescue": "busca e resgate",
    "first_aid": "primeiros socorros",
    "structural_engineering": "engenharia estrutural",
    "logistics": "logística",
    "gis_mapping": "mapeamento gis",
    "drone_operator": "operador de drone",
    "psychological_support": "apoio psicológico",
    "communication": "comunicação",
}


def _canonical_skill(skill: str) -> str:
    key = skill.strip().lower()
    return _SKILL_ALIASES.get(key, key)


class MatchVolunteersUseCase:
    def __init__(self, incident_repo: IIncidentRepository, volunteer_repo: IVolunteerRepository):
        self.incident_repo = incident_repo
        self.volunteer_repo = volunteer_repo

    def execute(self, incident_id: str) -> List[Volunteer]:
        incident = self.incident_repo.get_by_id(incident_id)
        if not incident:
            return []

        required_skills = {_canonical_skill(s) for s in incident.required_skills}
        all_volunteers = self.volunteer_repo.get_all()
        matched_volunteers = []

        for volunteer in all_volunteers:
            if not volunteer.available:
                continue

            volunteer_skills = {_canonical_skill(s) for s in volunteer.skills}
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
