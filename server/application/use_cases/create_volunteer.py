from server.domain.repositories import IVolunteerRepository
from server.domain.entities import Volunteer, Location
from server.application.dtos.api_dtos import VolunteerCreateRequest

class CreateVolunteerUseCase:
    def __init__(self, volunteer_repo: IVolunteerRepository):
        self.volunteer_repo = volunteer_repo

    def execute(self, request: VolunteerCreateRequest) -> Volunteer:
        all_volunteers = self.volunteer_repo.get_all()
        new_id = str(len(all_volunteers) + 101)
        
        # Mapping neighborhoods to coords (from original data_service.py)
        coords = {
            "Jardim Amanda": (-22.871, -47.234),
            "Parque Hortolandia": (-22.842, -47.215),
            "Remanso Campineiro": (-22.858, -47.218),
            "Jardim Rosolem": (-22.863, -47.195),
            "Jardim Novo Angulo": (-22.835, -47.228)
        }
        lat, lng = coords.get(request.neighborhood, (-22.85, -47.22))
        
        volunteer = Volunteer(
            id=new_id,
            name=request.name,
            age=request.age,
            phone=request.phone,
            email=request.email,
            skills=request.skills,
            certifications=[],
            location=Location(
                lat=lat,
                lng=lng,
                neighborhood=request.neighborhood,
                city=request.city
            ),
            available=True,
            availability_hours="full_time",
            experience_years=1,
            past_deployments=0,
            languages=["pt"],
            transport="own_vehicle",
            notes="Cadastrado via Agente wxO."
        )
        
        return self.volunteer_repo.save(volunteer)
