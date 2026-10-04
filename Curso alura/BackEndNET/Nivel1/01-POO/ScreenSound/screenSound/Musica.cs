class Musica
{
    public Musica(Banda artista, string nome)
    {
        Artista = artista;
        Nome = nome;
    }
    public string Nome { get; }            //get leitura, set escrita. Ex: p.Nome = "Felipe";   // chama o set
                                                 //                          Console.WriteLine(p.Nome); // chama o get
    public Banda Artista { get; }
    public int Duracao { get; set; }
    public bool Disponivel { get; set; }
    public string DescricaoResumida  =>
        $"A música {Nome} pertence à banda {Artista}";
    //public void EscreveDisponivel(bool value)
    //{
    //    disponivel = value; 
    //}

    //public bool LeDisponivel()
    //{
    //    return disponivel;
    //}
    public void ExibirFichaTecnica()
    {
        Console.WriteLine($"Nome: {Nome}");
        Console.WriteLine($"Artista: {Artista.Nome}");
        Console.WriteLine($"Duração: {Duracao}");
        if (Disponivel)
        {
            Console.WriteLine("Disponivel no plano");
        }
        else
        {
            Console.WriteLine("Adquira o planos Plus+");
        }
    }

}

