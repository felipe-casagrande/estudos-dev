using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Menus;

internal class MenuAvaliarBanda : Menu
{
    public override void Executar()
    {
        
        ExibirTituloDaOpcao("Avaliar banda");
        Console.Write("Digite o nome da banda que deseja avaliar: ");
        var nomeDaBanda = Console.ReadLine()!;

        var banda = BandaRepository.GetByName(nomeDaBanda);

        if (banda is null)
        {
            Console.WriteLine($"\nA banda {nomeDaBanda} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
        }
        
        Console.Write($"Qual a nota que a banda {nomeDaBanda} merece: ");
        var nota = int.Parse(Console.ReadLine());
        banda.AdicionarNota(nota);
        Console.WriteLine($"\nA nota {nota} foi registrada com sucesso para a banda {nomeDaBanda}");
        Thread.Sleep(2000);

        LimparTela();
    }
}
