
Console.WriteLine("Digite o primeiro numero: ");
int primeiroNumero = int.Parse(Console.ReadLine());
Console.WriteLine("Digite o segundo numero: ");
int segundoNumero = int.Parse(Console.ReadLine());

Console.WriteLine("Digite a operação que deseja realizar (+,-,*,/");
string operacao = Console.ReadLine();



double? resultado = operacao switch
{
    "+" => primeiroNumero + segundoNumero,
    "-" => primeiroNumero - segundoNumero,
    "*" => primeiroNumero * segundoNumero,
    "/" => segundoNumero != 0 ? primeiroNumero / segundoNumero:null,   // se lê:  se o segundo numero for diferente de 0, faça 1°/2°, se for 0 vai dar nulo. Estrutura: condicao ? valorSeVerdadeiro : valorSeFalso
    _ => null
};


if(resultado == null)
{
    Console.WriteLine("Operação Invalida");
}
else
{
    Console.WriteLine(resultado);
}
    