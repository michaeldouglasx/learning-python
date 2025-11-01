from datetime import datetime
data_atual = datetime.now().strftime('%d/%m/%y %H:%M:%S')
log = []

class Calculadora:
    
    def __init__(self):
        pass

    @staticmethod
    def soma(n1, n2):
        return n1+n2
    
    @staticmethod
    def subtracao(n1,n2):
        return n1-n2
    
    @staticmethod
    def multiplicacao(n1,n2):
        return n1*n2

    @staticmethod
    def divisao(n1,n2):
        try:
            return n1/n2
        except ZeroDivisionError as erro_divisao:
            nome_erro = type(erro_divisao).__name__
            mensagem_erro = str(erro_divisao)
            log.append([
                {'timestamp': data_atual,
                'tipo': nome_erro,
                'mensagem': mensagem_erro,
                'detalhe': 'Tentativa de divisão por zero.'}])

