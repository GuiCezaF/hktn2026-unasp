# TODO List - Hackathon UNASP 2026

Baseado no arquivo `implementation_plan.md` e na análise dos arquivos já existentes no projeto, aqui está o que falta implementar:

## Marco 0: Enquadramento do Projeto
- [ ] **T0.1 - Documento de Visão e Alinhamento:** Criar o arquivo `docs/visao.md` conectando os 4 desafios listados na temática com as funcionalidades do sistema.
- [x] **T0.2 - Personas, Dados e Roteiros da Demo:** Arquivos criados (`dados/personas.json`, `dados/incidentes_demo.json`, `docs/demo-scripts.md`).

## Marco 1: Dados Mock e Servidor API
- [x] **T1.1 - Criar Arquivos de Dados Mock:** Arquivos na pasta `dados/` criados com sucesso.
- [x] **T1.2 - Servidor HTTP Mock (FastAPI):** Criar a estrutura do servidor na pasta `server/` (main.py, models.py, services/), configurar lógica de matching e subir a API.
- [x] **T1.3 - Specs OpenAPI YAML para as Tools:** Criar a pasta `wxo/tools/` e os respectivos arquivos de especificação YAML (incident_classifier.yaml, volunteer_matcher.yaml, geo_context.yaml).

## Marco 2: Núcleo watsonx Orchestrate
- [x] **T2.1 - Criar Agente Principal + Knowledge Base:** Agente `CrisisCoordinator` criado e Knowledge Base configurada.
- [ ] **T2.2 - Importar e Registrar Tools no wxO:** Importar os arquivos YAML no wxO para a toolset do agente principal.
- [ ] **T2.3 - Criar Agente Colaborador (Matcher de Voluntários):** Configurar o VolunteerMatcher no wxO e associar sua Tool, adicionando-o como colaborador do agente principal.
- [ ] **T2.4 - Testes de Fluxo Completo no wxO:** Testar todos os fluxos e documentar resultados em `docs/test-results.md`.

## Marco 3: Fluxos da Demo no WhatsApp
- [ ] **T3.1 - Fluxos e Roteiros da Demo no WhatsApp:** Validar a formatação de mensagens, tabelas e fallback no canal Twilio/WhatsApp do wxO.
- [ ] **T3.2 - Plano de Contingência:** Preparar ambiente de fallback no browser caso o WhatsApp falhe no momento da gravação.

## Marco 4: Entrega e Demo
- [ ] **T4.1 - README e Documentação Final:** Atualizar o README com arquitetura e problema. Criar `.gitignore` e `.env.example`.
- [ ] **T4.2 - Checklist Pré-Gravação:** Validar se a API mock está online, ferramentas wxO estão ativas e fluxos não têm falhas.
- [ ] **T4.3 - Gravação do Vídeo Demo:** Gravação do vídeo final seguindo o roteiro de 3 minutos.
