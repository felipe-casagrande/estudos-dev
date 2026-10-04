List<string> Alunos = new List<string> { "Ana", "Carlos", "Bianca", "João", "Marina" };
Console.WriteLine("Digite o nome de um aluno");
string nomeAluno = Console.ReadLine();
int indice = 0;
bool encontrado = false;

while(Alunos.Count >indice)
{
    if (nomeAluno == Alunos[indice])
    {
        encontrado = true;
        break;
    }
    indice++;
}
if (encontrado)
{
    Console.WriteLine($"{nomeAluno} encontrado na posição {indice}");
}
else
{
    Console.WriteLine("Aluno nao encontrado na lista");
}
