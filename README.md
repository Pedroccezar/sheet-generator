# 📊 Automação de Escala de Plantão com Google Sheets

Script em Python para geração e atualização automática de escala semanal de plantão, com integração direta à API do Google Sheets.

O sistema consome uma planilha de disponibilidades, processa a distribuição dos membros por dia e publica automaticamente a escala final em outra planilha.



## 🛠 Tecnologias Utilizadas

- Python
- Pandas  
- NumPy  
- gspread  
- gspread-dataframe  
- Google Sheets API  



## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as dependências:

```bash
pip install -r requirements.txt
```



## 🔐 Configuração da API do Google

Para permitir que o projeto acesse e edite planilhas, é necessário configurar uma conta de serviço no Google Cloud.

### 1. Criar projeto no Google Cloud

Acesse:
https://console.cloud.google.com/

Crie um novo projeto.

### 2. Ativar APIs necessárias

No menu **APIs e Serviços → Biblioteca**, ative:

- Google Sheets API  
- Google Drive API  


### 3. Criar Conta de Serviço

- Vá em **APIs e Serviços → Credenciais**
- Clique em **Criar credenciais → Conta de Serviço**
- Defina um nome
- Finalize a criação


### 4. Gerar chave JSON

- Acesse a conta de serviço criada
- Vá na aba **Chaves**
- Clique em **Adicionar chave → Criar nova chave**
- Selecione o formato **JSON**
- Faça o download do arquivo

Renomeie o arquivo para:

```
credencial.json
```

Coloque o arquivo na raiz do projeto.

---

### 5. Compartilhar a planilha com a conta de serviço

Abra a planilha no Google Sheets:

- Clique em **Compartilhar**
- Adicione o e-mail da conta de serviço  
  (formato: `xxxxx@xxxxx.iam.gserviceaccount.com`)
- Conceda permissão de **Editor**

Sem essa etapa, a API não terá acesso à planilha.

---

## ▶️ Execução

Gerar escala inicial:

```bash
python main.py
```

Atualizar escala com lógica de rotação automática:

```bash
python update.py
```


## 📁 Estrutura do Projeto

```
.
├── main.py
├── update.py
├── credencial.json
└── README.md
```


## 📌 Funcionamento

### `main.py`

- Lê a planilha de disponibilidades
- Organiza membros por dia
- Evita duplicações na mesma semana
- Gera o DataFrame final
- Atualiza automaticamente a planilha destino

### `update.py`

- Lê a escala anterior
- Identifica o último dia trabalhado por cada membro
- Aplica rotação automática respeitando disponibilidade
- Publica nova versão da escala



## ⚠️ Segurança

O arquivo `credencial.json` contém dados sensíveis.

Adicione ao `.gitignore`:

```
credencial.json
```

Nunca versionar esse arquivo.



## 📎 Requisitos de Formato da Planilha

A planilha de entrada deve conter exatamente as seguintes colunas:

```
membros
segunda
terca
quarta
quinta
sexta
```

Alterações nesses nomes exigem ajuste no código.
