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
- [x] **T2.2 - Importar e Registrar Tools no wxO:** Importar os arquivos YAML no wxO para a toolset do agente principal. ✅ 2026-04-25
- [x] **T2.3 - Criar Agente Colaborador (Matcher de Voluntários):** Configurar o VolunteerMatcher no wxO e associar sua Tool, adicionando-o como colaborador do agente principal. ✅ 2026-04-25
- [x] **T2.4 - Testes de Fluxo Completo no wxO:** Testar todos os fluxos e documentar resultados em `docs/test-results.md`. ✅ 2026-04-25
- [x] **T2.5 - Registro Automático de Incidente:** Criar tool `incident_registrar.yaml` e endpoint na API para evitar que o usuário digite o ID. ✅ 2026-04-25
## Marco 3: Fluxos da Demo no WhatsApp
- [x] **T3.1 - Fluxos e Roteiros da Demo no WhatsApp:** Validar a formatação de mensagens, tabelas e fallback no canal Twilio/WhatsApp do wxO. ✅ 2026-04-25
- [x] **T3.2 - Plano de Contingência:** Preparar ambiente de fallback no browser caso o WhatsApp falhe no momento da gravação. ✅ 2026-04-25
- [x] **T3.3 - Notificação Ativa de Voluntários via WhatsApp:** Criar tool `volunteer_notifier.yaml` e endpoint usando Twilio API para enviar o alerta aos celulares dos voluntários. ✅ 2026-04-25


## Marco 4: Funcionalidades Avançadas
- [x] **T5.1 - Cadastro Autônomo de Voluntários:** Criar endpoint `POST /volunteers` e tool para permitir que novos voluntários se cadastrem conversando com o Agente. ✅ 2026-04-25
- [ ] **T5.2 - Avaliação de Risco via Imagem:** Implementar tool que recebe uma URL de imagem (enviada pelo WhatsApp), utiliza uma IA de visão (ou mock estruturado) para identificar rachaduras ou deslizamentos e retorna uma recomendação técnica.
	- [ ] Falta testar

## Marco 5: Entrega e Demo
- [ ] **T4.1 - README e Documentação Final:** Atualizar o README com arquitetura e problema. Criar `.gitignore` e `.env.example`. (Em progresso: .gitignore e .env.example criados).
- [ ] **T4.2 - Checklist Pré-Gravação:** Validar se a API mock está online, ferramentas wxO estão ativas e fluxos não têm falhas. ✅ 2026-04-25 (Validados via Agente e WhatsApp).


## Marco 6: Entrega Final
- [ ] **T6.1 - Gravação do Vídeo Demo:** Gravação do vídeo final seguindo o roteiro de 3 minutos. (ÚLTIMO PASSO).

## Notas de Implementação (Pós-Testes)
- [x] Migração de todos os dados para a região de **Hortolândia - SP**.
- [x] Implementação de **Scoring e Ranking** de voluntários (Skill match + Proximidade).
- [x] Suporte a **termos em Português** para classificação de incidentes.
- [x] Robustez na busca de voluntários (suporte a IDs, nomes e limpeza de prefixos).
- [x] Otimização de **Instruções (System Prompt)** para evitar formatação indesejada no WhatsApp.
