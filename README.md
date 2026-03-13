# Teste Técnico — Central de Enquetes (75% Highcode + 25% Bubble)

## Sobre a Pipeimob

A Pipeimob é uma plataforma de gestão imobiliária em migração de Bubble para highcode. Este teste avalia suas habilidades como desenvolvedor fullstack que constrói o novo sistema e integra com o Bubble existente.

## Prazo

- **48 horas** após recebimento
- Tempo estimado: **4-6 horas**
- Uso de IA é permitido e esperado (documente no NOTES.md)

## Stack Obrigatória (Highcode)

- **Backend:** Python + FastAPI
- **Frontend:** React + Vite
- **Banco:** PostgreSQL (via psycopg2)
- **Deploy:** Docker + docker-compose

## Starter Repo

Você receberá um repositório base, baseado no template interno da Pipeimob. Fork e desenvolva a partir dele.

A estrutura segue o padrão de organização da Pipeimob: controllers em `api/v1/routes/`, lógica de negócio em `services/`, validação em `schemas/` e utilitários em `utils/`.

```
pipeimob-challenge/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                        # FastAPI app com CORS e health check
│   │   ├── api/
│   │   │   └── v1/
│   │   │       └── routes/                # TODO: Controllers (*_controller.py)
│   │   ├── models/                        # TODO: Database models/queries
│   │   ├── schemas/                       # TODO: Pydantic schemas (*_schema.py)
│   │   ├── services/                      # TODO: Business logic (*_service.py)
│   │   ├── utils/
│   │   │   ├── db_utils.py                # PostgreSQL connection (psycopg2)
│   │   │   └── logger.py                  # Logger configurado
│   │   └── auth/                          # TODO: JWT auth
│   ├── tests/                             # TODO: Testes com FastAPI TestClient
│   ├── requirements.txt                   # Dependências base incluídas
│   └── Dockerfile                         # Base funcional, completar se necessário
├── frontend/
│   ├── src/
│   │   ├── App.tsx                        # Routing básico
│   │   ├── main.tsx
│   │   ├── components/                    # Componente exemplo
│   │   ├── pages/                         # Skeleton login
│   │   ├── services/                      # API client base
│   │   └── hooks/
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
├── docker-compose.yml                     # PostgreSQL + backend + frontend
├── .env.example
├── README.md
└── NOTES.md                               # Template para documentar uso de IA
```

### Convenções de nomenclatura (seguir o padrão do template)
- **Controllers:** `poll_controller.py`, `auth_controller.py` (sufixo `_controller`)
- **Services:** `poll_service.py`, `auth_service.py` (sufixo `_service`)
- **Schemas:** `poll_schema.py`, `auth_schema.py` (sufixo `_schema`)
- **Rotas:** prefixo versionado `/api/v1/...`

## O Desafio

Construir uma **Central de Enquetes** fullstack com integração ao Bubble.

## Parte 1: Highcode (principal)

### 1. Autenticação

- Register com hash de senha (bcrypt) + Login retornando JWT
- Middleware de autenticação protegendo rotas

### 2. API Design

- CRUD completo de enquetes (POST, GET, PUT, DELETE `/api/polls`)
- Endpoint de votação com validação (`POST /api/polls/{id}/vote`)
- Pydantic models para request/response
- Status codes corretos + formato de erro consistente

### 3. Database

- Tabelas PostgreSQL: `users`, `polls`, `options`, `votes`
- Script de criação do schema (SQL ou via código Python)
- Constraints adequadas (unique vote por user/poll)

### 4. Business Logic

- Voto único por usuário/enquete
- Visibilidade pública/privada
- Bulk archive/unarchive de múltiplas enquetes
- Filtro por intervalo de datas

### 5. Deploy

- Dockerfile funcional
- docker-compose com PostgreSQL
- Deploy com URL pública (Railway, Render, Fly.io, etc.)

### 6. Frontend: UI

- Formulário de enquete com opções dinâmicas (add/remove)
- Timeline/feed com cards de enquetes
- Design responsivo

### 7. Frontend: Estado e Dados

- Integração API com error handling
- Loading states e feedback visual
- Gerenciamento de formulário

### 8. Frontend: Real-time

- Votos atualizam sem refresh (polling, SSE ou WebSocket)

### 9. Frontend: Rotas e Auth

- React Router com rotas protegidas
- Páginas de login/register

## Parte 2: Integração Bubble (complementar)

Demonstrar capacidade de integrar com Bubble criando:

### 1. Backend Workflow POST

- Criar um **Backend Workflow no Bubble** que recebe dados de uma nova enquete via POST (título, opções) e cria o registro no banco do Bubble
- O candidato deve chamar esse endpoint a partir do app highcode ou via Postman/curl para demonstrar

### 2. Backend Workflow GET

- Criar um **Backend Workflow no Bubble** que retorna dados de enquetes do Bubble em formato JSON
- Demonstrar a chamada a esse endpoint

### 3. Modelagem no Bubble

- Criar a tabela de enquetes no Bubble com modelagem correta (tipos de campo, relações)

### 4. API Connector

- Configurar o **API Connector** no Bubble para chamar pelo menos um endpoint do seu backend highcode

## Padrões Esperados

- Organização de código (separação de responsabilidades)
- Naming conventions (snake_case Python, camelCase React)
- README com instruções de setup
- Error handling adequado

## Diferenciais (opcionais)

- Testes unitários (pytest/vitest)
- Swagger/OpenAPI docs
- WebSocket para real-time
- Paginação

## Entrega

1. **Fork** do starter repo com código
2. **URL pública** do app deployado
3. **Link do app Bubble** (editor + app)
4. **NOTES.md** documentando:
   - Ferramentas de IA usadas
   - Decisões arquiteturais
   - Trade-offs
   - O que faria diferente

---

**Boa sorte!**

---

## Setup do Starter Repo

### Setup rápido

#### Com Docker (recomendado)

```bash
# 1. Copie o arquivo de ambiente
cp .env.example .env

# 2. Suba os containers
docker-compose up --build

# Backend: http://localhost:8000
# Frontend: http://localhost:3000
# Docs: http://localhost:8000/docs
```

#### Sem Docker

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### O que já está pronto

- FastAPI app com CORS configurado
- Health check (`GET /health`)
- Conexão PostgreSQL com `psycopg2` (`app/utils/db_utils.py`)
- Helper `run_query()` para executar queries SQL
- Logger configurado (`app/utils/logger.py`)
- Frontend com React Router, Tailwind CSS e página de login skeleton
- API client base (`src/services/api.ts`)
- Docker + docker-compose com PostgreSQL
- Testes de exemplo
