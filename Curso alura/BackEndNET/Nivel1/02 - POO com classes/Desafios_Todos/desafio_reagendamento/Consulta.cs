class Consulta
{
    public string NomePaciente { get; set; }
    public string NomeMedico { get; set; }
    public DateTime DataConsulta { get; set; }
    private bool FoiReagendada = false;

    public Consulta(string nomePaciente, string nomeMedico,DateTime dataConsulta)
    {
        NomePaciente = nomePaciente;
        NomeMedico = nomeMedico;
        DataConsulta = dataConsulta;
        FoiReagendada =false;
    }
    public void Reagendar(DateTime novaData)
    {
        DataConsulta = novaData;
        FoiReagendada =true;
    }
    public void ExibirResumo()
    {
        Console.WriteLine($"Consulta maracada com o {NomeMedico} para o paciente {NomePaciente}");
        if (FoiReagendada)
        {
            Console.WriteLine($"Nova data {DataConsulta.ToString("dd/MM/yyyy")}");
        }
        else
        {
            Console.WriteLine("Data: " + DataConsulta.ToString("dd/MM/yyyy"));
        }
        Console.WriteLine();
    }
}
