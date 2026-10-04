class Funcionario
{
    public string Nome {  get; set; }
    public string Cargo {  get; set; }
    
    public Funcionario(string nome, string cargo)
    {
        Nome = nome;
        Cargo = cargo;
    }

    public void Promover(string novoCargo)
    {
        if(novoCargo.Equals(Cargo, StringComparison.OrdinalIgnoreCase))
        {
            Console.WriteLine($"o funcionario {Nome} já ocupa o cargo {Cargo}");
        }
        else
        {
            Cargo = novoCargo;
            Console.WriteLine($"O funcionario {Nome} foi promovido para o cargo {Cargo}");
        }
    }
}