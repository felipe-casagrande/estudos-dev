//int contador = 0;

//while (contador >= 1)
//{
//    Console.WriteLine(contador);
//    contador--;
//}
//Console.WriteLine("A contagem chegou ao fim");


//int contador = 0;

//do
//{
//    Console.WriteLine(contador);
//    contador--;
//} while (contador >= 1);
//    Console.WriteLine("A contagem chegou ao fim");


// código omitido
int opcao;
do
{
    Console.WriteLine("\nMENU:");
    Console.WriteLine("1 - Ver produtos");
    Console.WriteLine("2 - Fazer pedido");
    Console.WriteLine("0 - Sair");
    Console.Write("Escolha uma opção: ");
    opcao = int.Parse(Console.ReadLine());
    switch (opcao)
    {
        case 1:
            Console.WriteLine("Mostrando produtos…");
            break;
        case 2:
            Console.WriteLine("Pedido realizado!");
            break;
        case 0:
            Console.WriteLine("Saindo…");
            break;
        default:
            Console.WriteLine("Opção inválida!");
            break;
    }  

} while (opcao != 0);
