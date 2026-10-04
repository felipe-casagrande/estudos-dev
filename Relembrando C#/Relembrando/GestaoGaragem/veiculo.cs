using System;
using System.Collections.Generic;
using System.Text;

namespace GestaoGaragem
{
    public class Veiculo
    {
    //declarando as propriedades que minha classe vai ganhar
    public string Modelo { get; }
        public string Marca { get; }
        public int Ano { get; }
        public double Preco { get; }
        public string FichaTecnica { get; set; }
        public string Placa {  get;}

        // metodo construtor
        public Veiculo(string modelo, string marca, int ano, double preco, string placa)
        {
            Modelo = modelo;
            Marca = marca;
            Ano = ano;
            Preco = preco;
            Placa = placa.ToUpper();

            FichaTecnica = $"{Marca}, {Modelo}, {Ano}, {Preco}";
        }

    }
}
