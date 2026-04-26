from server.application.dtos.api_dtos import ClassificationRequest, ClassificationResponse

class ClassifyIncidentUseCase:
    def execute(self, request: ClassificationRequest) -> ClassificationResponse:
        desc_lower = request.description.lower()
        
        # Logic based on knowledge_crisis_protocols.txt
        is_critical = any(word in desc_lower for word in [
            "landslide", "collapse", "deslizamento", "desabar", "soterramento", "trapped", "injured"
        ])
        is_moderate = any(word in desc_lower for word in [
            "erosion", "crack", "erosão", "rachadura", "fenda", "heavy rain", "chuva forte"
        ])

        if is_critical:
            return ClassificationResponse(
                severity="critical",
                required_skills=["busca e resgate", "primeiros socorros", "engenharia estrutural"]
            )
        elif is_moderate:
            return ClassificationResponse(
                severity="moderate",
                required_skills=["engenharia estrutural", "mapeamento gis", "operador de drone"]
            )
        
        return ClassificationResponse(
            severity="low",
            required_skills=["mapeamento gis", "logística"]
        )
