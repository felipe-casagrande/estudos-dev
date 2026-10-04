
using System.Text.Json.Serialization;

namespace Aula.Modelos;

internal class Musica
{
    [JsonPropertyName("song")]
    public string? Nome { get; set; }

    [JsonPropertyName("artist")]
    public string? Artista { get; set; }


    [JsonPropertyName("duration")]
    public int Duracao { get; set; }


    [JsonPropertyName("genre")]
    public string Genero { get; set; }

    public void ExibirDetalhesDaMusica()
    {
        Console.WriteLine($"Artista: {Artista}");
        Console.WriteLine($"Musica: {Nome}");
        Console.WriteLine($"Duraçao em segundos: {Duracao/1000}");
        Console.WriteLine($"Genero Musical: {Genero}");
    }

}
