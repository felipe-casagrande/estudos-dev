namespace desafio_interface;

internal class Circulo : IForma
{
    public double Raio { get; set; }
    public double CalcularArea()
    {
        return Math.PI*Math.Pow(Raio,2);  // Pi x Raio ao quaddrado
    }
    public double CalcularPerimetro()
    {
        return 2 * Math.PI * Raio;
    }
}

