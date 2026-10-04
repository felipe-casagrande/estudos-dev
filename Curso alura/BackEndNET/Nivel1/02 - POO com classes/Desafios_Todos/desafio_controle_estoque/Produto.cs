class Produto
{
    public string Nome {  get; set; }
    private int QuantidadeEstoque {  get; set; }

    public Produto(string nome, int quantidadeInicial )
    {
        Nome = nome;
        QuantidadeEstoque = quantidadeInicial;
    }
    public void Retirar(int quantidade)
    {
        if (quantidade <=0)
        {
            Console.WriteLine("Erro,Quantidade para retirada tem que ser maior que 0");
        }
        else if (quantidade <= QuantidadeEstoque)
        {
            QuantidadeEstoque -= quantidade;
            Console.WriteLine($"A retirada de {quantidade} foi realizada com sucesso!");
        }
        else
        {
            Console.WriteLine("Erro: Quantidade para retirar maior que a quantidade do estoque");
        }
    }
    public void ExibirEstoque()
    {
        Console.WriteLine($"Produto:{Nome}");
        Console.WriteLine($"Quantidade: {QuantidadeEstoque}");
    }
}