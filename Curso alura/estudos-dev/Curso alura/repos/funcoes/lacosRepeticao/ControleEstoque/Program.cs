int estoque = 0;
int opcao = 0;
do
{
    Console.WriteLine("Deseja adicionar um produto ao estoque? (digite 0 para sair)");
    opcao = int.Parse(Console.ReadLine());
    if (opcao == 0)
    {
        Console.WriteLine("Obrigado por usar nosso sistema de estoque!");
    }
    else
    {
        Console.WriteLine($"Quantidade atual: {estoque}");
        Console.WriteLine("Qual a quantidade: ");
        estoque += int.Parse(Console.ReadLine());
    }
    
}while (opcao != 0);
