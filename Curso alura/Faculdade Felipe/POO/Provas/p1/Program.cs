using System;

namespace prova_felipe
{
    public class Funcionario
    {
        public string nome {  get; set; }
        public string cpf { get; set; }
        public double salario { get; set; }

        public Funcionario(string n, string c, double s)
        {
            nome = n;
            cpf = c;
            salario= s;
        }
        public void ApresentarDados() 
        {
            Console.WriteLine($"Nome: {nome}" );
            Console.WriteLine($"CPF: {cpf}");
            Console.WriteLine($"Salario: R$ {salario}");
        }
    }
    public class Program
    {
        public static void Main(string[] args) 
        {
            Funcionario f1 = new Funcionario("Zé da manga","12345678901", 3500.75);
            f1.ApresentarDados();
        }
    }
}