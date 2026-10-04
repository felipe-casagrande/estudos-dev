Dictionary<string,int> Loja = new Dictionary<string,int>();

string nomeProduto = "Pao";
Loja[nomeProduto] = 10;

string nomeProduto2 = "Goiaba";
Loja[nomeProduto2] = 3;

string nomeProduto3 = "Azeite";
Loja[nomeProduto3] = 2;

foreach( var produto in Loja)
{
    Console.WriteLine($"Produto: {produto.Key} quantidade: {produto.Value}");
}

Console.Write("Digite o nome do produto que deseja ver a quantidade: ");
string Produto = Console.ReadLine();
if (Loja.ContainsKey(Produto))
{
    Console.WriteLine($"Produto: {Produto} quantidade: {Loja[Produto]}");

}