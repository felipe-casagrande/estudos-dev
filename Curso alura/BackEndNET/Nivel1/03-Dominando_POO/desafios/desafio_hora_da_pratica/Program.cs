using Alura.Filmes;
Artista ator1 = new("felipe", 20);
Filme filme1 = new("duro de matar1", 100);
List<Filme> FilmesCadastrados = new([filme1]);

foreach(Filme item  in FilmesCadastrados)
{
    Console.WriteLine(item.Titulo);
}