ContaBancaria conta = new ContaBancaria("78901-2", 1000.00);
conta.DepositarValor(500.00);

Console.WriteLine("Conta: " + conta.NumeroConta);
Console.WriteLine("Saldo atual: R$ " + conta.Saldo.ToString("F2"));
