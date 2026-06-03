-- CHAVE PRIMÁRIA
ALTER TABLE tb_usuarios
MODIFY COLUMN id_usuario INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_usuario);

ALTER TABLE tb_livros
MODIFY COLUMN id_livro INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_livro);

ALTER TABLE tb_alugados
MODIFY COLUMN id_aluguel INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_aluguel);

ALTER TABLE tb_itens_alugados
MODIFY COLUMN id_item INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_item);



-- CHAVE ESTRANGEIRA
ALTER TABLE tb_alugados
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario) REFERENCES tb_usuarios(id_usuario);

ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_aluguel
FOREIGN KEY (id_aluguel) REFERENCES tb_alugados(id_aluguel);

ALTER TABLE tb_itens_alugados
ADD CONSTRAINT fk_livro
FOREIGN KEY (id_livro) REFERENCES tb_livros(id_livro);