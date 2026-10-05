namespace desafio6;

internal class Produto
{
    public string Nome { get; set; }
    public int Preco { get; set; }

    public Produto(string nome, int preco)
    {
        Nome = nome;
        Preco = preco;
    }
}
