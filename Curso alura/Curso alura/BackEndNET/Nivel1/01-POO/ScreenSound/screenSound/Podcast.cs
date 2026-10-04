class Podcast
{
    public Podcast(string host, string nome)
    {
        Host = host;
        Nome = nome;
    }

    public string Host { get; }
    public string Nome { get; }
    public int TotalEpisodios => ListaEpisodios.Count;
    public List<Episodio> ListaEpisodios = new List<Episodio>();
    public void AdicionarEpisodio(Episodio episodio)
    {
        ListaEpisodios.Add( episodio );
    }
    
    public void ExibirDetalhes()
    {
    
        Console.WriteLine($"Podcast {Nome} apresentado por {Host}\n");
        Console.WriteLine("Episodios");
   
        foreach (var ep in ListaEpisodios.OrderBy(e =>e.Ordem))
        {
            Console.WriteLine($"{ep.Resumo}");
            
        }
        Console.WriteLine($"Esse podcast possui {TotalEpisodios} episódios.");
    }
}

