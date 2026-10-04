//Banda queen = new Banda("Queen");

//Album albumDoQueen = new Album("A nigth at the opera");


//Musica musica1 = new Musica(queen, "Love of my life")
//{
//    Duracao = 213,
//    Disponivel = true,
//};


//Musica musica2 = new Musica(queen, "Bohemian Rhapsody")
//{
//    Duracao = 354,
//    Disponivel = false,
//};

//albumDoQueen.AdicionarMusica(musica1);
//albumDoQueen.AdicionarMusica(musica2);
//queen.AdicionarAlbum(albumDoQueen);
//musica1.ExibirFichaTecnica();
//musica2.ExibirFichaTecnica();
//albumDoQueen.ExibirMusicasDoAlbum();
//queen.ExibirDiscografia();

Episodio ep1 = new Episodio(1,"Curso Alura",45);
ep1.AdicionarConvidados("Maria");
ep1.AdicionarConvidados("Marcelo");
 

Episodio ep2 = new Episodio(2, "Poo",50);
ep2.AdicionarConvidados("Marcos");
ep2.AdicionarConvidados("Flavia");

Podcast FlowAlura = new Podcast("Felipao", "FlowAlura");
FlowAlura.AdicionarEpisodio(ep1);
FlowAlura.AdicionarEpisodio(ep2);
FlowAlura.ExibirDetalhes();

