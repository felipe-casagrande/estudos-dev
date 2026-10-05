using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Menus;

internal class MenuExibirDetalhes : Menu
{
    public override void Executar()
    {
        LimparTela();
        ExibirTituloDaOpcao("Exibir detalhes da banda");
        Console.Write("Digite o nome da banda que deseja conhecer melhor: ");
        var nomeDaBanda = Console.ReadLine()!;

        var banda = BandaRepository.GetByName(nomeDaBanda);
        if (banda is null)
        {
            Console.WriteLine($"\nA banda {nomeDaBanda} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
        }
  
        Console.WriteLine($"\nA média da banda {nomeDaBanda} é {banda.Media}.");
        Console.WriteLine("\nDiscografia: ");
        foreach (var album in banda.Albuns)
        {
            Console.WriteLine($"{album.Nome}-> {album.Media}");
        }
        Console.WriteLine("Digite uma tecla para votar ao menu principal");
        Console.ReadKey();
        LimparTela();
    }
}

