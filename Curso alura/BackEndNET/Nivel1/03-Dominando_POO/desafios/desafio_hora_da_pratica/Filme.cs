namespace Alura.Filmes;
class Filme
{
    public string Titulo {  get; set; }
    public decimal Duracao {  get; set; }
    public List<Artista> Elenco = new List<Artista>();

    public Filme(string titulo, decimal duracao)
    {
        Titulo = titulo;
        Duracao = duracao;
    
    }
    public void AdicionarArtistaAoFilme(Artista ator)
    {
        if (ator != null && !Elenco.Contains(ator))
        {
            Elenco.Add(ator);
            ator.ListaFilmes.Add(this);
        }
    }
}