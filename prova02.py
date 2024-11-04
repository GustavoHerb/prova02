# Criando um dicionário para armazenar as informações do contato
contato = {}

# Solicitando ao usuário que insira as informações
contato['nome'] = input("Digite o nome do contato: ")
contato['telefone'] = input("Digite o número de telefone do contato: ")
contato['email'] = input("Digite o endereço de email do contato: ")

# Exibindo o conteúdo do dicionário
print("\nInformações do contato:")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")
