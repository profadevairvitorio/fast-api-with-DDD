# 📘 Guia de Execução do Projeto

Este projeto é uma API construída com FastAPI, utilizando o padrão DDD (Domain-Driven Design) para cadastro de alunos e registro de aulas.

## 🚀 Passo a Passo para Rodar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/profadevairvitorio/meu-qr-code.git
cd fast-api-with-DDD
```

### 2️⃣ Criar e Ativar um Ambiente Virtual
```bash
python3 -m venv venv
source venv/bin/activate  # -> Linux/Mac
.\venv\Scripts\activate # -> Windows: 
```

### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Iniciar o Servidor
```bash
uvicorn main:app --reload
```

### 5️⃣ Acessar a Documentação Interativa
- Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Estrutura de Pastas

```
.
├── application
│   ├── crud.py            # Operações CRUD
│   ├── schemas.py         # Schemas de validação
│   └── services.py        # Regras de negócio adicionais
│
├── domain
│   └── models.py          # Modelos do banco
│
├── infrastructure
│   ├── database.py        # Configuração do SQLite
│   └── repositories.py    # Acesso direto ao banco (opcional)
│
├── main.py                # Aplicação FastAPI
├── requirements.txt       # Dependências
└── README.md               # Documentação
```

---

## 🧪 Testando Endpoints
### ➡️ Criar um Aluno
```bash
POST /students/
{
  "name": "João Silva",
  "email": "joao@example.com",
  "languages": ["Python", "JavaScript"],
  "city": "São Paulo",
  "state": "SP"
}
```

### ➡️ Listar Alunos
```bash
GET /students/
```

### ➡️ Cadastrar uma Aula
```bash
POST /lessons/
{
  "student_id": 1,
  "date": "2025-02-13",
  "topic": "Estruturas de Dados",
  "notes": "Aula prática com listas e dicionários"
}
```

### ➡️ Consultar Aulas de um Aluno
```bash
GET /students/1/lessons
```
