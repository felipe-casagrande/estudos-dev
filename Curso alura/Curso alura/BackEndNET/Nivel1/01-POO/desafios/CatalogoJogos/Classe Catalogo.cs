class CatalogoJogos
{
    private List<JogosClasse> Jogos { get; set; }

    public bool CatalagoVazio => Jogos.Count == 0;

    public CatalogoJogos()
    {
        Jogos = new List<JogosClasse>();
    }

    public void AdicionarJogo(string nome, int ano, string genero)
    {
        JogosClasse novoJogo = new JogosClasse(nome, ano, genero);
        Jogos.Add(novoJogo);
        Console.WriteLine($"Jogo: {nome} adicionado!");
    }

    public void ListarJogos()
    {
        if (CatalagoVazio)
        {
            Console.WriteLine("Catalogo vazio");
        }
        else
        {
            Console.WriteLine("Catalogo de jogos");
            foreach (var jogo in Jogos)
            {
                Console.WriteLine($"Nome: {jogo.Nome}, Genero: {jogo.Genero}, ano: {jogo.Ano}");
            }
        }
            
    }
}