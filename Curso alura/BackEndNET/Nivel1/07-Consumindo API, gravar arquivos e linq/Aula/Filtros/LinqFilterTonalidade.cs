using Aula.Modelos;

namespace Aula.Filtros;

internal class LinqFilterTonalidade
{
    public static void FiltrarMusicaPorTonalidade(List<Musica> ListaMusicas)
    {
        var musicas = ListaMusicas.Where(m => m.Key == 1).ToList();
        Console.WriteLine($"Musicas da tonalidade C#");
        foreach (var musica in musicas)
        {
            Console.WriteLine($"{musica.Nome}-{musica.Tonalidade}");
        }
      
    }
}
