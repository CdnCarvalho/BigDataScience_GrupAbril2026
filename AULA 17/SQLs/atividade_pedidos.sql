-- Tabela clientes
ALTER TABLE tb_clientes
MODIFY COLUMN codigo_cliente INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_cliente);

-- Tabela produtos
ALTER TABLE tb_produtos
MODIFY COLUMN codigo_produto INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_produto);

-- Tabela pedidos
ALTER TABLE tb_pedidos
MODIFY COLUMN codigo_pedido INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_pedido);

-- Tabela itens
ALTER TABLE tb_itens
MODIFY COLUMN codigo_item INT AUTO_INCREMENT,
ADD PRIMARY KEY (codigo_item);


-- CHAVE ESTRANGEIRA CLIENTE -> PEDIDO
ALTER TABLE tb_pedidos
ADD CONSTRAINT fk_tb_pedidos_clientes
FOREIGN KEY (codigo_cliente) REFERENCES tb_clientes(codigo_cliente);


-- CHAVE ESTRANGEIRA ITENS -> PEDIDO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_pedidos
FOREIGN KEY (codigo_pedido) REFERENCES tb_pedidos(codigo_pedido);


-- CHAVE ESTRANGEIRA ITENS -> PRODUTO
ALTER TABLE tb_itens
ADD CONSTRAINT fk_tb_itens_produtos
FOREIGN KEY (codigo_produto) REFERENCES tb_produtos(codigo_produto);
-- ---------------------------------------------------

-- Liste os pedidos feitos por clientes que moram em São Paulo.
SELECT 
tb_clientes.nome, 
tb_clientes.sobrenome, 
tb_pedidos.codigo_pedido, 
tb_pedidos.data_pedido,
tb_produtos.produto,
tb_pedidos.valor
FROM tb_pedidos
JOIN tb_clientes ON tb_pedidos.codigo_cliente = tb_clientes.codigo_cliente
JOIN tb_itens ON tb_itens.codigo_pedido = tb_pedidos.codigo_pedido
JOIN tb_produtos ON tb_produtos.codigo_produto = tb_itens.codigo_produto
WHERE tb_clientes.cidade = 'São Paulo';



