
SELECT * FROM cadastro_produtos;

SELECT Produto, Marca FROM cadastro_produtos;

SELECT * FROM cadastro_produtos
WHERE Marca = 'Logitech';


SELECT * FROM cadastro_produtos
WHERE `Preço Unitario` > 20
ORDER BY `Preço Unitario` ASC; -- Descendente DESC

SELECT * FROM cadastro_produtos
WHERE Marca = 'Hashtag'
AND `Preço Unitario` <  25;
-- ORDER BY `Preço Unitario`;

SELECT * FROM cadastro_produtos
WHERE `tipo do produto` = 'Mouse'
AND (`marca` = 'Logitech' OR `marca` = 'Multilaser');


SELECT * FROM cadastro_produtos
WHERE Produto LIKE '%tv%';

/* 
NÃO ABORDAR AINDA
SELECT * 
FROM cadastro_produtos
WHERE `Observação` IS NOT NULL
AND `Observação` != '';
*/

