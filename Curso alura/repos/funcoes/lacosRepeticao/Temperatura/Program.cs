int opcao;
double temperatura;
do
{
    Console.WriteLine("1- Celsius para Fahrenheit");
    Console.WriteLine("2- Fahrenheit para Celsius");
    Console.WriteLine("3- Sair");
    opcao = int.Parse(Console.ReadLine());
    switch (opcao)
    {
        case 1:
            Console.WriteLine("Digite a temperatura em celsius");
            temperatura = double.Parse(Console.ReadLine());
            double calculo = (temperatura * 9 / 5) + 32;
            Console.WriteLine($"Celsius: {temperatura}\nFahrenheit: {calculo}");
            break;
        case 2:
            Console.WriteLine("Digite a temperatura em Fahrenheit");
            temperatura = double.Parse(Console.ReadLine());
            calculo = (temperatura - 32) * 5 / 9;
            Console.WriteLine($"Celsius: {calculo}\nFahrenheit: {temperatura}");
            break;
        case 3:
            Console.WriteLine("Saindo..");
            break;

        default:
            Console.WriteLine("Opcao invalida");
            break;


    }
} while (opcao != 3);
