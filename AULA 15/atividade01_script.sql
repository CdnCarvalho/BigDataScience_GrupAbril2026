-- EXEMPLOS INICIAIS
-------------------------------------------------------------------
-- EXEMPLO LIKE % %
SELECT * FROM cadastro_produtos
WHERE Produto LIKE '%tv%';

-- EXEMPLO BETWWEN
SELECT * FROM cadastro_produtos
WHERE `Preço Unitario` BETWEEN 50 AND 100;

-- BETWWEN DATAS
SELECT * FROM bd_vendas.tb_pedidos
WHERE data_pedido BETWEEN '2023-11-10' AND '2023-11-30';

-------------------------------------------------------------------


-- ATIVIDADE 1 – BÁSICO
-- 1. Mostrar todos os dados da tabela
SELECT * FROM materiais_construcao;

-- 2. Mostrar apenas produto e preço
SELECT produto, preco FROM materiais_construcao;




-- ATIVIDADE 2 – WHERE SIMPLES
-- 1. Mostrar apenas produtos da categoria "cimento"
SELECT * 
FROM materiais_construcao
WHERE categoria = 'cimento';

-- 2. Mostrar produtos com preço maior que 200
SELECT * 
FROM materiais_construcao
WHERE preco > 200;



-- ATIVIDADE 3 – AND / OR
-- 1. Produtos da categoria "agregado" com preço acima de 200
SELECT * 
FROM materiais_construcao
WHERE categoria = 'agregado'
AND preco > 200;

-- 2. Produtos vendidos mais que 3000 unidades E da categoria cimento
SELECT * 
FROM materiais_construcao
WHERE quantidade_vendida > 3000
AND categoria = 'cimento';

-- 3. Produtos do fornecedor "local" OU "votoran"
SELECT * 
FROM materiais_construcao
WHERE fornecedor = 'local'
OR fornecedor = 'votoran';



-- 4. Produtos da categoria "alvenaria" do fornecedor "olaria"
SELECT * 
FROM materiais_construcao
WHERE categoria = 'alvenaria'
AND fornecedor = 'olaria';

-- 4. Produtos com preço menor que 100 ordenados
SELECT * 
FROM materiais_construcao
WHERE preco < 100
ORDER BY preco;



-- ATIVIDADE 6 – LIKE
-- 1. Buscar produtos que contenham "cimento"
SELECT * 
FROM materiais_construcao
WHERE produto LIKE '%cimento%';

-- 2. Buscar produtos que contenham "areia"
SELECT * 
FROM materiais_construcao
WHERE produto LIKE '%areia%';


-------------------------------------------------------------------
-- EXEMPLO LIKE % %
SELECT * FROM cadastro_produtos
WHERE Produto LIKE '%tv%';

-- EXEMPLO BETWWEN
SELECT * FROM cadastro_produtos
WHERE `Preço Unitario` BETWEEN 50 AND 100;

-- BETWWEN DATAS
SELECT * FROM bd_vendas.tb_pedidos
WHERE data_pedido BETWEEN '2023-11-10' AND '2023-11-30';


