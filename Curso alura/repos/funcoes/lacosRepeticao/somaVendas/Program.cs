
double vendas = 0;
double valorVenda;
do
{
    Console.WriteLine("Digite o valor da venda ou 0 para encerrar");
    valorVenda = double.Parse(Console.ReadLine());
    vendas += valorVenda;
} while (valorVenda != 0);
Console.WriteLine($"Numero de venda do dia {vendas}");

