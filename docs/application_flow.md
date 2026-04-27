# Complete Orchestrated Application Flow

This diagram presents all tools and agents, centered around the **Crisis Coordinator** as the primary orchestrator of the disaster response system.

```mermaid
graph TD
    %% User Entry
    User([User: WhatsApp / Orchestrate Chat]) ==> CC

    %% Central Agent
    CC{Agent: Crisis Coordinator}

    %% Delegated Agents & their specific tools
    subgraph Agent_RO ["Agent: Registry Officer"]
        RO_CI[Tool: createIncident]
        RO_CV[Tool: createVolunteer]
    end

    subgraph Agent_VM ["Agent: Volunteer Matcher"]
        VM_MV[Tool: matchVolunteers]
    end

    %% Tools directly orchestrated by CC
    subgraph CC_Tools ["Crisis Coordinator Tools"]
        direction TB
        CC_IC[Tool: classifyIncident]
        CC_RA[Tool: analyzeRisk]
        CC_GC[Tool: getRiskAreas]
        CC_VN[Tool: notifyVolunteers]
    end

    %% Orchestration Logic
    CC ==> |"1. Analyze Image"| CC_RA
    CC ==> |"2. Classify Incident"| CC_IC
    CC -.-> |"Get Context"| CC_GC
    
    CC ==> |"3. Request Entry"| Agent_RO
    Agent_RO -.-> |"Return IDs"| CC
    
    CC ==> |"4. Find Responders"| Agent_VM
    Agent_VM -.-> |"Return matches"| CC
    
    CC ==> |"5. Final Alert"| CC_VN

    %% Output
    CC_VN -.-> |WhatsApp| V([Volunteers])

    %% Database
    DB[(JSON Storage)]
    Agent_RO --- DB
    Agent_VM --- DB
    CC_Tools --- DB

    %% Styling
    classDef orchestrator fill:#fff3e0,stroke:#e65100,stroke-width:3px;
    classDef agent fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef tool fill:#f3e5f5,stroke:#4a148c,stroke-width:2px;
    classDef storage fill:#eceff1,stroke:#263238,stroke-width:2px;
    classDef user fill:#f5f5f5,stroke:#9e9e9e,stroke-width:2px;

    class CC orchestrator;
    class Agent_RO,Agent_VM agent;
    class CC_IC,CC_RA,CC_GC,CC_VN,RO_CI,RO_CV,VM_MV tool;
    class DB storage;
    class User,V user;
```

## Agent & Tool Catalog

| Agent | Tools Managed | Responsibility |
| :--- | :--- | :--- |
| **Crisis Coordinator** | `analyzeRisk`, `classifyIncident`, `getRiskAreas`, `notifyVolunteers` | Orchestrates the triage, context gathering, and final execution of notifications. |
| **Registry Officer** | `createIncident`, `createVolunteer` | Handles formal data persistence and ID generation. |
| **Volunteer Matcher** | `matchVolunteers` | Computational matching of incidents to available human resources. |
