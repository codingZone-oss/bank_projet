-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28-Out-2025 às 14:45
-- Versão do servidor: 10.4.28-MariaDB
-- versão do PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `bank_bd`
--
CREATE DATABASE IF NOT EXISTS `bank_bd` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `bank_bd`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `acount_access`
--

CREATE TABLE `acount_access` (
  `cod` int(11) NOT NULL,
  `balance` float NOT NULL,
  `deposit_balance` float NOT NULL,
  `draw_money_balance` float NOT NULL,
  `name_transfer` varchar(20) NOT NULL,
  `balance_transfer` float NOT NULL,
  `acount_number_transfer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `add_client`
--

CREATE TABLE `add_client` (
  `cod` int(11) NOT NULL,
  `date1` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `cod_client` int(11) NOT NULL,
  `cod_worker` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `add_repartition_worker`
--

CREATE TABLE `add_repartition_worker` (
  `cod` int(11) NOT NULL,
  `date1` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `cod_adm` int(11) NOT NULL,
  `cod_repartition` int(11) NOT NULL,
  `cod_worker` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `adm`
--

CREATE TABLE `adm` (
  `cod` int(11) NOT NULL,
  `name_adm` varchar(50) NOT NULL,
  `profile` varchar(30) NOT NULL,
  `speciality` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `client`
--

CREATE TABLE `client` (
  `cod` int(11) NOT NULL,
  `client_name` varchar(50) NOT NULL,
  `number_identity_card` varchar(14) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `city` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `avenue` varchar(30) NOT NULL,
  `neighborhood` varchar(30) NOT NULL,
  `street` varchar(30) DEFAULT NULL,
  `cod_repartition` int(11) NOT NULL,
  `cod_acount_access` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `repartition`
--

CREATE TABLE `repartition` (
  `cod` int(11) NOT NULL,
  `district` varchar(30) NOT NULL,
  `avenue` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `user`
--

CREATE TABLE `user` (
  `cod` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `pass_word` varchar(30) NOT NULL,
  `cod_worker` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `worker`
--

CREATE TABLE `worker` (
  `cod` int(11) NOT NULL,
  `name_worker` varchar(30) NOT NULL,
  `number_identity_card` varchar(14) NOT NULL,
  `funtion_type` varchar(30) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `city` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `avenue` varchar(30) NOT NULL,
  `neighborhood` varchar(30) NOT NULL,
  `street` varchar(30) DEFAULT NULL,
  `cod_repartition` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `acount_access`
--
ALTER TABLE `acount_access`
  ADD PRIMARY KEY (`cod`),
  ADD UNIQUE KEY `acount_number_transfer` (`acount_number_transfer`),
  ADD UNIQUE KEY `name_transfer` (`name_transfer`);

--
-- Índices para tabela `add_client`
--
ALTER TABLE `add_client`
  ADD PRIMARY KEY (`cod`),
  ADD KEY `cod_client` (`cod_client`),
  ADD KEY `cod_worker` (`cod_worker`);

--
-- Índices para tabela `add_repartition_worker`
--
ALTER TABLE `add_repartition_worker`
  ADD PRIMARY KEY (`cod`),
  ADD KEY `cod_adm` (`cod_adm`),
  ADD KEY `cod_repartition` (`cod_repartition`),
  ADD KEY `cod_worker` (`cod_worker`);

--
-- Índices para tabela `adm`
--
ALTER TABLE `adm`
  ADD PRIMARY KEY (`cod`);

--
-- Índices para tabela `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`cod`),
  ADD UNIQUE KEY `number_identity_card` (`number_identity_card`),
  ADD UNIQUE KEY `phone_number` (`phone_number`),
  ADD KEY `cod_repartition` (`cod_repartition`),
  ADD KEY `cod_acount_access` (`cod_acount_access`);

--
-- Índices para tabela `repartition`
--
ALTER TABLE `repartition`
  ADD PRIMARY KEY (`cod`);

--
-- Índices para tabela `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`cod`),
  ADD KEY `cod_worker` (`cod_worker`);

--
-- Índices para tabela `worker`
--
ALTER TABLE `worker`
  ADD PRIMARY KEY (`cod`),
  ADD UNIQUE KEY `number_identity_card` (`number_identity_card`),
  ADD UNIQUE KEY `phone_number` (`phone_number`),
  ADD KEY `cod_repartition` (`cod_repartition`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `acount_access`
--
ALTER TABLE `acount_access`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `add_client`
--
ALTER TABLE `add_client`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `add_repartition_worker`
--
ALTER TABLE `add_repartition_worker`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `adm`
--
ALTER TABLE `adm`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `client`
--
ALTER TABLE `client`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `repartition`
--
ALTER TABLE `repartition`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `user`
--
ALTER TABLE `user`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `worker`
--
ALTER TABLE `worker`
  MODIFY `cod` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `add_client`
--
ALTER TABLE `add_client`
  ADD CONSTRAINT `add_client_ibfk_1` FOREIGN KEY (`cod_client`) REFERENCES `client` (`cod`),
  ADD CONSTRAINT `add_client_ibfk_2` FOREIGN KEY (`cod_worker`) REFERENCES `worker` (`cod`);

--
-- Limitadores para a tabela `add_repartition_worker`
--
ALTER TABLE `add_repartition_worker`
  ADD CONSTRAINT `add_repartition_worker_ibfk_1` FOREIGN KEY (`cod_adm`) REFERENCES `adm` (`cod`),
  ADD CONSTRAINT `add_repartition_worker_ibfk_2` FOREIGN KEY (`cod_repartition`) REFERENCES `repartition` (`cod`),
  ADD CONSTRAINT `add_repartition_worker_ibfk_3` FOREIGN KEY (`cod_worker`) REFERENCES `worker` (`cod`);

--
-- Limitadores para a tabela `client`
--
ALTER TABLE `client`
  ADD CONSTRAINT `client_ibfk_1` FOREIGN KEY (`cod_repartition`) REFERENCES `repartition` (`cod`),
  ADD CONSTRAINT `client_ibfk_2` FOREIGN KEY (`cod_acount_access`) REFERENCES `acount_access` (`cod`);

--
-- Limitadores para a tabela `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`cod_worker`) REFERENCES `worker` (`cod`);

--
-- Limitadores para a tabela `worker`
--
ALTER TABLE `worker`
  ADD CONSTRAINT `worker_ibfk_1` FOREIGN KEY (`cod_repartition`) REFERENCES `repartition` (`cod`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
