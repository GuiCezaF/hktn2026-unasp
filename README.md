# Coordenação de voluntariado em deslizamentos · Landslide crisis volunteer coordination

**Idiomas / Languages:** [Português (PT-BR)](#readme-pt) · [English (EN)](#readme-en)

---

<a id="readme-pt"></a>

## Português (Brasil)

PoC para o **Hackathon IA Descomplicada: Da Ideia à Implementação** (UNASP + IBM), no tema **Orquestrando o Voluntariado Inteligente para Situações de Crise**. O cenário trata de **deslizamentos de barranco / encosta**: apoio ao contexto de risco e **encaixe de voluntários por habilidades**, com **IBM watsonx Orchestrate** como camada de orquestração de agentes.

**Aviso:** dados geoespaciais e imagens neste repositório são **fictícios** e apenas para demonstração. Este software **não** substitui decisões de órgãos competentes, equipes de busca e salvamento ou pareceres técnicos oficiais.

### Estrutura do repositório

| Caminho | Função |
|---------|--------|
| `server/` | Backend **FastAPI**: incidentes, voluntários, áreas de risco, classificação, análise fictícia de imagem, notificações WhatsApp (Twilio). |
| `dados/` | JSONs mock e imagens de demo (servidos em `/dados/...` com a API no ar). |
| `wxo/` | Definições de tools/agentes e conhecimento de domínio para **watsonx Orchestrate**. |
| `docs/` | Materiais do evento, roteiros de demo e notas. |



### Arquitetura (MVP)

| Camada | Descrição |
|--------|-----------|
| **Orquestração** | Agente(s) no **watsonx Orchestrate** com instruções de domínio e **tools** (OpenAPI) chamando este backend para contexto geo mock e “análise” de imagem fictícia. |
| **Interface** | **Sem front-end web dedicado** — uso via **WhatsApp** (Twilio), **Telegram** (se integrado) e/ou **chat do wxO** com o agente principal. **`/docs`** e **`/redoc`** servem só para inspeção da API e testes manuais. |
| **Dados** | Arquivos JSON e imagens estáticas em `dados/`; identificadores de **habilidades** nos dados e na API estão em **inglês** (ex.: `search and rescue`, `first aid`) para alinhar com o código e com o material em `wxo/memory/`. |

### Pré-requisitos

- Acesso **IBM Cloud** ao **watsonx Orchestrate** (e opcionalmente watsonx.ai), conforme o edital.
- Para **Twilio WhatsApp**: SID, token e remetente aprovado (`TWILIO_WHATSAPP_NUMBER`). Documentação: [Twilio WhatsApp](https://www.twilio.com/docs/whatsapp).
- **Não** versionar segredos. Use `server/.env` (fora do Git) ou o cofre de segredos do seu ambiente.

### Como rodar

Na **raiz** do repositório (pasta pai de `server/` e `dados/`):

```bash
cd server
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

Opcional: copie `server/.env.example` para `server/.env` e preencha o Twilio. Sem credenciais, classificação, match e criação de incidentes seguem funcionando; o envio de WhatsApp é ignorado e `notified_count` pode ser `0`.

Suba o **uvicorn a partir da raiz** para os imports `server.*` e os caminhos para `dados/` funcionarem:

```bash
python -m uvicorn server.main:app --reload --host 127.0.0.1 --port 8000
```

- **Swagger:** http://127.0.0.1:8000/docs  
- **ReDoc:** http://127.0.0.1:8000/redoc  
- **Assets de demo:** http://127.0.0.1:8000/dados/imagens_demo/…  

#### Principais endpoints HTTP

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET` | `/incidents` | Lista incidentes |
| `GET` | `/incidents/{id}` | Detalhe de um incidente |
| `POST` | `/incidents` | Cria incidente (payload de tool) |
| `POST` | `/incidents/classify` | Severidade + habilidades a partir de texto (regras) |
| `GET` | `/volunteers` | Lista voluntários |
| `GET` | `/volunteers/match/{incident_id}` | Ordena voluntários por habilidades e bairro |
| `POST` | `/volunteers` | Cadastra voluntário |
| `POST` | `/volunteers/notify` | Notifica voluntários selecionados (Twilio se configurado) |
| `GET` | `/risk-areas` | Lista áreas de risco mock |
| `POST` | `/analyze-risk` | Risco mock por “dicas” na URL da imagem |

### watsonx Orchestrate

YAMLs de tools e conhecimento em `wxo/`. Aponte as **URLs do servidor** no wxO para sua base publicada ou túnel (ex.: ngrok). Ajuste `servers.url` em cada fragmento OpenAPI ao seu ambiente.

### Leitura adicional

- Materiais do evento / IBM: `docs/`  
- Roteiro passo a passo da demo: `docs/demo-scripts.md`  
- Planejamento: `plan.md`, `implementation_plan.md`  

### Licença

Veja [`LICENSE`](LICENSE).

*IBM, watsonx e watsonx Orchestrate são marcas da International Business Machines Corporation.* Este projeto não é um produto oficial da IBM.

---

<a id="readme-en"></a>

## English

Proof-of-concept for **Hackathon IA Descomplicada: Da Ideia à Implementação** (UNASP + IBM), theme **Orchestrating intelligent volunteering for crisis situations**. The scenario focuses on **slope / embankment landslides**: risk context support and **matching volunteers by skills**, with **IBM watsonx Orchestrate** as the agent orchestration layer.

**Disclaimer:** geospatial data and images in this repository are **fictional** and for demonstration only. This software **does not** replace decisions by competent authorities, search-and-rescue teams, or official technical assessments.

### Repository layout

| Path | Purpose |
|------|---------|
| `server/` | **FastAPI** backend: incidents, volunteers, risk areas, classification, mock image risk, Twilio WhatsApp notifications. |
| `dados/` | Mock JSON datasets and demo images (served at `/dados/...` when the API is running). |
| `wxo/` | Tool / agent definitions and domain knowledge for **watsonx Orchestrate**. |
| `docs/` | Event materials, demo scripts, and related notes. |


### Architecture (MVP)

| Layer | Description |
|-------|-------------|
| **Orchestration** | Agent(s) on **watsonx Orchestrate** with domain instructions and **tools** (OpenAPI) calling this backend for mock geo context and mock image “analysis”. |
| **Interface** | **No dedicated web UI** — interaction through **WhatsApp** (Twilio), **Telegram** (if wired), and/or the **watsonx Orchestrate** chat with the main agent. **`/docs`** and **`/redoc`** are for API inspection and manual tests only. |
| **Data** | JSON files and static images under `dados/`; **skill** identifiers in data and API responses use **English** slugs (e.g. `search and rescue`, `first aid`) to align with the codebase and `wxo/memory/`. |

### Prerequisites

- **IBM Cloud** access to **watsonx Orchestrate** (and optionally watsonx.ai), per hackathon rules.
- For **Twilio WhatsApp**: account SID, auth token, and approved sender (`TWILIO_WHATSAPP_NUMBER`). See [Twilio WhatsApp documentation](https://www.twilio.com/docs/whatsapp).
- **Never commit secrets.** Use `server/.env` (gitignored) or your platform’s secret store.

### Quick start

From the **repository root** (parent of `server/` and `dados/`):

```bash
cd server
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
cd ..
```

Optional: copy `server/.env.example` to `server/.env` and set Twilio variables. Without them, classification, matching, and incident creation still work; WhatsApp sends are skipped and `notified_count` may be `0`.

Run **uvicorn from the repo root** so `server.*` imports and paths to `dados/` resolve correctly:

```bash
python -m uvicorn server.main:app --reload --host 127.0.0.1 --port 8000
```

- **Interactive API:** http://127.0.0.1:8000/docs  
- **Alternative docs:** http://127.0.0.1:8000/redoc  
- **Static demo assets:** http://127.0.0.1:8000/dados/imagens_demo/…  

#### Main HTTP endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/incidents` | List incidents |
| `GET` | `/incidents/{id}` | Get one incident |
| `POST` | `/incidents` | Create incident (tool payload) |
| `POST` | `/incidents/classify` | Rule-based severity + skills from text |
| `GET` | `/volunteers` | List volunteers |
| `GET` | `/volunteers/match/{incident_id}` | Rank volunteers by skill overlap and neighborhood |
| `POST` | `/volunteers` | Register volunteer |
| `POST` | `/volunteers/notify` | Notify selected volunteers (Twilio when configured) |
| `GET` | `/risk-areas` | List mock risk areas |
| `POST` | `/analyze-risk` | Mock image risk from URL hints |

### watsonx Orchestrate

Tool YAML and knowledge live under `wxo/`. Point tool **server URLs** in wxO to your deployed or tunneled base URL (e.g. ngrok). Update `servers.url` in each OpenAPI fragment to match your environment.

### Further reading

- Hackathon / IBM materials: `docs/`  
- Step-by-step demo narrative: `docs/demo-scripts.md`  
- Planning notes: `plan.md`, `implementation_plan.md`  

### License

See [`LICENSE`](LICENSE).

*IBM, watsonx, and watsonx Orchestrate are trademarks of International Business Machines Corporation.* This project is not an official IBM product.
