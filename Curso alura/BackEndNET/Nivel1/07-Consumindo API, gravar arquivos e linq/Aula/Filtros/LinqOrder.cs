using Aula.Modelos;

namespace Aula.Filtros;

internal class LinqOrder
{
    public static void ExibirListaDeArtistasOrdenados(List<Musica> musicas)
    {
        var artistaOrdenados = musicas.OrderBy(musica => musica.Artista).Select(musica => musica.Artista).Distinct().ToList();
        // se fica apenas ate antes do select, ia ordenar por artista mas ia trazer todos os outros dados, colocando o select eu so trago o valor artista.
        Console.WriteLine("Lista de Artistas Ordenaddos");
        foreach(var  artista in artistaOrdenados)
        {
            Console.WriteLine($"-{artista}");
        }

    }
}
