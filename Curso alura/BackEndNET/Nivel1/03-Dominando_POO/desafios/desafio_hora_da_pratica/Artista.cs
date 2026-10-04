namespace Alura.Filmes;

class Artista
{
    public string Nome {  get; set; }
    public int Idade {  get; set; }
    public List<Filme> ListaFilmes { get; set; }

    public Artista(string nome, int idade)
    {
        Nome = nome;
        Idade = idade;
        ListaFilmes = new List<Filme>();
}

}