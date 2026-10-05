using Aula.Modelos;
using System.Text.Json;
using System.Text.Json.Nodes;
using Aula.Filtros;

using (HttpClient client = new HttpClient())
{

    try
    {
        string resposta = await client.GetStringAsync("https://guilhermeonrails.github.io/api-csharp-songs/songs.json");
        var musicas = JsonSerializer.Deserialize<List<Musica>>(resposta)!;
        //foreach (var musica in musicas)
        //{
        //    Console.WriteLine(musica.Nota);
        //}
        musicas[0].ExibirDetalhesDaMusica();
        LinqFilterTonalidade.FiltrarMusicaPorTonalidade(musicas);
        //LinqFilter.FiltrarTodosOsGenerosMusicais(musicas);
        //LinqOrder.ExibirListaDeArtistasOrdenados(musicas);
        //LinqFilter.FiltrarArtistaPorGeneroMusica(musicas,"rock");
        //LinqFilterMusica.MusicasDeUmArtista(musicas, "Green Day");
        //var musicasPreferidasDoDaniel = new MusicasPreferidas("Felipe");
        //musicasPreferidasDoDaniel.AdicionarMusicasFavoritas(musicas[1]);
        //musicasPreferidasDoDaniel.AdicionarMusicasFavoritas(musicas[377]);
        //musicasPreferidasDoDaniel.AdicionarMusicasFavoritas(musicas[4]);
        //musicasPreferidasDoDaniel.AdicionarMusicasFavoritas(musicas[6]);
        //musicasPreferidasDoDaniel.AdicionarMusicasFavoritas(musicas[1467]);

        //musicasPreferidasDoDaniel.ExibirMusicasFavoritas();

        var musicasPreferidasDaLara = new MusicasPreferidas("Lara");
        musicasPreferidasDaLara.AdicionarMusicasFavoritas(musicas[637]);
        musicasPreferidasDaLara.AdicionarMusicasFavoritas(musicas[4]);
        musicasPreferidasDaLara.AdicionarMusicasFavoritas(musicas[6]);
        musicasPreferidasDaLara.AdicionarMusicasFavoritas(musicas[5]);
        musicasPreferidasDaLara.AdicionarMusicasFavoritas(musicas[1500]);

        musicasPreferidasDaLara.ExibirMusicasFavoritas();

        musicasPreferidasDaLara.GerarArquivoJson();
    }

    catch (Exception ex)
    {
        Console.WriteLine($"Temos um problema: {ex.Message}");
    }
    
}