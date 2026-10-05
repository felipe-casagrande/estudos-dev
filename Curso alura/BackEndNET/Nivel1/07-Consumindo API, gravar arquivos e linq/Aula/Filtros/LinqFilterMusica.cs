using Aula.Modelos;

namespace Aula.Filtros;

internal class LinqFilterMusica
{
    public static void MusicasDeUmArtista(List<Musica> musicas,string nomeArtista)
    {
        var artista = musicas.Where(musica => musica.Artista.Equals(nomeArtista)).Select(musica=>musica.Nome).ToList();

        Console.WriteLine(nomeArtista);

        foreach (var musica in artista)
        {
            Console.WriteLine($" {musica} ");
        }
    }
}
