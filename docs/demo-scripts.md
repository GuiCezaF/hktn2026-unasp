# Roteiros da Demo

Este documento contem os roteiros passo a passo para a demonstracao do sistema de orquestracao de voluntarios durante o Hackathon UNASP 2026.

## Cenario 1: Caminho Feliz (Deslizamento Critico)

**Objetivo:** Demonstrar o fluxo completo e ideal da aplicacao, desde o relato do incidente ate a sugestao de notificacao dos voluntarios selecionados.

### Contexto
- **Incidente:** Deslizamento com pessoas em risco (inc-001)
- **Local:** Brasilandia
- **Classificacao Esperada:** CRITICO
- **Agentes Envolvidos:** Coordenador (Principal) -> Matcher (Colaborador)

### Passo a Passo

1. **Apresentacao do Sistema (Instituicao/Defesa Civil):**
   - O agente inicia a conversa no WhatsApp (ou chat do wxO).
   - *Agente:* "Ola! Sou o Coordenador de Voluntariado. Estou aqui para ajudar a organizar a resposta a incidentes. Como posso ajudar agora?"

2. **Relato do Incidente (Usuario):**
   - *Usuario envia:* "Houve um grande deslizamento na Rua das Flores, bairro Brasilandia. Tres predios residenciais estao em risco de desabamento. Chuva forte nas ultimas 48 horas. Pelo menos 15 pessoas podem estar presas. Precisamos de ajuda urgente."

3. **Analise e Classificacao (Sistema):**
   - O agente principal aciona a **Tool A (Contexto Geografico)** para buscar o historico da encosta na Brasilandia.
   - O agente principal aciona a **Tool B (Classificacao)**.
   - *Agente:* "Entendido. Este incidente foi classificado como **CRITICO** devido ao risco imediato a vida e infraestrutura (historico de alto risco na Brasilandia). As habilidades necessarias para esta operacao sao: Busca e Salvamento, Engenharia Estrutural, Primeiros Socorros e Apoio Psicologico."

4. **Match de Voluntarios (Sistema):**
   - O agente principal delega a tarefa para o **Agente Colaborador (Matcher)**.
   - O agente colaborador aciona a **Tool C (Match de Voluntarios)**.
   - *Agente:* "Apos analisar nosso banco de voluntarios com base nestas habilidades e na proximidade ao local, os melhores perfis disponiveis sao:"
     - **Carlos Mendes** (Engenheiro Estrutural, Especialista em Avaliacoes)
     - **Fernanda Costa** (Bombeira Voluntaria, Busca e Salvamento)
     - **Ana Silva** (Logistica e Primeiros Socorros)
     - **Diego Nascimento** (Piloto de Drone, Mapeamento Aereo)
     - **Beatriz Oliveira** (Psicologa, Suporte a Crise)

5. **Acao Final (Usuario/Sistema):**
   - *Usuario:* "Perfeito. Notifique os 5 voluntarios, por favor."
   - *Agente:* "Notificacoes de mobilizacao urgentes enviadas para Carlos, Fernanda, Ana, Diego e Beatriz com as coordenadas e instrucoes de seguranca."

---

## Cenario 2: Informacao Incompleta

**Objetivo:** Demonstrar a capacidade cognitiva do agente em identificar falta de contexto e conduzir perguntas de esclarecimento antes de acionar ferramentas.

### Contexto
- **Incidente:** Erosao de solo (inc-002)
- **Local:** Jardim Angela
- **Classificacao Esperada:** MODERADO

### Passo a Passo

1. **Relato Vago (Usuario):**
   - *Usuario:* "Parece que teve um problema numa encosta aqui perto. Ta chovendo muito."

2. **Pedido de Esclarecimento (Sistema):**
   - O agente reconhece que nao ha informacao suficiente para classificar a severidade ou buscar voluntarios.
   - *Agente:* "Para que eu possa classificar a urgencia e enviar a equipe correta, por favor me informe: 1. Qual a localizacao (bairro ou endereco)? 2. Ha pessoas feridas ou presas? 3. Ha danos visiveis a predios ou rachaduras no solo?"

3. **Fornecimento de Detalhes (Usuario):**
   - *Usuario:* "E no Jardim Angela, na Rua Esperanca. Ninguem se feriu, mas tem umas casas com rachaduras na fundacao porque o solo cedeu um pouco."

4. **Classificacao e Resultado (Sistema):**
   - O agente aciona as **Tools A e B**.
   - *Agente:* "Obrigado. Com base nessas informacoes, o incidente foi classificado como **MODERADO**. Serao necessarios profissionais com habilidades em Engenharia Estrutural e Mapeamento. Deseja que eu liste os voluntarios mais proximos para essa avaliacao?"

5. **Encerramento:**
   - O usuario confirma e o fluxo de match se repete.
