class Produto
{
    private double preco;
    private int estoque;
    public string Nome { get; set; }
    public string Marca { get; set; }
    public double Preco
    {
        get => preco;
        set
        {
            if (value < 0)
            {
                Console.WriteLine("Não pode ter preço negativo!");
            }
            else
            {
                preco = value;
            }
        }
    }
    public int Estoque
    {
        get => estoque;
        set
        {
            if (value < 0)
            {
                Console.WriteLine("Não pode estoque com valor negativo!");
            }
            else
            {
                estoque = value;
            }
        }
    }
    public string DescricaoProduto => $"{this.Nome} {this.Marca} - {this.preco}";
}