using System;

Console.WriteLine("Digite o codigo da recompensa: (DOBRAR, CURAR, OURO, ESPECIAL): ");
string recompensa = Console.ReadLine();

string mensagem = recompensa switch
{
    "DOBRAR" => "Você ganhou 2x EXP por 1 hora!",
    "CURAR" => "Poção de cura adquirida!",
    "OURO" => "+ 1000 moedas de ouro.",
    "ESPECIAL" => "Item lendário desbloqueado!.",
    _ => "Recompensa indisponivel"
};
Console.WriteLine(mensagem);