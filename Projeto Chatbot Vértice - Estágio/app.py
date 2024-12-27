from flask import Flask, render_template, request
from chatbot import encontrar_resposta
from chatbot import chatbot
import threading

# Inicialização
app = Flask(__name__)

# Rota
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    resposta = encontrar_resposta(user_message, {
        "quais exames vocês realizam?": "Realizamos exames médicos ocupacionais como admissional, demissional, periódico, retorno ao trabalho, mudança de riscos e consulta ocupacional.",
        "qual o horário de atendimento?": "Nosso horário de atendimento é de Segunda à Sexta, das 7h10 às 17h.",
        "onde fica a clínica?": "Nossa clínica está localizada na Avenida Nelson Spielmann, 857 (Palmital).",
        "preciso agendar um exame?": "Sim, é necessário agendar. Entre em contato pelo telefone (14) 99108-8095 para agendamento.",
    })
    return resposta

# Função para iniciar o servidor Flask
def iniciar_servidor():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    # Inicia o Flask em um thread separado
    thread_flask = threading.Thread(target=iniciar_servidor)
    thread_flask.daemon = True  # Permite que o thread Flask seja encerrado ao sair
    thread_flask.start()

    # Executa o chatbot 
    chatbot()