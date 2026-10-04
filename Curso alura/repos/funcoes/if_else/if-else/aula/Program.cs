/*bool conexaoAtiva = false;   
if (conexaoAtiva)
{
    Console.WriteLine("iniciando o jogo");
}
else
{
    Console.WriteLine("Voce perdeu sua conexao");
}
*/

double valorCompra = 250.00;
bool clienteVip = false;
if (valorCompra > 300.00 || clienteVip)
{
    double desconto = valorCompra * 0.1;
    Console.WriteLine($"Voce ganhou {desconto} reais em desconto!");
} else if (valorCompra > 200.00)
{
    Console.WriteLine("Parabêns! Você ganhou um brinde!!");
}
else
{
    double diferenca = 300 - valorCompra;
    Console.WriteLine($"Faltam {diferenca} reais para voce ganhar desconto na sua compra");


}