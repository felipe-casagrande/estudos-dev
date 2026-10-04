
try
{
    Console.WriteLine("Digite o numerador");
    int numerador = int.Parse(Console.ReadLine());

    Console.WriteLine("Digite o denominador");
    int denominador = int.Parse(Console.ReadLine());

    int resultado = numerador / denominador;
    Console.WriteLine(resultado);
}    
catch (Exception ex)
    {
       Console.WriteLine(ex.Message);
    }

