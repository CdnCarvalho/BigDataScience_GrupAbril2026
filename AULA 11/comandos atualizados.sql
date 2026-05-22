-- para saber se o mysql está instalado e qual versão, digite o seguinte comando no prompt de comando do windows:
mysql --version

-- Para conectar no mysql, digite o seguinte comando no prompt de comando do windows:
-- -u informa que root é o nome do usuário e -p para pedir a senha
-- a senha será pedida, somente depois de teclar enter
mysql -u root -p  

-- Logado
-- Após logar no MySQL, o terminal ficará diferente. Já não é mais o prompt de comando do windows, mas sim o prompt do MySQL



-- Para criar um banco de dados, digite o seguinte comando no MySQL, onde bd_aula11 
-- é o nome do banco de dados que você quer criar:
-- OBS: Para finalizar os comandos, ao témino use ;
CREATE DATABASE bd_aula11;


-- Para selecionar o banco de dados atual que você quer usar, digite:
USE bd_aula11;


-- Criar uma Tabela para o nosso exemplo
CREATE TABLE tb_produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(255),
    preco DECIMAL(10, 2),
    vendidos INT
    );


-- P/ Inserir dados na Tabela (não chegamos a utilizar)
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Mouse Logitech MX Master 4', 700.00, 82);


INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Mouse Gamer Redragon Cobra', 149.90, 120),
('Teclado Mecânico HyperX Alloy', 399.90, 65),
('Monitor AOC 24 Polegadas', 899.00, 34);



-- COMANDO PARA CARREGAR OS ARQUIVOS CSV
-- Inserindo o conteúdo do arquivo.csv na tabela. Os diretórios nos caminhos precisam ser separados com duas '\\'
-- O arquivo CSV precisa ser colocado na pasta C:\ProgramData\MySQL\MySQL Server 8.4\Uploads\
-- LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 9.7\\Uploads\\base1.csv'  -- caminho do arquivo CSV base1.csv 
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.4\\Uploads\\base1.csv'  -- caminho do arquivo CSV base1.csv 
INTO TABLE tb_produtos       -- nome da tabela que será inserido os dados
FIELDS TERMINATED BY ';'     -- define o caractere, que separa as colunas no CSV
OPTIONALLY ENCLOSED BY '"'   -- define que os textos estão entre aspas, se aparecer um nome com vígula, ele não confunde
LINES TERMINATED BY '\n'     -- define a quebra de linha utilizada no arquivo
IGNORE 1 ROWS                -- ignora a primeira linha do arquivo
(produto, preco, vendidos)  -- colunas da tabela que receberão os dados do CSV
;

-- Mostrando todo conteúdo da tabela
SELECT * FROM tb_produtos;
-- ---------------------------------------------------------------------------------------------------------------------------



-- ===========================================================================================================================
-- ESTE TRECHO É EXPLICATIVO:

-- Os comandos LOAD DATA INFILE e LOAD DATA LOCAL INFILE
-- são utilizados para importar dados de arquivos externos,
-- como arquivos .csv, para dentro das tabelas do MySQL.

-- Em muitas instalações do MySQL, a importação pode ser bloqueada
-- por questões de segurança. Isso acontece devido ao parâmetro
-- secure_file_priv configurado no arquivo my.ini.

-- Esse parâmetro limita os diretórios que o MySQL pode acessar
-- para leitura de arquivos durante a importação.

-- Quando o secure_file_priv está definido, normalmente o MySQL
-- só permite importar arquivos que estejam dentro do diretório configurado.

-- Nesse caso, é necessário:
-- 1. localizar o arquivo my.ini
-- 2. configurar o parâmetro secure_file_priv
-- 3. definir um diretório permitido para importação
-- 4. reiniciar o serviço do MySQL

-- Exemplo:
-- secure_file_priv="C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/"

-- Após isso, os arquivos .csv devem ser colocados
-- dentro desse diretório para que a importação funcione corretamente.

-- Já no XAMPP, o MySQL normalmente vem configurado
-- de forma mais permissiva, permitindo importar arquivos
-- de diferentes diretórios sem necessidade de configurar
-- o secure_file_priv.

-- Apesar de facilitar os testes e as aulas,
-- isso pode representar um risco de segurança,
-- pois permite maior acesso do MySQL aos arquivos do sistema operacional.



-- --------------------------------------------------------------------
-- Roteiro para estes casos:
-- entrar no MySQL
mysql -u root -p

-- verificar se a importação local de arquivos está habilitada
SHOW VARIABLES LIKE 'local_infile';

-- Saída esperada:
-- local_infile | ON  -> habilitada
-- local_infile | OFF -> desabilitada


-- habilitar a importação local, caso esteja OFF
SET GLOBAL local_infile = 1;
-- após executar este comando, o esperado é que o parâmetro local_infile fique como ON


-- verificar o diretório permitido para importação de arquivos
SHOW VARIABLES LIKE 'secure_file_priv';

-- saída esperada no Windows:
-- secure_file_priv | C:\\ProgramData\\MySQL\\MySQL Server 9.7\\Uploads\\
-- Esse diretório indica a partir de onde os arquivos .csv
-- devem estar, para que o LOAD DATA INFILE funcione.


-- sair do MySQL atual
exit


-- entrar novamente permitindo LOCAL INFILE
mysql --local-infile -u root -p

--  Seguir o fluxo normal de trabalho para o LOAD DATA INFILE que é o próximo passo a passo...
-- ---------------------------------------------------------------------------------------


-- INSERIR DADOS USANDO PYTHON
-- ======================================================
-- Inserir dados na Tabela usando o Python
-- INSERT para 1 produto
inserir_sql_um = """
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Fone de Ouvido JBL Tune 510BT', 299.00, 120);
"""

-- Para inserir
inserir_sql = """
INSERT INTO tb_produtos (produto, preco, vendidos) VALUES
('Smartphone Samsung Galaxy A15', 1299.00, 85),
('Notebook Dell Inspiron 15', 3499.00, 28),
('Smart TV LG 50 4K', 2799.00, 41);
"""
-- ======================================================



