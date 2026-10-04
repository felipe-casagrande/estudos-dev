class ContaBancaria
{
    public string NumeroConta { get;set; }
    public double Saldo {  get; set; }
    
    public ContaBancaria(string numeroConta, double saldo)
    {
        NumeroConta = numeroConta;
        Saldo = saldo; 
    }

    public void DepositarValor(double valor)
    {
        Saldo += valor;
    }
}