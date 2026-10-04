class Filme
{
    public string Titulo {  get; set; }
    public int ClassificacaoEtaria {  get; set; }

    public Filme(string titulo, int classificacaoEtaria)
    {
        Titulo = titulo;
        ClassificacaoEtaria = classificacaoEtaria;
    }

    public bool PodeAssistir(int idadeUsuario)
    {
        if (idadeUsuario  >= ClassificacaoEtaria)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }


    public void ExibirResultado(int idadeUsuario)
    {
        if(idadeUsuario >= ClassificacaoEtaria)
        {
            Console.WriteLine($"Usuario com {idadeUsuario} pode assistir ao filme {Titulo}");
        }
        else
        {
            Console.WriteLine($"Usuario com {idadeUsuario} não pode assistir ao filme {Titulo}");
        }
    }
}