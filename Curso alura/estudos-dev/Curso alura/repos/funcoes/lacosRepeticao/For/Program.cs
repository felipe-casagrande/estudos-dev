//for (int i = 0; i <= 10; i++)
//{
//    Console.WriteLine(i);
//}
//Console.WriteLine("A contagem chegou ao fim");

// código omitido

List<string> funcionarios = new List<string>
        {
            "João-Gerente-8500",
            "Maria-Analista de Sistemas-6200",
            "Carlos-Desenvolvedor-5500",
            "Ana-Designer-4800",
            "Pedro-Suporte Técnico-3900",
            "Fernanda-Coordenadora de Projetos-7300",
            "Ricardo-Contador-6000",
            "Juliana-RH-4500"
        };

// código omitido

for (int i = 0; i < funcionarios.Count; i++)
{
    var salario = funcionarios[i].Split("-")[2];
    var salarioInt = int.Parse(salario);
    if (salarioInt > 5000)
    {
        continue;
    }
    Console.WriteLine($"Dados do funcionário buscado: {funcionarios[i]}");
}



