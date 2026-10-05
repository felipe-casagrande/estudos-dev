using ScreenSound.Modelos;

namespace ScreenSound.Repositories;

internal static class BandaRepository
{
    public static List<Banda> Bandas { get; private set; } = [];

    public static void Add(Banda banda) =>
        Bandas.Add(banda);

    public static bool Exists(string nome) =>
        Bandas.Any(b => b.Nome.Equals(nome));

    public static Banda? GetByName(string nome) =>
        Bandas.FirstOrDefault(b => b.Nome.Equals(nome));
}
