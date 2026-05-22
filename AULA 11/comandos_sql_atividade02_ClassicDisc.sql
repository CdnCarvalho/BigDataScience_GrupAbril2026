-- =========================================================
-- CRIAÇÃO DA TABELA

CREATE TABLE tb_musicas (

    id INT PRIMARY KEY AUTO_INCREMENT,
    faixa VARCHAR(150),
    artista VARCHAR(150),
    album VARCHAR(150),
    ano INT,
    duracao INT,
    compasso_musical INT,
    dancabilidade DECIMAL(5,3),
    energia DECIMAL(5,3),
    tom_musical INT,
    intensidade_sonora DECIMAL(6,3),
    modo INT,
    nivel_de_fala DECIMAL(6,4),
    acousticidade DECIMAL(6,4),
    instrumentalidade DECIMAL(10,7),
    presenca_ao_vivo DECIMAL(6,4),
    valencia_musical DECIMAL(5,3),
    tempo DECIMAL(6,3),
    popularidade INT
);




-- =========================================================
-- INSERT INTO

INSERT INTO tb_musicas (
    faixa,
    artista,
    album,
    ano,
    duracao,
    compasso_musical,
    dancabilidade,
    energia,
    tom_musical,
    intensidade_sonora,
    modo,
    nivel_de_fala,
    acousticidade,
    instrumentalidade,
    presenca_ao_vivo,
    valencia_musical,
    tempo,
    popularidade
)

VALUES (

    'Boogie Oogie Oogie',
    'A Taste Of Honey',
    'A Taste Of Honey',
    1978,
    245173,
    4,
    0.797,
    0.548,
    2,
    -9.228,
    0,
    0.0492,
    0.0401,
    0.0000105,
    0.0994,
    0.868,
    123.686,
    53
);




-- =========================================================
-- LOAD DATA INFILE
-- Inserindo o conteúdo do arquivo CSV na tabela
-- O arquivo musicas.csv precisa estar na pasta:
-- C:\\ProgramData\\MySQL\\MySQL Server 8.4\\Uploads\\
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.4\\Uploads\\ClassicDisc.csv'
INTO TABLE tb_musicas
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS

(
    faixa,
    artista,
    album,
    ano,
    duracao,
    compasso_musical,
    dancabilidade,
    energia,
    tom_musical,
    intensidade_sonora,
    modo,
    nivel_de_fala,
    acousticidade,
    instrumentalidade,
    presenca_ao_vivo,
    valencia_musical,
    tempo,
    popularidade
);