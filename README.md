# Coordenação de voluntariado em deslizamentos de barranco

PoC para o **Hackathon IA Descomplicada: Da Ideia à Implementação** (UNASP + IBM), com foco no tema **Orquestrando o Voluntariado Inteligente para Situações de Crise**. O cenário de uso trata de **deslizamentos de barranco**: apoio à priorização de áreas e ao **encaixe de voluntários por habilidades**, com **IBM watsonx Orchestrate** como núcleo de orquestração de agentes.

**Importante:** os dados geoespaciais e as imagens previstos para a demo são **fictícios**. A solução **não** substitui decisões de órgãos competentes, equipes de busca e salvamento ou análises técnicas oficiais.

## Estado do repositório

Este README é **inicial**: o código (adaptador Telegram/WhatsApp, serviços das tools, etc.) será adicionado conforme a implementação. O planejamento detalhado está em [`tarefas-e-fluxo.md`](tarefas-e-fluxo.md).

## Arquitetura prevista (MVP)

| Camada | Descrição |
|--------|-----------|
| **Orquestração** | Agente(s) no **watsonx Orchestrate** com instruções de domínio e **tools** (APIs) para contexto geo mock e “análise” de imagem fictícia. |
| **Interface** | **Sem front-end web** — interação por **Telegram** (preferencial) e/ou **WhatsApp**, ou conector nativo do wxO quando disponível. |
| **Dados** | Arquivos mock (ex.: GeoJSON/CSV) e imagens apenas para demonstração. |

## Documentação do evento e da IBM

Materiais oficiais e guias em [`docs/`](docs/) (PDFs). Para pré-work do edital, consulte também a [documentação Academic Initiative da IBM](https://github.com/academicinitiative/documentation) (conta IBM Cloud e watsonx Orchestrate).

## Pré-requisitos (planejado)

- Conta **IBM Cloud** com acesso ao **watsonx Orchestrate** (e opcionalmente watsonx.ai), conforme o edital.
- Para Telegram: bot criado com [@BotFather](https://t.me/BotFather) e URL de **webhook HTTPS** (ex.: túnel em desenvolvimento ou deploy leve).
- **Não** commite tokens, chaves ou URLs com segredos. Use variáveis de ambiente locais (ex.: `TELEGRAM_BOT_TOKEN`) e um arquivo `.env` fora do versionamento.

## Como rodar (em breve)

Instruções de instalação e execução serão preenchidas quando o adaptador e os serviços das tools estiverem no repositório.

## Licença

Veja o arquivo [`LICENSE`](LICENSE).

---

*IBM, watsonx e watsonx Orchestrate são marcas da International Business Machines Corporation.* Este projeto não é um produto oficial da IBM.
