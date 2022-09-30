import csv
from fileinput import filename
import time
import os

# Dando inicio ao contador de pontos que será utilizado em todo o código
score = 0

# Nesta função é apresentado o menu com as possibilidades de escolha do usuário
def start():
    os.system("cls")
    print('''Seja bem vindo ao nosso quiz!
  Aqui vamos testar os seus conhecimentos de robótica.
  No nosso sistemas temos algumas opções onde você pode escolher no nosso menu.''')
    print('''
  ------------------------------------------------------------
  ------M-E-N-U-------
  1- Quiz de questões fáceis
  2- Quiz de questões médias
  3- Quiz de questões difíceis
  4- Adicionar questões a um dos nossos Quiz
  5- Remover pergunta de um dos nossos Quiz
  6- ALterar alguma pergunta dos nossos Quiz
  7- Buscar pergunta em um dos nossos Quiz
  8- Sair
  ''')
    time.sleep(2)
    option1()

# Nesta função após a escolha do usuário, ele receberá algumas mensagens e será redirecionado para as devidas funções do programa.
def option1():
    option = int(input(''''''))
    if option == 1:
        print("Boa! Vamos começar por essa.")
        print("CARREGANDO AS PERGUNTAS....")
        time.sleep(3)
        os.system("cls")
        easy()

    elif option == 2:
        print('''Essa já não é tão fácil em?
    Vamos ver o que você sabe!''')
        time.sleep(1)
        print("CARREGANDO AS PERGUNTAS....")
        time.sleep(3)
        os.system("cls")
        medium()

    elif option == 3:
        print('''Então quer dizer que posso pegar pesado?
    Simbora!''')
        time.sleep(1)
        print("CARREGANDO AS PERGUNTAS....")
        time.sleep(3)
        os.system("cls")
        hard()

    elif option == 4:
        os.system("cls")
        addQuestions()

    elif option == 5:
        os.system("cls")
        removeQuestion()

    elif option == 8:
        os.system("cls")
        print("Obrigada por usar o nosso sistema. Bye bye :)")

    else:
        print("Resposta inválida.")
        time.sleep(2)
        print("Por favor escolha uma opção válida.")
        option1()

# A função easy será a qual o usuário será redirecionado quando fizer a escolha do quiz fácil.
def easy():

    # definindo a pontuação inicial
    global score
    score = 0
    os.system("cls")
# abrindo e lendo o arquivo csv. Além disso definimos o utf-8 para que seja permitido acentuação
    csvfile = open('easy.csv', 'r', encoding='utf-8')
    lines = csv.reader(csvfile, delimiter=',')
# printando e formatando a saída das questões e alternativas para o usuário.
    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        # neste caso como adicionamos a pergunta no formato de lista, o item na posição 5 é a letra que define a resposta correta 
        answer = q[5]
        user_answer = input("Qual é a resposta correta?").upper()
        time.sleep(2)
        print("A resposta correta é letra ", answer)
        # aqui fazemos a comparação da resposta do usuário com a resposta correr=ta
        if user_answer == answer:
            print("Você está indo bem!")
            time.sleep(2)
            # somando pontos ao score no caso de acerto
            score = score + 1
            print("Até agora esses são seus pontos: ", score)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")
    print("Finalizamos esse nível!")
    time.sleep(2)
# se a quantidade de acertos for menor que 4 enviamos uma mensagem positiva 
    if score < 4:
        print("Você precisa estudar um pouco mais :(")
        time.sleep(2)
        print("Seus pontos foram muito baixos.")
        time.sleep(2)
        print("Você só teve", score, "acertos nas questões.")
        time.sleep(2)
# desponibilizando a opção de o usuário jogar novamente este ou qualquer outro nivel
        option = input(
            "Gostaria de tentar novamente? Responda com sim ou não.").lower()
        if option == "sim":
            option1()
        elif option == "não":
            print("Ok")
            time.sleep(2)
            print("Bye bye :)")
            print("")
# se a quantidade de acertos for maior que 4 enviamos uma mensagem positiva e deixamos disponivel a opção de jogar novamente 
    elif score > 4:
        print("Você é muito bom!")
        time.sleep(2)
        print("Você acertou", score, "questões.")
        time.sleep(2)
        print("Temos dois outros níveis, gostaria de tentar?")
        option3 = input(
            "Você pode escolher entre nível 'médio' ou 'difícil'. Se você não quer continuar jogando escreva 'não'").lower()
        if option3 == "médio":
            medium()

        elif option3 == "difícil":
            hard()

        elif option3 == "não":
            time.sleep(2)
            print("Ok! Bye bye :)")
            print("")
# Os comentários da função easy() servem para as funções medium() e hard() sendo modificado apenas os valores necessários.

def medium():
    global score
    score = 0
    os.system("cls")

    csvfile = open('medium.csv', 'r',  encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')

    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        answer = q[5]
        user_answer = input("Qual é a resposta correta?").upper()
        time.sleep(2)
        print("A resposta correta é letra ", answer)
        if user_answer == answer:
            print("Você está indo bem!")
            time.sleep(2)
            score = score + 1
            print("Até agora esses são seus pontos: ", score)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")
# when the user has answered all the questions the code determinds the users score
    print("Finalizamos esse nível!")
    time.sleep(2)
# if it is below 4 it will print an 'encouraging' message
    if score < 4:
        print("Você precisa estudar um pouco mais :(")
        time.sleep(2)
        print("Seus pontos foram muito baixos.")
        time.sleep(2)
        print("Você só teve", score, "acertos nas questões.")
        time.sleep(2)
# the user will also get the option to play again
        option = input(
            "Gostaria de tentar novamente? Responda com sim ou não.").lower()
        if option == "sim":
            option1()

        elif option == "não":
            print("Ok")
            time.sleep(2)
            print("Bye bye :)")
            print("")
# if the user gets more than 4 they will get an actually encouraging message and will be asked if they want to play the other quiz
    elif score > 4:
        print("Você é muito bom!")
        time.sleep(2)
        print("Você acertou", score, "questões.")
        time.sleep(2)
        print("Temos dois outros níveis, gostaria de tentar?")
        option3 = input(
            "Você pode escolher entre nível 'fácil' ou 'difícil'. Se você não quer continuar jogando escreva 'não'").lower()
        if option3 == "fácil":
            easy()

        elif option3 == "difícil":
            hard()

        elif option3 == "não":
            time.sleep(2)
            print("Ok! Bye bye :)")
            print("")


def hard():
    global score
    score = 0

    csvfile = open('hard.csv', 'r', encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')
    for q in lines:
        question = q[0]
        print('''
        {}
        '''.format(question))
        posible_answers = (q[1], q[2], q[3], q[4],)
        time.sleep(2)
        print('''
        {} 
        {}
        {}
        {}
        '''.format(posible_answers[0], posible_answers[1], posible_answers[2], posible_answers[3]))
        answer = q[5]
        user_answer = input("Qual é a resposta correta?").upper()
        time.sleep(2)
        print("A resposta correta é letra ", answer)
        if user_answer == answer:
            print("Você está indo bem!")
            time.sleep(2)
            score = score + 1
            print("Até agora esses são seus pontos: ", score)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
            os.system("cls")
# when the user has answered all the questions the code determinds the users score
    print("Finalizamos esse nível!")
    time.sleep(2)
# if it is below 4 it will print an 'encouraging' message
    if score < 4:
        print("Vocêprecisa estudar um pouco mais :(")
        time.sleep(2)
        print("Seus pontos foram muito baixos.")
        time.sleep(2)
        print("Você só teve", score, "acertos nas questões.")
        time.sleep(2)
# the user will also get the option to play again
        option = input(
            "Gostaria de tentar novamente? Responda com sim ou não.").lower()
        if option == "sim":
            option1()

        elif option == "não":
            print("Ok")
            time.sleep(2)
            print("Bye bye :)")
            print("")
# if the user gets more than 4 they will get an actually encouraging message and will be asked if they want to play the other quiz
    elif score > 4:
        print("Você é muito bom!")
        time.sleep(2)
        print("Você acertou", score, "questões.")
        time.sleep(2)
        print("Temos dois outros níveis, gostaria de tentar?")
        option3 = input(
            "Você pode escolher entre nível 'fácil' ou 'médio'. Se você não quer continuar jogando escreva 'não'").lower()
        if option3 == "fácil":
            easy()

        elif option3 == "médio":
            medium()

        elif option3 == "não":
            time.sleep(2)
            print("Ok! Bye bye :)")
            print("")

# Função para adicionar pergunta
def addQuestions(): 
    os.system("cls")
    question_level_add = int(input('''Você gostaria de adicionar questões de que nível?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    4- Voltar ao menu '''))
    # após a escolha de qual quiz deseja adicionar o programa inicia e dá permissão para a adição de novas perguntas
    if question_level_add == 1:
        csvfile = open('easy.csv', 'a', newline="")
    elif question_level_add == 2:
        csvfile = open('medium.csv', 'a', newline="")
    elif question_level_add == 3:
        csvfile = open('hard.csv', 'a', newline="")
    elif question_level_add == 4:
        option1
    else:
        print("Escolha uma opção de adicionar válida.")
        addQuestions()
    # os inputs são pedidos separadamente e adicionado em variáveis para facilitar a comunicação com o usuário.
    question = input("Escreva aqui sua pergunta: ")
    answer1 = input('''Escreva aqui a primeira opção de alternativa:
    Ex.: A)Programação
    ''')
    answer2 = input('''Escreva aqui a segunda opção de alternativa:
    Ex.: B)Livros
    ''')
    answer3 = input('''Escreva aqui a terceira opção de alternativa:
    Ex.: C)Sapatos
    ''')
    answer4 = input('''Escreva aqui a quarta opção de alternativa:
    Ex.: D)Brinquedos
    ''')
    correctAnswer = input('''Agora escreva a letra da alternativa correta:
    Ex.: A
    ''')
    # adicionamos os valores no formato de lista
    questions_and_answers = (question, answer1, answer2, answer3, answer4, correctAnswer)
    # "ativamos" a função de escrever no código csvfile que definimos algumas linhas antes a partir da escolha do usuário 
    writer = csv.writer(csvfile)
    # comando de escrever linha no arquivo
    writer.writerow(questions_and_answers)
    print("Questão registrada. Obrigada!")
    csvfile.close()
    start()

# Função para remover pergunta 
def removeQuestion():
    os.system("cls")
    # momento de escolha do usuário
    question_file = int(input('''De qual destes quiz você gostaria de remover a pergunta?
    Digite:
    1- Fácil
    2- Médio
    3- Difícil
    4- Voltar ao menu
    '''))
    # função especifica de deletar que tem seus parâmetros modificados a partir da escolha do usuário
    def delete_line(filename, line_number):
      # abrindo e lendo todo o arquivo 
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # verificando se o valor que o usuário está depositando é válido para a quantidade de perguntas existentes no arquivo
        if (line_number <= len(lines)):
          # comando para deletar linha
            del lines[line_number - 1]
            with open(filename, "w") as file:
                for line in lines:
                    file.write(line)

        else:
            print("Essa linha", line_number, "não existe no arquivo.")
            print("Este arquivo tem", len(lines), "linhas.")
  # Apartir daqui as condicionais partem da decisão do usuário modificando os valores dos parâmetros e mostrando para o usuário todas as perguntas existentes
  # no arquivo para que ele escolha pelo número qual deseja deletar.
    if question_file == 1:
        delete_filename = 'easy.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 2:
        delete_filename = 'medium.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 3:
        delete_filename = 'hard.csv'
        archive = open(delete_filename)
        questions = csv.reader(archive)
        for question in questions:
            print('''{}
      '''.format(question))
        delete_line_number = int(
            input("Qual dessas questões deseja remover? Escreva o número a partir de 1."))
        delete_line(delete_filename, delete_line_number)
        option1()
    elif question_file == 4:
        option1
    else:
        print("Digite uma opção válida.")
        removeQuestion()

start()