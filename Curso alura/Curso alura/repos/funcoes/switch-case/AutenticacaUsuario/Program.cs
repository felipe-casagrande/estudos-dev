Console.WriteLine("Digite seu nome");
string nome = Console.ReadLine();
string ADMIN_USER = "Admin";

if (nome == ADMIN_USER)
{
    Console.WriteLine($"Bem-vindo, {nome}!");

}
else
{
    Console.WriteLine("Usuario nao cadastrado.");
    Console.WriteLine("Opções disponíveis:\r\n[1] Cadastrar novo usuário\r\n[2] Acessar como convidado\r\n[3] Sair");
    int opcao = int.Parse(Console.ReadLine());
    switch (opcao)
    {
        case 1:
            Console.WriteLine($"Novo usuario {nome} cadastrado!");
            break;
        case 2:
            Console.WriteLine("Acesso concedido como usuario");
            break;
        case 3:
            Console.WriteLine("Saindo..");
            break;
        default:
            Console.WriteLine("Opçao invalida");
            break;

    }
}

