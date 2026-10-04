class Cardapio
{
    public List<ProdutoRestaurante> Itens { get; set; } = new List<ProdutoRestaurante>();
    public void AdicionarProduto(ProdutoRestaurante produto)
    {
        Itens.Add(produto);
    }
    public void ExibirCardapio()
    {
        foreach (var produto in Itens)
        {
            Console.WriteLine(produto.NomeProduto);
        }
    }
    public string BuscarProduto(string nome)
    {
        foreach (var item in Itens)
        {
            if (item.NomeProduto == nome)
            {
                return $"Nome: {nome}\nPreço: {item.preco}";
            }
        }

        return null;
    }
}