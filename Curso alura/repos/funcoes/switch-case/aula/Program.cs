/*Console.WriteLine("\nMENU:");
Console.WriteLine("1 - Ver produtos");
Console.WriteLine("2 - Fazer pedido");
Console.WriteLine("0 - Sair");
Console.Write("Escolha uma opção: ");

int opcao = int.Parse(Console.ReadLine());

switch (opcao)
{
    case 1:
        Console.WriteLine("Mostrando produtos…");
        break;
    case 2:
        Console.WriteLine("Pedido realizado!");
        break;
    case 0:
        Console.WriteLine("Saindo…");
        break;
    default:
        Console.WriteLine("Opção inválida!");
        break;


}
*/
// código omitido

Console.WriteLine("Digite o tipo de cliente (Comum, VIP, Premium):");
string tipoCliente = Console.ReadLine();

decimal desconto;

desconto = tipoCliente switch
{
    "Comum" => 0.05m,
    "VIP" => 0.10m,
    "Premium" => 0.15m,
    _ => 0.00m
};
Console.WriteLine(desconto);