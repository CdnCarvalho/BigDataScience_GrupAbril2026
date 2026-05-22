-- =========================================================
-- CRIAÇÃO DA TABELA

CREATE TABLE tb_loja_roupas (
    id INT PRIMARY KEY AUTO_INCREMENT,    
    descricao_produto VARCHAR(150),
    categoria VARCHAR(80),
    cor VARCHAR(50),
    tamanho VARCHAR(20),
    material VARCHAR(80),    
    preco_venda DECIMAL(10,2),
    custo_unitario DECIMAL(10,2),    
    quantidade_estoque INT,    
    ano_lancamento INT
);



-- =========================================================
-- INSERT INTO
INSERT INTO tb_loja_roupas (
    descricao_produto,
    categoria,
    cor,
    tamanho,
    material,
    preco_venda,
    custo_unitario,
    quantidade_estoque,
    ano_lancamento
)

VALUES (
    'Camiseta Oversized Basic',
    'Camisetas',
    'Preto',
    'M',
    'Algodao',
    89.90,
    35.50,
    120,
    2025
);


-- =========================================================
-- LOAD DATA INFILE

-- Inserindo o conteúdo do arquivo CSV na tabela
-- O arquivo loja_roupas.csv precisa estar na pasta:
-- C:\\ProgramData\\MySQL\\MySQL Server 8.4\\Uploads\\

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.4\\Uploads\\loja_roupas.csv'
INTO TABLE tb_loja_roupas
FIELDS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

(
    descricao_produto,
    categoria,
    cor,
    tamanho,
    material,
    preco_venda,
    custo_unitario,
    quantidade_estoque,
    ano_lancamento
);



-- NÃO PRECISA, porém comentar do comportamento autoincrement não continua na sequência exata geralmente no insert logo após o load
-- se quiser, precisa configurar
INSERT INTO tb_loja_roupas (descricao_produto, categoria, cor, tamanho, material, preco_venda, custo_unitario, quantidade_estoque, ano_lancamento)
VALUES
('Jaqueta Jeans Premium', 'Jaquetas', 'Azul', 'G', 'Jeans', 249.90, 120.00, 45, 2024),
('Calca Cargo Streetwear', 'Calcas', 'Verde Militar', '42', 'Sarja', 159.90, 70.00, 80, 2025);