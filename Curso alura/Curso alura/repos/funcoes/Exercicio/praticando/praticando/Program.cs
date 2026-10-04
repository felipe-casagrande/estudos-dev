//int notaMedia = 4;

//if (notaMedia >=5)
//{
//    Console.WriteLine("Nota Suficiente para aprovação");

//}
//else
//{
//    Console.WriteLine("Reprovado");
//}

Dictionary<string, List<int>> Aluno = new Dictionary<string, List<int>>();

string nomeAluno = "Felipe";
Aluno[nomeAluno] = new List<int>();
Aluno[nomeAluno].Add(10);
Aluno[nomeAluno].Add(9);

string nomeAluno2 = "lara";
Aluno[nomeAluno2] = new List<int>();
Aluno[nomeAluno2].Add(2);
Aluno[nomeAluno2].Add(10);


foreach (var pessoa in Aluno)
    
{
    float soma = 0;
    foreach (int nota in pessoa.Value)
    {
        soma += nota;
    }

   double media = soma / Aluno.Values.Count;
   Console.WriteLine($"A media do aluno {pessoa.Key} é: { media}");
   
}
