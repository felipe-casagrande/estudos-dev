using ScreenSound.Modelos;

namespace ScreenSound.Menus;

internal interface IMenu
{
    void Executar();
    void ExibirTituloDaOpcao(string titulo);
    void LimparTela();
}