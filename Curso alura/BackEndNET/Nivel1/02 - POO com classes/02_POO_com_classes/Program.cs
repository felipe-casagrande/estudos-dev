Produto item1 = new Produto();
item1.nome = "teclado";
item1.descricao = "modelo compacto e silencioso," +
                        "perfeito para a produtividade diaria";
item1.preco = 80.00m;
item1.estoque = 15;

Console.WriteLine($@"dados do item 1:
Nome: {item1.nome};
Descrição:{item1.descricao};
Preço:{item1.preco};
Estoque:{item1.estoque}
");

if (item1.EstaDisponivel())
{
    Console.WriteLine("Produto está disponivel");
}

item1.AlterarPrecoComDesconto(0.2m);
Console.WriteLine($@"dados do item 1:
Nome: {item1.nome};
Descrição:{item1.descricao};
Preço:{item1.preco};
Estoque:{item1.estoque}
");
