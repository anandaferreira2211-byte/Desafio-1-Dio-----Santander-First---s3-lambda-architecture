aws_servicos.py
# Programa: Descrição dos principais serviços AWS
# Entrada: Nome do serviço (ex: Amazon EC2)
# Saída: Descrição correspondente

# Lê a entrada (nome do serviço)
servico = input().strip()

# Verifica qual serviço foi informado e imprime a descrição correspondente
if servico == "Amazon EC2":
    print("Serviço de máquinas virtuais sob demanda")
elif servico == "Amazon S3":
    print("Armazenamento de objetos na nuvem")
elif servico == "AWS Lambda":
    print("Executa código sem gerenciar servidores")
elif servico == "Amazon Machine Image":
    print("Modelo de instância EC2 pré-configurado")
