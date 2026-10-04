List<double> notas = new List<double>
        {
    8.5,
    6.2,
    9.1,
    5.8,
    7.4
        };

foreach (var n in notas)
{
    if (n < 7)
    {
        Console.WriteLine($"O aluno com a nota {n} - Abaixo da media");
    }
    else
    {
        Console.WriteLine($"O aluno com a nota {n} - esta indo muito bem!");

    }
}
