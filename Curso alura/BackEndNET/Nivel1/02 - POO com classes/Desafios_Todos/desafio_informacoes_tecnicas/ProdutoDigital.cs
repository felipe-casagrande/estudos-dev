class ProdutoDigital
{
    public string Nome { get; set; }
    public double Preco { get; set; }
    public InformacaoTecnica InfoTecnica {  get; set; }

    public ProdutoDigital(string nome, double preco,InformacaoTecnica infoTecnica)
    {
        Nome = nome;
        Preco = preco;
        InfoTecnica = infoTecnica;
    }
    public void ExibirDetalhes()
    {
        Console.WriteLine(Nome);
        Console.WriteLine(Preco);
        Console.WriteLine(InfoTecnica.SistemaOperacional);
        Console.WriteLine(InfoTecnica.TamanhoMB);
    }
}