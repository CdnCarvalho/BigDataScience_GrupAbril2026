-- REMOVER CHAVE ESTRANGEIRA
ALTER TABLE tb_pedidos
DROP FOREIGN KEY fk_tb_pedidos_clientes;

-- REMOVER CHAVE PRIMARIA
ALTER TABLE clientes
ADD PRIMARY KEY (codigo_cliente);
-- Obs: Se houver relacionamento com outras tabelas, é preciso remover a chave estrangeira primeiro.


-- -------------------------------------------------------
-- Alterar a coluna RG de BIGINT para texto
ALTER TABLE clientes
MODIFY COLUMN rg VARCHAR(20);

-- Alterar a coluna id_cliente de texto para inteiro
ALTER TABLE clientes
MODIFY COLUMN id_cliente INT;


DESCRIBE clientes;

SHOW COLUMNS FROM clientes;

