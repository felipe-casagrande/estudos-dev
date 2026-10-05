using ScreenSound.Modelos;
using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Menus;

internal class MenuRegistrarAlbum : Menu
{
    public override void Executar()
    {
        LimparTela();
        ExibirTituloDaOpcao("Registro de álbuns");

        Console.Write("Digite a banda cujo álbum deseja registrar: ");
        var nomeDaBanda = Console.ReadLine()!;

        var banda = BandaRepository.GetByName(nomeDaBanda);
        if (banda is null)
        {
            Console.WriteLine($"\nA banda {nomeDaBanda} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
            return;
        }

        Console.Write("Agora digite o título do álbum: ");
        var tituloAlbum = Console.ReadLine()!;

        banda.AdicionarAlbum(new Album(tituloAlbum));
        Console.WriteLine($"O álbum {tituloAlbum} de {nomeDaBanda} foi registrado com sucesso!");

        Thread.Sleep(4000);
        LimparTela();
    }
    
}
