List<int> notas = new List<int> { 4, 7, 5, 9, 6 };

foreach(var n in notas)
{
    if (n < 6)
    {
        Console.WriteLine($"Nota {n} - Reprovado");
    }
    else
    {
        Console.WriteLine($"Nota {n} - Aprovado");

    }
}
