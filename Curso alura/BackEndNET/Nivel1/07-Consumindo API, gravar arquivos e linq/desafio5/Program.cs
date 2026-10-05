using desafio5;

var livro1 = new Livro("A prendendo LINQ", "Felipe Casagrande", 2026);
var livro2 = new Livro("C  Diario de um Banana", "Qualquer Autor", 2023);
var livro3 = new Livro("B Sou Noob", "Bolsonaro", 2000);

var ListaLivros1 = new List<Livro> { livro1, livro2, livro3 };

ListaLivros1 = Funcoes.OrdenarAlfabeto(ListaLivros1);

foreach (var item in ListaLivros1)
{
    Console.WriteLine(item.Titulo);
}

