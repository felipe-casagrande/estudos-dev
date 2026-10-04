class Estoque
{   
    List<string> produtos = new List<string>();
    public void AdicionarProdutos(string produto)
    {
        produtos.Add(produto);
    }
    public void MostrarProdutos()
    {
        Console.WriteLine("Lista de produtos no estoque ");
        foreach (var produto in produtos)
        {
            Console.WriteLine(produto);
        }
    }
}