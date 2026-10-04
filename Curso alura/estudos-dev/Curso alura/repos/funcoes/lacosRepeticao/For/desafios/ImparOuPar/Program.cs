int contadorImpar = 0;
for (int i = 0; i <10; i++)
{
    Console.WriteLine("Digite um numero: ");
    int numero = int.Parse(Console.ReadLine());
    if (numero % 2 != 0)
    {
        contadorImpar++;
    }
}
Console.WriteLine($"Digitou: {contadorImpar} numeros impares");