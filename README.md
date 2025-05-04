# FuriaBot

## Conteúdo

 - [📌 Introdução](#intro)
 - [🎯 Objetivo](#goal)
 - [🚀 Instalação / Execução local](#settings)
 - [🔧 Deploy em produção](#deploy)
 - [📁 Estrutura do Projeto](#structure)
 - [Teck Stack](#teck-stack)

---

<div id="intro"></div>

## 📌 Introdução

O [FuriaBot](https://t.me/furiagg2025_bot) é um bot desenvolvido para o Telegram com objetivo de facilitar o acompanhamento dos times [FURIA](https://www.instagram.com/furiagg/). Através de comandos simples, os usuários podem acessar rapidamente as últimas notícias, próximos jogos e outras informações relevantes sobre o time, tudo diretamente pelo Telegram.










---

<div id="goal"></div>

## 🎯 Objetivo

O projeto surgiu com a proposta de criar uma ferramenta prática para torcedores da FURIA, permitindo que se mantenham atualizados de forma automatizada e centralizada. Além disso, o projeto também visa:










---

<div id="settings"></div>

## 🚀 Instalação / Execução local

Siga os passos abaixo para rodar o [FuriaBot](https://t.me/furiagg2025_bot) localmente na sua máquina.

**1. Clone o repositório e entre na pasta:**  

```bash
git clone https://github.com/rodrigols89/furiabot.git
```

```bash
cd furiabot/
```

**2. Crie e ative o ambiente virtual (recomendado):**  

```bash
python -m venv environment
```

**LINUX:**  
```bash
source environment/bin/activate
```

**WINDOWS:**  
```bash
source environment/Scripts/activate
```

**3. Instale as dependências:**  

```bash
pip install -U -v --require-virtualenv -r requirements.txt
```

**4. Configure as variáveis de ambiente:**  

```bash
touch .env
```

```bash
TELEGRAM_TOKEN=ADICIONE_SEU_TOKEN_DO_TELEGRAM_AQUI
```

**5. Execute o bot:**  

```bash
python main.py
```

> **Se tudo estiver correto, você verá a mensagem:**  
> "🤖 Bot rodando... Envie comandos no Telegram."










---

<div id="deploy"></div>

## 🔧 Deploy em produção

Você pode hospedar o [FuriaBot](https://t.me/furiagg2025_bot) em uma VPS para que ele funcione 24/7. Abaixo estão os passos básicos para configurar o deploy com systemd.

**NOTE:**  
O mesmo processo que você fez na sua máquina local faça na sua VPS: Clone o repositório, entre na pasta, ...., Execute o bot.

Com o bot rodando na sua VPS agora, basta configurar o systemd para ele iniciar automaticamente ao reiniciar a VPS.

Primeiro crie um arquivo de incialização chamado **"furiabot.service"** em **"/etc/systemd/system/"**:

```bash
nano /etc/systemd/system/furiabot.service
```

O arquivo de configuração da minha VPS ficou assim (você pode modificar para atender ao seu caso):

```bash
[Unit]
Description=FuriaBot Telegram Service
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/furiabot
ExecStart=/root/furiabot/environment/bin/python main.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Agora, recarregue o `systemd` e ative o serviço:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable furiabot.service
sudo systemctl start furiabot.service
```

Alguns comandos úteis para trabalhar com o serviço são:

 - `systemctl status furiabot.service`
   - Verificar status.
   - **NOTE:** Esse comando é útil para ver se o serviço iniciou corretamente.
 - `journalctl -u furiabot.service -f`
   - Ver logs do serviço.
 - `systemctl stop furiabot.service`
   - Parar o serviço.
 - `systemctl restart furiabot.service`
   - Reiniciar o serviço.










---

<div id="structure"></div>

## 📁 Estrutura do Projeto

Esse projeto é bem simples e segue a seguinte estrutura:

```bash
furiabot/
├── .github/                      # Configurações do GitHub Actions
├── furiabot
│    └─ bot/                      # Pasta com os arquivos do bot
|        └─ handlers/             # Pasta com os handlers do bot
|            └─ menu.py           # Arquivo com o handler para o comando /menu (principal)
|            └─ news.py           # Arquivo com o handler para o comando /noticias
|            └─ nextgames.py      # Arquivo com o handler para o comando /proximosjogos
│    └─ tests/                    # Pasta com os testes unitários
|        └── test_placeholder.py  # Teste só para passar no CI
├── .editorconfig                 # Configurações do editor de texto
├── .env                          # Arquivo com variáveis de ambiente (token do bot)
├── .gitignore                    # Arquivo com configurações para arquivos ignorados
├── main.py                       # Ponto de entrada principal do bot
├── Makefile                      # Comando úteis para formatar e corrigir os códigos



└── README.md                 # Documentação do projeto
├── bot/
│   ├── handlers/              # Handlers responsáveis por cada comando do bot
│   │   ├── menu.py            # Comando /start
│   │   ├── news.py            # Comando /noticias
│   │   └── games.py           # Comando /proximosjogos
│   └── main.py                # Ponto de entrada principal do bot
├── tests/
│   └── bot/
│       └── handlers/          # Testes unitários para os handlers

├── requirements.txt           # Lista de dependências do projeto
└── README.md                  # Documentação do projeto

```


```bash

```


```bash

```


```bash

```


```bash

```









---

<div id="teck-stack"></div>

## Teck Stack

 - **Automação:**
   - [python-telegram-bot](https://python-telegram-bot.org/)
   - [python-dotenv](https://pypi.org/project/python-dotenv/)
 - **Formatação e Linter:**
   - [black](https://black.readthedocs.io/en/stable/)
   - [ruff](https://beta.ruff.rs/docs/)
   - [isort](https://pycqa.github.io/isort/)
 - **Testes:**
   - [pytest](https://docs.pytest.org/en/latest/)

---

**Rodrigo** **L**eite da **S**ilva - **rodrigols89**
