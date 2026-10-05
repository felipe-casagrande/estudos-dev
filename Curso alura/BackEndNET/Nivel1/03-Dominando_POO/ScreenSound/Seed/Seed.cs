using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Seed;

internal static class Seed
{
    public static IEnumerable<Banda> GetBandas()
    {
        Banda ira = new Banda("Ira!");
        ira.AdicionarNota(10);
        ira.AdicionarNota(8);
        ira.AdicionarNota(6);

        Banda beatles = new("The Beatles");
        beatles.AdicionarNota(10);
        beatles.AdicionarNota(5);
        beatles.AdicionarNota(8);

        var bandas = new List<Banda>();
        BandaRepository.Bandas.Add(ira);
        BandaRepository.Bandas.Add(beatles);

        return bandas;
    }
}
