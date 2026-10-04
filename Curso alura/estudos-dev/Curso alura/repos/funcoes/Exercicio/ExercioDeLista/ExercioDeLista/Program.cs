//List<string> bandasFavoritas = new List<string>();
//bandasFavoritas.Add("u2");
//bandasFavoritas.Add("Ze da manga");
//Console.WriteLine("Minhas bandas favoritas sao");

//foreach (string banda in bandasFavoritas)
//{
//    Console.WriteLine(banda);
//}
//Console.WriteLine("Agora com for normal");
//for  (int i = 0; i < bandasFavoritas.Count; i++)
//{
//    Console.WriteLine($"banda: {bandasFavoritas[i]}");
//}




List<int> Numeros = new List<int> {1,2,3,4,5,6,7,8,9};

int Soma = 0;

for (int i = 0; i < Numeros.Count; i++)
{
    Soma += Numeros[i];

}
Console.WriteLine(Soma);