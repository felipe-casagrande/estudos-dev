
using Aula.Modelos;
using System.Linq;
namespace Aula.Filtros;

internal class LinqFilter
{
    public static void FiltrarTodosOsGenerosMusicais(List<Musica> musicas)
    {
        var todosOsGenerosMusicais = musicas.Select(generos =>generos.Genero).Distinct().ToList();
        foreach (var genero in todosOsGenerosMusicais)
        {
            Console.WriteLine($"- {genero}");
        }
     
    }
    public static void FiltrarArtistaPorGeneroMusica(List<Musica> musicas,string genero)
    {
        var artistaPorGeneroMusical = musicas.Where(musica => musica.Genero.Contains(genero)).Select(musica => musica.Artista).Distinct();
        Console.WriteLine("Exibindo Artistas por genero musical");
        foreach (var artist in artistaPorGeneroMusical)
        {
            Console.WriteLine(artist);
        }
    }
}
