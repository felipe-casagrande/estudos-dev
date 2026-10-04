Restaurante Shilo = new Restaurante();
ProdutoRestaurante produto1 = new ProdutoRestaurante();
ProdutoRestaurante produto2 = new ProdutoRestaurante();

produto1.NomeProduto = "coca cola";
produto1.preco = 10.5m;
produto2.NomeProduto = "Pizza";
produto2.preco = 20;

Cardapio cardapio1 = new Cardapio();
cardapio1.Itens.Add(produto1);
cardapio1.Itens.Add(produto2);

Mesa mesa1 = Shilo.AbrirMesa(1);
mesa1.AdicionarPedido(produto1, 3);
mesa1.AdicionarPedido(produto2,5);
mesa1.MostrarConta();
mesa1.CalcularTotal();








//mesa1.AdicionarPedido(produto1,2);
//mesa1.AdicionarPedido(produto2, 5);

//mesa1.MostrarConta();