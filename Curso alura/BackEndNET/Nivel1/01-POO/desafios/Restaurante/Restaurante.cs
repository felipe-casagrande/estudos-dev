class Restaurante
{
    public List<Mesa> Mesas {  get; set; } = new List<Mesa>();
    public Cardapio Cardapio { get; set; } = new Cardapio();

    public Mesa AbrirMesa(int numero)
    {
        Mesa mesa = new Mesa();
        mesa.Numero = numero;
        Mesas.Add(mesa);
        return mesa;
    }

    public Mesa BuscarMesa(int numero)
    {
        foreach (var mesa in Mesas)
        {
            if (mesa.Numero == numero)
            {
                return mesa;
            }
        }
        return null;
    }
    public void FecharMesa(int numero)
    {
        var mesa = BuscarMesa(numero);

        if (mesa != null)
            Mesas.Remove(mesa);
    }

}