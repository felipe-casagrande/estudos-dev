
Console.WriteLine("Informe a nota final do aluno");
double nota = double.Parse(Console.ReadLine());

if (nota >= 9)
{
    Console.WriteLine("Nota A");
}
else if (nota >= 7 )
{
    Console.WriteLine("Nota B");
}
else if (nota >= 5 )
{
    Console.WriteLine("Nota C");
}
else
{
    Console.WriteLine("Nota D");
}
