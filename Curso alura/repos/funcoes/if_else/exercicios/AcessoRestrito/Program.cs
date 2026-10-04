int senha = 42;
int nivelAcesso = 5;
Console.WriteLine("Digite a senha");
int senhaDigitada = int.Parse(Console.ReadLine());
Console.WriteLine("Digite o nivel");
int nivelDigitado = int.Parse(Console.ReadLine());


if (senhaDigitada == senha && nivelDigitado>= nivelAcesso)
{
    Console.WriteLine("Acesso permitido");
}
else
{
    Console.WriteLine("Acesso negado");
}

