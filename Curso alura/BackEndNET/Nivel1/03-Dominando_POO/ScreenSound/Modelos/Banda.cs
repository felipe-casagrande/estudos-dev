namespace ScreenSound.Modelos;

internal class Banda : IAvaliavel
{
    private List<Album> albuns = new List<Album>();
    private List<Avaliacao> notas = new List<Avaliacao>();

    public Banda(string nome)
    {
        Nome = nome;
    }

    public string Nome { get; }
    public double Media
    {
        get
        {
             if (notas.Count == 0) // se nao tiver notas, retornar media 0
            {
                return 0;
            }
            else
            {
                return notas.Average(a => a.Nota);  //media das notas com lambda
            }
        }
    }

    public IEnumerable<Album> Albuns => albuns;

    public void AdicionarAlbum(Album album)
    {
        albuns.Add(album);
    }

    public void AdicionarNota(int nota)
    {
        var avaliacao = new Avaliacao(nota);
        notas.Add(avaliacao);
        //notas.Add(new Avaliacao(nota)); 
    }

    public void ExibirDiscografia()
    {
        Console.WriteLine($"Discografia da banda {Nome}");
        foreach (Album album in albuns)
        {
            Console.WriteLine($"Álbum: {album.Nome} ({album.DuracaoTotal})");
        }
    }
} 

