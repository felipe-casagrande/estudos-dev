Titular titular1 = new Titular("Felipe Casagrande", "123", "Rio de areia");

Conta conta1 = new Conta(titular1,2122,10,1000,5000);
Console.WriteLine($"{conta1.Titular.Nome}");
Console.WriteLine(conta1.Informacoes);

//Estoque estoque1 = new Estoque();
//estoque1.AdicionarProdutos("Desinfetante");
//estoque1.AdicionarProdutos("Esponja");
//estoque1.MostrarProdutos();