# Desafio-1-Dio-----Santander-First---s3-lambda-architecture
# Arquitetura: S3 + Lambda (simples)

Descrição rápida:
Arquitetura simples para processamento automático de arquivos enviado ao S3. Quando um novo objeto é criado, o S3 dispara um evento que aciona uma AWS Lambda para processar o arquivo (ex.: redimensionar imagem, validar, gerar saída). O resultado é salvo em um bucket de saída.

## Diagrama (ASCII)
┌───────────────┐
│ Usuário │
│ (web/aplicativo) │
└───────┬───────┘


    │ Carregar arquivo
             ▼

┌───────────────┐
│ Balde S3 │
│ (armazenamento)│
└───────┬───────┘


      │ Evento: "s3:ObjectCreated:*"
               ▼

┌───────────────┐
│ Lambda │
│ (processa o │
│ arquivo) │
└───────┬───────┘


     │ Salva saída/processado
            ▼

┌───────────────┐
│ Balde S3 │
│ (processados) │
└───────────────┘
