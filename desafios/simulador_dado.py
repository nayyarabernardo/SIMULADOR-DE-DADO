'''1. SIMULADOR DE DADO
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.
Habilidades práticas a aplicar:
Tratamento de excepcionais
Condicionais If/Else
Entrada de dados
Geração de valores
Impressão
Detalhes e a seguir: Você desenvolverá um projeto em Python que irá executar o comando e que, ao ser executado, deverá ser executado ao usuário: “Você gostaria de jogar?” Ou alguma pergunta essa pergunta. Depois de feito essa pergunta, o seu programa precisa ter avaliado a resposta que foi digitado pelo.
Um passo importante aqui é que, quando digo avaliar quero dizer que você precisa receber o valor, tratar quando ele(a) disser que sim ou que não. Seu programa deve depois fazer uma ação necessária de acordo com a resposta que foi recebida pelo usuário. Seu script não deve construir ou para funcionar caso o usuário entre algo que não seja esperado, como, por exemplo, um número. Trate como excepcionais ou erros para que seu script rodou liso e sem problemas.
Caso a resposta à pergunta inicial tenha sido “sim” ou positiva de alguma forma, gere um valor aleatoriamente entre 1 e 6(você pode claro alterar essa faixa) e exiba o número no console para o usuário. Na sequência pergunte se ele(a) quer rodar o script novamente e trate essa situação para que continue rodando enquanto a resposta for positiva, fechando apenas quando for um “não”.
'''

importar  aleatório
da  hora  importar  dormir


class  SimuladorDados :
    def  __init__ ( self ):
        próprio . __dados  = [ 4 , 6 , 8 , 10 , 12 , 20 , 100 ]

    def  lanca_dado ( self , : int , quantidade : de_dados int = 1 ):  
        valor_max  =  tipo
        lances  =  quantidade_de_dados
        resultados  = []
        retorno  =  Nenhum
        se  lances  >  1 :
            para  dado  na  faixa ( lançamentos ):
                resultado  =  aleatório . randint ( 1 , valor_max )
                print ( f'O dado { dado + 1 } deu: { resultado } ' )
                resultados . anexar ( resultado )
                retorno  =  resultado
        mais :
            resultado  =  aleatório . randint ( 1 , valor_max )
            print ( f'Resultado: { resultado } ' )
            retorno  =  resultado

        voltar  voltar

    def  soma_resultado ( self , lista ):
        soma  =  0
        para  i  na  lista :
            soma  =  soma  +  int ( i )
        devolver  soma

    def  executar ( self ):
        print ( 'Olá, qual é o seu nome?' )
        dormir ( 1 )
        jogador  =  input ( 'Seu nome:' )
        dormir ( 2 )
        print ( f'Prazer em te conhecer {  player  } ' )
        dormir ( 1 )
        lancar  =  Verdadeiro
        while  lancar  ==  Verdadeiro :
            print ( 'Você quer lançar um dado? ' )
            dormir ( 2 )
            print ( 'Sim(1)' )
            print ( 'Não (2)' )
            tente :
                resposta  =  int ( input ( 'Sua resposta: ' ))
                se  resposta  ==  1 :
                    #Seleção de dados
                    print ( 'Vamos Jogar' )
                    dormir ( 1 )
                    print ( 'Que tipo de dado você quer lançar?' )
                    dormir ( 2 )
                    contador  =  0
                    para  dado  em  si mesmo . __dados :
                        print ( f'D { dado } ( { contador } )' )
                        contador  +=  1
                        dormir ( 1 )
                    tente :
                        tipo  =  int ( input ( 'Sua resposta: ' ))
                    exceto :
                        print ( 'Resposta invalida, tente de novo' )
                    dormir ( 2 )
                    print ( f'Você vai lançar o D {  self .__ dados [ tipo ] } ' )
                    dormir ( 1 )
                    #Seleção de quantidade
                    print ( 'Quantos dados você quer jogar?' )
                    dormir ( 1 )
                    tente :
                        qtd  =  int (
                            input ( 'Sua resposta(deve ser um número inteiro): ' ))
                    exceto :
                        print ( 'Resposta invalida, tente de novo' )
                    resultado  =  self . lanca_dado ( self . __dados [ tipo ], qtd )
                    if  tipo ( resultado ) ==  lista :
                        resultado  =  self . soma_resultado ( resultado )
                    imprimir (
                        f'Você lançou { qtd } D { self . __dados [ tipo ] } e { resultado } como resultado' )
                    dormir ( 10 )

                eli  resposta  ==  2 :
                    lancar  =  Falso
                    imprima ( 'ok' )

            exceto :
                print ( 'Resposta invalida, tente de novo' )


if  __name__  ==  '__main__' :
    SimuladorDados (). executar ()
