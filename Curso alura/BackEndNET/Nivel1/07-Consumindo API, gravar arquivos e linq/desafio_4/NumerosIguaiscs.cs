namespace desafio_4;
internal class NumerosIguaiscs
{   
    public static void NumerosUnicos(List<int>numerosFuncao)
    {
        var numeros1 = numerosFuncao.Where(n => numerosFuncao.Count(x => x == n)==1);
        foreach (var numeros in numeros1)
        {
            Console.WriteLine(numeros);
        }
    }
}
