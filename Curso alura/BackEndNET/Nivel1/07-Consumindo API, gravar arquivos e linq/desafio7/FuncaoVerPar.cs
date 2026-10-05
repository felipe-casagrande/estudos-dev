namespace desafio7;

internal class FuncaoVerPar
{
    public static List<int> Pares(List<int> Lista)
    {
        var par = Lista.Where(n => n % 2  == 0).ToList();
        return par;
    }
}
