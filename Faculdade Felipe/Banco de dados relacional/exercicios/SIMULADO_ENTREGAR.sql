-- Essa tabela atualmente vem varios defeitos--
--redundancia:
--Anomilias de exclusao e etc: Se quiser excluir um pedido, e caso o cliente so tenha feito esse pedido, tambem vai exlcuir o cliente.
-- Para cadastrar um cliente, tambem tem que cadastrar uma venda, produto, etc
-- ou seja, tudo esta dependente de tudo, e iremos separar para ficar dentro da estrutura 3nf


CREATE TABLE Clientes(
	cliente_id SERIAL PRIMARY KEY,
	nome_cliente VARCHAR(100) NOT NULL,
	cidade VARCHAR(100) NOT NULL
);

CREATE TABLE Produtos(
	produto_id SERIAL PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	categoria VARCHAR(30) NOT NULL,
	preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE Pedidos(
	pedido_id SERIAL PRIMARY KEY,
	cliente_id INT REFERENCES Clientes(cliente_id),
	data_pedido DATE NOT NULL,
	status_entrega VARCHAR(30) NOT NULL
);

CREATE TABLE Itens_pedidos(
	produto_id INT REFERENCES Produtos(produto_id),
	pedido_id INT REFERENCES Pedidos(pedido_id),
	preco DECIMAL(10,2) NOT NULL,
	quantidade INT NOT NULL,
	PRIMARY KEY(produto_id,pedido_id)
-- aqui em itens_pedidos eu tambem coloco o preco pois aqui fica como--
--um historico da venda, se eu mudar o preco do produto amanha, nao vai mudar o preco do produto aqui na venda passada.
);
--Questao 2

INSERT INTO Clientes(nome_cliente,cidade)
VALUES
('Zé da Manga','Saquarema'),
('Goku da Titi','Araruama'),
('Pandora da Destruição','Bacaxá'),
('Juvenal do Mobral','Cabo Frio'),
--meu cadastro
('Felipe Casagrande','Saquarema');

INSERT INTO Produtos(nome_produto,categoria,preco)
VALUES
('Sanduiche Natural','Lanche',12.00),
('Suco de Laranja','Bebida',7.50),
('Bolo de Chocolate','Sobremesa',8.00),
('Café Expresso','Bebida',5.00);

INSERT INTO Pedidos(cliente_id,data_pedido,status_entrega)
VALUES
(1,'2025-03-10','Entregue'),
(2,'2025-03-10','Pendente'),
(1,'2025-03-11','Entregue'),
(3,'2025-03-12','Cancelado'),
(4,'2025-03-12','Entregue'),
-- MEU PEDIDO E DEPOIS O PEDIDO PENDENTE DA QUESTAO 2
(5,'2025-03-12','Entregue'),
(4,'2025-03-13','Pendente');


INSERT INTO Itens_pedidos(produto_id,pedido_id,preco,quantidade)
VALUES
(1,1,12.00,2),
(2,2,7.50,1),
(3,3,8.00,3),
(1,4,12.00,1),
(4,5,5.00,2),
(4,6,5.00,2),
(3,7,8.00,1);

--QUESTAO 3
--A)
UPDATE Clientes
SET cidade = 'Rio de janeiro'
WHERE nome_cliente = 'Juvenal do Mobral'

--B)A restriçao diz que para remover um, primeiro temos que remover seus descendentes

--entao primeiro a gente tira ele em Itens pedidos e depois na tabela pedidos

DELETE FROM Itens_pedidos
WHERE pedido_id = 4

DELETE FROM Pedidos
WHERE pedido_id = 4
SELECT * FROM Pedidos


-- QUESTAO 4
-- Aqui irei selecionar o id do cliente e fazer um count
--de forma simples, coloque o numero do id e retorna as vezes que ele fez um pedido.
--A)
SELECT COUNT(*)
FROM Pedidos
WHERE cliente_id = 1

--B)
SELECT 
	SUM(preco*quantidade)
FROM Pedidos
JOIN Itens_pedidos ON Itens_pedidos.pedido_id = Pedidos.pedido_id
WHERE Pedidos.status_entrega = 'Entregue'


--QUESTAO 5

SELECT 
	Clientes.cliente_id,
	nome_cliente,
	cidade,
	Pedidos.pedido_id,
	data_pedido,
	Produtos.produto_id,
	nome_produto,
	categoria,
	quantidade,
	status_entrega
FROM Clientes
JOIN Pedidos ON Pedidos.cliente_id = Clientes.cliente_id
JOIN Itens_pedidos ON Pedidos.pedido_id = Itens_pedidos.pedido_id
JOIN Produtos ON Produtos.produto_id = Itens_pedidos.produto_id
	


CREATE DATABASE SIMULADO_ANTES