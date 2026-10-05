namespace desafio5;

internal class Funcoes
{
    public static List<Livro> OrdenarAno(List<Livro> ListaLivros)
    {
        return ListaLivros.Where(l => l.Ano >= 2000).OrderBy(i =>i.Ano).ToList();
    }

    public static List<Livro> OrdenarAlfabeto(List<Livro> ListaLivros)
    {
        return ListaLivros.Where(l => l.Ano >= 2000).OrderBy(t => t.Titulo).ToList(); 
    }
}
