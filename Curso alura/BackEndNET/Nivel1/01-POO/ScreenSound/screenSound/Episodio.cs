class Episodio
{
    private List<string> Convidados = new ();
    public Episodio(int numero, string titulo, int duracao)
    {
        Ordem = numero;
        Titulo = titulo;
        Duracao = duracao;
    }


    public int Duracao { get; } 
    public int Ordem { get; }
    public string Titulo { get; }
    public string Resumo => $"{Ordem}. {Titulo} ({Duracao} min) - {string.Join(", ",Convidados)}";

    public void AdicionarConvidados(string convidado)
    {
        Convidados.Add(convidado);
    }
}