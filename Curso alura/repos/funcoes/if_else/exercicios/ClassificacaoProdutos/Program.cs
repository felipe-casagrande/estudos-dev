Console.Write("Digite o codigo do prouto (1 ou 2): ");
int tipoProduto = int.Parse(Console.ReadLine());

if (tipoProduto == 1)
{
    Console.WriteLine("Perecivel");
}else if(tipoProduto == 2)
{
    Console.WriteLine("Não perecivel");
}
else
{
    Console.WriteLine("Codigo invalido");
}