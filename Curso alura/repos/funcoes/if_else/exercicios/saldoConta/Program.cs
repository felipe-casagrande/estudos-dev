
Console.WriteLine("Digite o saldo da sua conta");
decimal saldo = decimal.Parse(Console.ReadLine());

if (saldo > 0)
{
    Console.WriteLine("O saldo esta positivo");
}else if (saldo < 0)
{
    Console.WriteLine("O saldo esta negativo");
}
else
{
    Console.WriteLine("Saldo igual a 0");
}