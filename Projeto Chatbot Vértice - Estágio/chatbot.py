import difflib # Permite interação mais humanizada buscando resposta com variações de perguntas

# Dicionário de perguntas e respostas
perguntas_resp = {
    "quais exames vocês realizam?": "Realizamos exames médicos ocupacionais como admissional, demissional, periódico, retorno ao trabalho, mudança de riscos e consulta ocupacional.",
    "qual o horário de atendimento?": "Nosso horário de atendimento é de Segunda à Sexta, das 7h10 às 17h.",
    "onde fica a clínica?": "Nossa clínica está localizada na Avenida Nelson Spielmann, 857 (Palmital).",
    "preciso agendar um exame?": "Sim, é necessário agendar. Entre em contato pelo telefone (14) 99108-8095 para agendamento.",
}

def encontrar_resposta(pergunta, perguntas_resp):
    # Encontrar a pergunta mais próxima com base na similaridade com apenas 1 retorno, similaridade de 50%
    pergunta_proxima = difflib.get_close_matches(pergunta, perguntas_resp.keys(), n=1, cutoff=0.5)
    if pergunta_proxima:
        return perguntas_resp[pergunta_proxima[0]]
    return "Desculpe, não entendi a sua pergunta. Tente novamente!"
    
# Função do chatbot
def chatbot():
    print("")
    print("------------------------------------------------------")
    print("Bem-vindo ao Chatbot de Vértice Medicina do Trabalho!")
    print("------------------------------------------------------")
    print("Caso deseje encerrar, digite 'sair'.")
    print("------------------------------------------------------")
    print("")

    while True:
        pergunta = input("").strip().lower() # Permite retirar espaços desnecessários e força a formatação ser minúscula
        if pergunta == "sair":
            print("")
            print("Encerrando chatbot...")
            print("")
            break
        resposta = encontrar_resposta(pergunta, perguntas_resp) # Permite procurar a resposta pela similaridade explicada acima
        print(f"Vértice: {resposta}")

# Executar o chatbot
if __name__ == "__main__":
    chatbot()