abstract class FormaGeometrica
{ 
    public abstract double Calcular_Area();
    public abstract double Calcular_Perimetro();
}

class Quadrado : FormaGeometrica
{
    public double lado {  get; set; }
    public override double Calcular_Area()
    {
        return lado * lado;
    }
    public override double Calcular_Perimetro()
    {
        return 4 * lado;
    }
}
class Circulo : FormaGeometrica
{
    public double Raio { get; set; }

    public override double Calcular_Area()
    {
        return Math.PI * Raio * Raio;
    }

    public override double Calcular_Perimetro()
    {
        return 2 * Math.PI * Raio;
    }
}

class Triangulo : FormaGeometrica
{
    public double Base { get; set; }
    public double Altura { get; set; }

    public override double Calcular_Area()
    {
        return 0.5 * Base * Altura;
    }

    public override double Calcular_Perimetro()
    {
        // Considerando um triângulo genérico
        return Base + Altura + Math.Sqrt(Base * Base + Altura * Altura);
    }
}

