public class banco {
    public boolean transferePara(banco ContaBancaria, banco outraConta, float valor){
        if (ContaBancaria.retirada(valor) > 0){
            outraConta.deposito(valor);
            return true;
        }
        return false;
    }

    public boolean transfereDe(banco ContaBancaria, banco outraConta, float valor){
        if (outraConta.retirada(valor) > 0){
            ContaBancaria.deposito(valor);
            return true;
        }

        return false;
    }
}

// Se fosse com herança (não precisaria criar os outros dois métodos anteriores)
// my banco estaria em outro arquivo
public class mybanco extends banco{

    public boolean transferePara(banco ContaBancaria, banco outraConta, float valor){
        if (ContaBancaria.retirada(valor) > 0){
            outraConta.deposito(valor);
            return true;
        }
        return false;
    }

    public boolean transfereDe(banco ContaBancaria, banco outraConta, float valor){
        if (outraConta.retirada(valor) > 0){
            ContaBancaria.deposito(valor);
            return true;
        }

        return false;
    }
}
