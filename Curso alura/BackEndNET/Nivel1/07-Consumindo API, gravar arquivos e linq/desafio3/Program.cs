List<int> numeros = new List<int> { 10,20,30};
try
{
    int elemento = numeros[2];
    Console.WriteLine($"Elemento: {elemento}");
}
catch (ArgumentOutOfRangeException)
{
    Console.WriteLine("O indice especificado nao existe na lista");
}
catch(Exception ex)
{
    Console.WriteLine(ex.Message);
}