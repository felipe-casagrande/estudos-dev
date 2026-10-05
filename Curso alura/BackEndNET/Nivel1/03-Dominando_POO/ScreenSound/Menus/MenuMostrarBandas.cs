using ScreenSound.Modelos;
using ScreenSound.Repositories;
namespace ScreenSound.Menus;

internal class MenuMostrarBandas : Menu
{
    public override void Executar()
    {
        LimparTela();
        ExibirTituloDaOpcao("Exibindo todas as bandas registradas na nossa aplicação");

        foreach (var banda in BandaRepository.Bandas)
            Console.WriteLine($"Banda: {banda.Nome}");
        

        Console.WriteLine("\nDigite uma tecla para voltar ao menu principal");
        Console.ReadKey();
        LimparTela();
    }
}