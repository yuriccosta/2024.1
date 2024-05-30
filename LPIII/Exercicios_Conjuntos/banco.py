class banco:
    def transferePara(ContaBancaria, outraConta, valor = 0):
            if valor > 0:
                if ContaBancaria.retirada(valor) > 0:
                    outraConta.deposito(valor)
                    return True
                return False
            else:
                "Faz o que já estava implementado"

    def transfereDe(ContaBancaria, outraConta, valor = 0):
            if valor > 0:
                if outraConta.retirada(valor) > 0:
                    ContaBancaria.deposito(valor)
                    return True
                return False
            else:
                "Faz o que já estava implementado"
    


# Se fosse com herança
class mybanco(banco):
     def transferePara(ContaBancaria, outraConta, valor = 0):
        if ContaBancaria.retirada(valor) > 0:
            outraConta.deposito(valor)
            return True
        return False

def transfereDe(ContaBancaria, outraConta, valor = 0):
        if outraConta.retirada(valor) > 0:
            ContaBancaria.deposito(valor)
            return True
        return False