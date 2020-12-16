-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 16-Dez-2020 às 20:48
-- Versão do servidor: 5.7.24
-- versão do PHP: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gymsystem`
--
CREATE DATABASE IF NOT EXISTS `gymsystem` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `gymsystem`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `alunos`
--

DROP TABLE IF EXISTS `alunos`;
CREATE TABLE IF NOT EXISTS `alunos` (
  `Matricula` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `CPF` varchar(11) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `modalidades` varchar(300) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `telefone_res` varchar(15) DEFAULT NULL,
  `telefone_celular` varchar(15) DEFAULT NULL,
  `data_nascimento` date DEFAULT NULL,
  `CEP` int(11) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `compl` varchar(10) DEFAULT NULL,
  `bairro` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `UF` varchar(4) DEFAULT NULL,
  `observacoes` varchar(500) DEFAULT NULL,
  `status` enum('','Ativo','Inativo') DEFAULT NULL,
  `imagem_aluno` varchar(350) DEFAULT NULL,
  `data_inclusao` datetime DEFAULT NULL,
  `data_atualizacao` datetime DEFAULT NULL,
  PRIMARY KEY (`Matricula`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `alunos`
--

INSERT INTO `alunos` (`Matricula`, `nome`, `CPF`, `email`, `modalidades`, `sexo`, `telefone_res`, `telefone_celular`, `data_nascimento`, `CEP`, `endereco`, `numero`, `compl`, `bairro`, `cidade`, `UF`, `observacoes`, `status`, `imagem_aluno`, `data_inclusao`, `data_atualizacao`) VALUES
(2, 'Luiza Bergman', '08428358060', 'bergamanlu@hotmail.com', NULL, 'F', '5132317002', '', NULL, NULL, 'Duque de Caxias, 500, Apto 40', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(3, 'Luiz Antonio Silva', '35999366097', 'antonio.silva@gmail.com', NULL, 'M', '5132311964', '', NULL, NULL, 'Praça Conde de Porto Alegre, 37, Apto 43', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(5, 'José dos Santos', '64822382036', 'j.santos@hotmail.com', NULL, 'M', '', '51997424588', NULL, NULL, 'Rua Coronel Genuíno, 422, 35', NULL, NULL, NULL, NULL, NULL, 'Hipertensão', NULL, NULL, NULL, NULL),
(6, 'Anita dos Santos', '79952872089', 'anita@hotmail.com', NULL, 'F', '', '997454586', NULL, NULL, 'Duque de Caixas, 81, 44', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(7, 'Jorge Barcellos', '40370912080', 'j.barcellos@gmail.com', NULL, 'M', '51 32128899', '', NULL, NULL, 'R. Riachuelo, 42, 88', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(8, 'Leonardo Silva', '59459217001', 'silva_leonardo@outlook.com', NULL, 'M', '32335656', '', NULL, NULL, 'R. dos Andradas, 285, 35', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(9, 'Luiza Lopes', '38090570020', 'llopes@hotmail.com', NULL, 'F', '32335656', '', NULL, NULL, 'R. dos Andradas, 285, 35', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL),
(10, 'Laura Paz', '70077462092', 'laura_paz@gmail.com', NULL, 'F', '', '', NULL, NULL, 'R. Riachuelo, 80, 23', NULL, NULL, NULL, NULL, NULL, '', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `modalidade`
--

DROP TABLE IF EXISTS `modalidade`;
CREATE TABLE IF NOT EXISTS `modalidade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `modalidade`
--

INSERT INTO `modalidade` (`id`, `nome`) VALUES
(1, 'Musculacao'),
(17, 'Judô'),
(3, 'Pilates'),
(4, 'Jiu-Jitsu'),
(5, 'Funcional'),
(6, 'Alongamento'),
(7, 'Crossfit'),
(8, 'Hit'),
(9, 'Caminhada'),
(10, 'Trilhas'),
(15, 'Testando'),
(16, 'Grupo de Corrida');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
