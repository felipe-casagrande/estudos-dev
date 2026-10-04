decimal salarioAtual = 1500;
decimal percentualAumento = 10;

decimal novoSalario = salarioAtual + (salarioAtual * percentualAumento / 100);
Console.WriteLine(novoSalario.ToString("F2"));