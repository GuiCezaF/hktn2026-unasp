from server.application.dtos.api_dtos import ImageAnalysisRequest, ImageAnalysisResponse

class AnalyzeImageRiskUseCase:
    def execute(self, request: ImageAnalysisRequest) -> ImageAnalysisResponse:
        url = request.image_url.lower()
        
        # Mock analysis based on original main.py logic
        if "cenario_02" in url or "crack" in url or "rachadura" in url or "fenda" in url:
            return ImageAnalysisResponse(
                risk_level="high",
                confidence_score=0.89,
                detected_issues=["Structural cracks", "Wall instability"],
                technical_recommendation="Evacuar área imediatamente e acionar engenharia estrutural.",
                suggested_incident_title="Rachadura Estrutural Crítica Detectada via Imagem",
                suggested_incident_description="Análise de IA detectou rachaduras estruturais e instabilidade de parede.",
                status="success"
            )
        elif "cenario_01" in url or "landslide" in url or "deslizamento" in url:
            return ImageAnalysisResponse(
                risk_level="critical",
                confidence_score=0.95,
                detected_issues=["Soil movement", "Slope instability"],
                technical_recommendation="Risco iminente de soterramento. Isolamento total do perímetro.",
                suggested_incident_title="Deslizamento Iminente Detectado via Imagem",
                suggested_incident_description="Análise de IA detectou movimento de solo e instabilidade de encosta.",
                status="success"
            )
        
        return ImageAnalysisResponse(
            risk_level="low",
            confidence_score=0.75,
            detected_issues=["Minor erosion or no issues detected"],
            technical_recommendation="Monitorar em caso de chuva forte. Não há risco imediato.",
            status="success"
        )
