namespace desafio6;

internal class LinqPreco
{
    public static double Media(List<Produto> produtos)

    {
        var media = produtos.Average(p => p.Preco);
        return media;
    }
}
