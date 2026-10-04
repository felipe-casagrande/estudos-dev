class Carro
{
    private int ano;
    public string Modelo { get; set; }
    public string Fabricante { get; set; }
    public int QuantidadePortas { get; set; }
    public int Ano
    {

        get => ano;
        set
        {
            if (value < 1960 || value > 2023)
            {
                Console.WriteLine("Valor invalido, insira um ano entre 1960 e 2023");
            }
            else
            {
                ano = value;
            }
        }
    }
    



    public int velocidade = 0;
    public string DescricaoDetalhada => $"Fabricante: {this.Fabricante}\nModelo: {this.Modelo}\nAno: {this.Ano}";

    public void acelerar()
    {
        Console.WriteLine("Acelerando...");
        if (velocidade < 150)
        {
            velocidade += 5;
            Console.WriteLine($"Velocidade atual: {velocidade}");
        }
        else
        {
            Console.WriteLine($"Carro ja esta em sua velocidade maxima!");
        }

    }

    public void frear()
    {
        if (velocidade > 0)
        {
            velocidade -= 5;
            Console.WriteLine($"Freiando carro, velocidade atual: {velocidade}");
        }
    }
    public void buzinar()
    {
        Console.WriteLine("Bi Bi");
    }
}