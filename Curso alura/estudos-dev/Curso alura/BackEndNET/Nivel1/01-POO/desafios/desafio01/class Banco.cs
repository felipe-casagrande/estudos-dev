class Banco
{
    public int NumeroIndicador {  get; set; }
    public string NomeDoTitular { get; set; }   
    public float Saldo { get; set; }
    public int Senha { get; set; }

    public void ExibirInformacoes()
    {
        Console.WriteLine($"Nome do titular: {NomeDoTitular}");
        Console.WriteLine($"Saldo: {Saldo}");
    }
}