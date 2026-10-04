using System.Security.Cryptography.X509Certificates;

class Mesa
{
    public int Numero { get; set; }
    public List<Pedido> Pedidos { get; set; } = new List<Pedido>();

    public void AdicionarPedido(ProdutoRestaurante produto, int quantidade)
    {
        Pedidos.Add(new Pedido
        {
            Produto = produto,
            Quantidade = quantidade,
        });
        Console.WriteLine($"Pedido: {produto.NomeProduto} realizado na quantidade {quantidade}");
    }

    public decimal CalcularTotal()
    {
        decimal total = 0;
        foreach( var item in Pedidos)
        {
            total += item.Produto.preco * item.Quantidade;

        }
        return total;
    }
    public void MostrarConta()
    {
        Console.WriteLine($"Mesa {this.Numero}");
        foreach(var p in Pedidos)
        {
            decimal subtotal = p.Produto.preco * p.Quantidade;
            Console.WriteLine($"{p.Produto.NomeProduto} x{p.Quantidade} - R$ {subtotal:F2}");
        }
        Console.WriteLine($"Total: R$ {CalcularTotal():F2}");

    }

}