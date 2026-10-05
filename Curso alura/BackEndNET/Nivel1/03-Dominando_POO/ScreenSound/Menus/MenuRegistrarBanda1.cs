using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Menus;

internal class MenuRegistrarBanda1 : Menu
{
    public override void Executar()
    {
        LimparTela();
        ExibirTituloDaOpcao("Registro das bandas");

        Console.Write("Digite o nome da banda que deseja registrar: ");
        string nomeDaBanda = Console.ReadLine()!;

        if (BandaRepository.Exists(nomeDaBanda))
        {
            Console.WriteLine($"A banda {nomeDaBanda} já existe");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
            return;
        }
        var banda = new Banda(nomeDaBanda);
        BandaRepository.Bandas.Add(banda);
        

        Console.WriteLine($"A banda {nomeDaBanda} foi registrada com sucesso!");
        Thread.Sleep(4000);

        Console.Clear();
    }
}
