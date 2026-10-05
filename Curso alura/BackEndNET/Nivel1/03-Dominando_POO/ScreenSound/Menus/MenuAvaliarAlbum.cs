using ScreenSound.Modelos;
using ScreenSound.Repositories;

namespace ScreenSound.Menus;

internal class MenuAvaliarAlbum : Menu
{
    public override void Executar()
    {
        LimparTela();
        ExibirTituloDaOpcao("Avaliar Album");
        Console.Write("Digite o nome da banda que deseja avaliar: ");
        var nomeDaBanda = Console.ReadLine()!;

        var banda  = BandaRepository.GetByName(nomeDaBanda);
        if (banda is null)
        {
            Console.WriteLine($"\nA banda {nomeDaBanda} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
            return;
        }

        Console.Write("Agora digite o título do álbum: ");
        var tituloAlbum = Console.ReadLine()!;

        var album = banda.Albuns.FirstOrDefault(a => a.Nome.Equals(tituloAlbum));

        if (album is null)
        {
            Console.WriteLine($"\nO album {tituloAlbum} não foi encontrada!");
            Console.WriteLine("Digite uma tecla para voltar ao menu principal");
            Console.ReadKey();
            return;
        }
       
        Console.Write($"Qual a nota que o álbum {tituloAlbum} merece: ");
        var nota = int.Parse(Console.ReadLine());

        album.AdicionarNota(nota);
        Console.WriteLine($"\nA nota {nota} foi registrada com sucesso para o album{tituloAlbum}");

        Thread.Sleep(2000);
            
        Console.Clear();
    }
}
