Console.WriteLine("Digite seu nome: ");
string nome = Console.ReadLine();

Console.WriteLine("Que momento do dia é agora? ");
Console.WriteLine("1 - Manhã");
Console.WriteLine("2 - Tarde");
Console.WriteLine("3 - Noite");
int opcaoEscolhida = int.Parse(Console.ReadLine());

string saudacao = opcaoEscolhida switch
{
    1 => "Bom dia",
    2 => "Boa tarde",
    3 => "Boa noite",
    _ => "Opcao invalida"
};
Console.WriteLine($"{saudacao}, {nome}.");