CREATE TABLE Veiculos(
	veiculo_id SERIAL PRIMARY KEY,
	modelo VARCHAR(100) NOT NULL,
	placa VARCHAR(20) NOT NULL,
	categoria VARCHAR(20) NOT NULL
);

CREATE TABLE Alunos(
	aluno_id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	cpf VARCHAR(14) NOT NULL,
	telefone VARCHAR(20) NOT NULL,
	email VARCHAR(100) NOT NULL
);

CREATE TABLE Instrutores(
	instrutor_id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	cnh VARCHAR(20) NOT NULL,
	categoria_cnh VARCHAR(10) NOT NULL
);

CREATE TABLE Aulas(
	aula_id SERIAL PRIMARY KEY,
	data_hora TIMESTAMP NOT NULL,
	aluno_id INT NOT NULL REFERENCES Alunos(aluno_id),
	instrutor_id INT NOT NULL REFERENCES Instrutores(instrutor_id),
	veiculo_id INT NOT NULL REFERENCES Veiculos(veiculo_id),
	status_aula VARCHAR(40) NOT NULL
);
