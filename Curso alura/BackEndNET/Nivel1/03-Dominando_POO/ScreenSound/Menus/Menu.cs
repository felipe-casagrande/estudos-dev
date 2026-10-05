using ScreenSound.Modelos;

namespace ScreenSound.Menus;

internal abstract class Menu : IMenu
{
    public virtual void Executar()
    {
        return;
    }

    public void ExibirTituloDaOpcao(string titulo)
    {
        int quantidadeDeLetras = titulo.Length;
        string asteriscos = string.Empty.PadLeft(quantidadeDeLetras, '*');
        Console.WriteLine(asteriscos);
        Console.WriteLine(titulo);
        Console.WriteLine(asteriscos + "\n");
    }

    public virtual void LimparTela()
    {
        Console.Clear();
    }
}
