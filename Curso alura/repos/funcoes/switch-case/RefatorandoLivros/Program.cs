//1: Ficção Científica
//2: Literatura Clássica
//3: Fantasia
//4: Romance
//5: Suspense / Mistério
//6: Não ficção
//7: Biografias / Memórias
//8: Distopia
//9: Infantojuvenil


Console.WriteLine("Digite o codigo do livro: ");
int codigoLivro = int.Parse(Console.ReadLine());


string mensagem = (codigoLivro/100) switch
{
    1 => "Ficção Científica",
    2 => "Literatura Clássica",
    3 => "Fantasia",
    4 => "Romance",
    5 => "Suspense / Mistério",
    6 => "Não ficção",
    7 => "Biografias / Memórias",
    8 => "Distopia",
    9 => "Infantojuvenil",
    _ => "Código não existente"
};
Console.WriteLine(mensagem);