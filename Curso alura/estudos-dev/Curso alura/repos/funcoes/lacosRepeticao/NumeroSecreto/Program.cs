int numeroSecreto = 10;
int tentativa;
while (true)
{
   
    Console.WriteLine("Tenta adivinha o numero entre 1 a 10: ");
    tentativa = int.Parse(Console.ReadLine());
    if (tentativa == numeroSecreto)
    {
        Console.WriteLine("Voce acertou!, parabens");
        break;
    }
    else
    {
        Console.WriteLine("Errado! Tente novamente.");
    }
}
