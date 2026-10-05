-- REDUNDANCIA: toda vez iria ter que ficar colocando os dados do cliente
--  Outros problemas como nao ter como cadastrar um produto sem fazer um pedido
-- Se apagar um pedido e a pessoa so tiver ele, tambem vai remover o cadastro dela
-- repetiçao de informacoes desnecessarias



--QUESTAO 1--
CREATE TABLE Clientes(
	cliente_id SERIAL PRIMARY KEY,
	nome_cliente VARCHAR(100) NOT NULL,
	cpf VARCHAR(14) NOT NULL,
	email VARCHAR(100) NOT NULL
);

CREATE TABLE Produtos(
	produto_id SERIAL PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE Pedidos(
	pedido_id SERIAL PRIMARY KEY,
	cliente_id INT REFERENCES Clientes(cliente_id),
	data_pedido DATE NOT NULL
);

CREATE TABLE Itens_pedidos(
	pedido_id INT REFERENCES Pedidos(pedido_id),
	produto_id INT REFERENCES Produtos(produto_id),
	preco DECIMAL(10,2) NOT NULL,
	quantidade INT NOT NULL,
	total_pedido DECIMAL(10,2) GENERATED ALWAYS  AS (preco*quantidade) STORED,
	PRIMARY KEY (pedido_id,produto_id)
);

--questao 2
INSERT INTO Clientes (cliente_id, nome_cliente, cpf, email)
VALUES
(1, 'João Silva', '12345678901', 'joao@email.com'),
(2, 'José da Silva', '12345678910', 'jose@email.com'),
(3, 'Maria Souza', '98765432109', 'maria@email.com'),
(4, 'Felipe Casagrande', '11122233344', 'felipe@email.com'),
(5, 'Ana Santos', '55566677788', 'ana@email.com');

INSERT INTO Produtos (produto_id, nome_produto, preco)
VALUES
(1, 'Notebook Dell', 5200.00),
(2, 'Mouse Wireless', 120.00),
(3, 'Teclado Mecânico', 250.00),
(4, 'Notebook Lenovo', 3500.00),
(5, 'Mouse Wireless G2', 135.00),
(6, 'Teclado Mecânico G2', 265.00),
(7, 'Monitor 24 Polegadas', 900.00),
(8, 'Headset Gamer', 300.00);


INSERT INTO Pedidos (pedido_id, cliente_id, data_pedido)
VALUES
(1, 1, '2023-05-10'),
(2, 2, '2023-05-10'),
(3, 3, '2023-05-10'),
(4, 1, '2023-05-10'),
(5, 2, '2023-05-10'),
(6, 3, '2023-05-11'),
(7, 4, '2023-05-12'),
(8, 5, '2023-05-12');

INSERT INTO Itens_pedidos (pedido_id, produto_id, preco, quantidade)
VALUES
(1, 1, 5200.00, 2),
(2, 2, 120.00, 1),
(3, 3, 250.00, 3),
(4, 4, 3500.00, 1),
(5, 5, 135.00, 3),
(6, 6, 265.00, 2),
(7, 7, 900.00, 1),
(8, 8, 300.00, 2);

--questao 3
UPDATE Clientes
SET email ='novoemailfelipe@email.com'
WHERE nome_cliente = 'Felipe Casagrande';

UPDATE Produtos
SET nome_produto = 'Headset Gamer Boladao'
WHERE nome_produto = 'Headset Gamer'

UPDATE Pedidos
SET data_pedido = '2023-05-20'
WHERE pedido_id = 8;

UPDATE Itens_pedidos
SET quantidade = 3
WHERE pedido_id = 2

DELETE FROM Itens_pedidos
WHERE pedido_id =7;

DELETE FROM Pedidos
WHERE pedido_id = 7;

DELETE FROM Produtos
WHERE produto_id= 7

DELETE FROM Clientes
WHERE cliente_id = 4 -- removi logo o meu, mas fiz assim pra facilitar e fazer uma escadinha.

-- questao 4
--primeiro caso
SELECT COUNT(*)
FROM Itens_pedidos
JOIN Pedidos ON Pedidos.pedido_id = Itens_pedidos.pedido_id
WHERE Pedidos.cliente_id = 1

--segundo caso

SELECT 
	SUM(preco*quantidade)
FROM Pedidos
JOIN Itens_pedidos ON Pedidos.pedido_id = Itens_pedidos.pedido_id
WHERE data_pedido = '2023-05-10'
-- caso a data fosse alterada o resultado seria diferente, tambem pode ser feito apartir de determinado data, usando >=


--questao 5

SELECT
	Pedidos.pedido_id,
	Clientes.cliente_id,
	nome_cliente,
	cpf,
	email,
	Produtos.produto_id,
	
	data_pedido,
	nome_produto,
	Itens_pedidos.preco,
	quantidade,
	total_pedido
FROM Clientes
JOIN Pedidos ON Pedidos.cliente_id = Clientes.cliente_id
JOIN Itens_pedidos ON Pedidos.pedido_id = Itens_pedidos.pedido_id
JOIN Produtos ON Produtos.produto_id = Itens_pedidos.produto_id
ORDER BY Pedidos.pedido_id;