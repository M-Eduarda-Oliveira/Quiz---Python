import csv
import time
import os

score = 0
# both the chapters of code for both quizes are the same so there are no comments on the latter quiz


def start():
    os.system("cls")
    print('''Seja bem vindo ao nosso quiz!
  Aqui vamos testar os seus conhecimentos de robótica.
  No nosso sistemas temos algumas opções onde você pode escolher no nosso menu.''')
    time.sleep(2)
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
  ''')
    time.sleep(2)
    option1()


def option1():
    # this is where the user chooses the quiz they would like to play
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

    # elif option == 5:

    else:
        print("Resposta inválida.")
        time.sleep(2)
        print("Por favor escolha uma opção válida.")
        option1()


def easy():
    # sets the score across the whole code
    global score
    score = 0
# opens and reads the csv
    csvfile = open('easy.csv', 'r', encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')
# prints the question and posible answers until there are no more questions
    for q in lines:
        question = q[0]
        print(question)
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

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
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
            "Você pode escolher entre nível 'médio' ou 'difícil'. Se você não quer continuar jogando escreva 'não'").lower()
        if option3 == "médio":
            medium()

        elif option3 == "difícil":
            hard()

        elif option3 == "não":
            time.sleep(2)
            print("Ok! Bye bye :)")
            print("")


def medium():
    global score
    score = 0

    csvfile = open('medium.csv', 'r',  encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')

    for q in lines:
        question = q[0]
        print(question)
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

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
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

    csvfile = open('minecraft quiz two.csv', 'r', encoding='utf-8')

    lines = csv.reader(csvfile, delimiter=',')
    for q in lines:
        question = q[0]
        print(question)
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

        else:
            print("Infelizmente você errou :(")
            time.sleep(2)
            print("Esses são seus pontos: ", score)
            time.sleep(2)
            print("Vamos tentar novamente!")
            time.sleep(2)
            print("CARREGANDO....")
            time.sleep(3)
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


def addQuestions():
    csvfile = open('easy.csv', 'a', newline="")
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
    questions_and_answers = (question, answer1, answer2,
                             answer3, answer4, correctAnswer)
    writer = csv.writer(csvfile)
    writer.writerow(questions_and_answers)
    print("Questão registrada. Obrigada!")
    csvfile.close()
    start()


start()
