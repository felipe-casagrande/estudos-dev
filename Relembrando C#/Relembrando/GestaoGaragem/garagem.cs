using System;
using System.Collections.Generic;
using System.Text;

namespace GestaoGaragem
{
    public class Garagem
    {
        public string NomeProprietario { get; }
        public List<Veiculo> listaVeiculo = new List<Veiculo>();

        //METODO CONSTRUTOR, VAMOS INICIAR SO COM O NOME DO PROPRIETARIO E DEPOIS USAR O METODO DE ADICIONAR VEICULOS 
        public Garagem(string nomeProprietario)
        {
            NomeProprietario = nomeProprietario;
        }


        //METODOS
        public void adicionarVeiculo(Veiculo item)
        {
            listaVeiculo.Add(item);
        }

        public void RemoverVeiculo(string placaAserRemovida)
        {
            Veiculo veiculoEncontrado = null;

            foreach (Veiculo veiculo in listaVeiculo)
            {
                if (veiculo.Placa.Equals(placaAserRemovida, StringComparison.OrdinalIgnoreCase))
                {
                    veiculoEncontrado = veiculo;
                    break;
                }
            }
            if(veiculoEncontrado!= null)
            {
                listaVeiculo.Remove(veiculoEncontrado);
                Console.WriteLine($"Veiculo da placa {placaAserRemovida.ToUpper()} foi removido");
            }
            else
            {
                Console.WriteLine("Veiculo nao encontrado");
            }
        }



        public void ExibirEstoque()
        {
            Console.WriteLine($"{NomeProprietario}");
            foreach (var item in listaVeiculo)
            {
                Console.WriteLine($"{item.FichaTecnica}");
            }
            Console.WriteLine($"Total de veiculos: {listaVeiculo.Count}");
        }

        public double CalcularValorEstoque()
        {
            double soma = 0;
            foreach (Veiculo item in listaVeiculo)
            {
                soma += item.Preco;
            }
            return soma;
        }
    }


}
