
Console.WriteLine("Digite a idade");
int idade = int.Parse(Console.ReadLine());

if(idade < 0)
{
    Console.WriteLine("idade invalida");
}
else if (idade <= 12)
{
    Console.WriteLine("Infatil");
}
else if (idade <= 17)
{
    Console.WriteLine("adolescente");
}
else if (idade <= 59)
{
    Console.WriteLine("adulto");
}
else
{
    Console.WriteLine("idoso");
}


