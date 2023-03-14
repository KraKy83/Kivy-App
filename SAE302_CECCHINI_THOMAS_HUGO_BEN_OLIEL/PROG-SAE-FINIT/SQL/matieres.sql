-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Client :  localhost
-- Généré le :  Jeu 19 Janvier 2023 à 14:31
-- Version du serveur :  5.7.40-0ubuntu0.18.04.1
-- Version de PHP :  7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `c21220018`
--

-- --------------------------------------------------------

--
-- Structure de la table `matieres`
--

CREATE TABLE `matieres` (
  `id_etu` int(11) NOT NULL,
  `matiere1` double DEFAULT NULL,
  `matiere2` double DEFAULT NULL,
  `matiere3` double DEFAULT NULL,
  `matiere4` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `matieres`
--

INSERT INTO `matieres` (`id_etu`, `matiere1`, `matiere2`, `matiere3`, `matiere4`) VALUES
(11, 10, 12, 19, 14),
(2122753, 15, 14, 11, 17),
(20014866, 18, 18, 17, 19),
(21201772, 15, 15, 14, 14),
(21202056, 15, 14, 13, 12),
(21202188, 16, 15, 14, 12),
(21202469, 17, 18, 14, 11),
(21202654, 15, 14, 13, 12),
(21202671, 18, 15, 14, 12),
(21203819, 10, 12, 11, 10),
(21204871, 15, 14, 13, 12),
(21204894, 15, 14, 16, 18),
(21205262, 15, 14, 13, 12),
(21205661, 15, 15, 14, 14),
(21207700, 17, 18, 14, 13),
(21211145, 15, 16, 14, 20),
(21212434, 12, 15, 13, 16),
(21214787, 18, 17, 15, 14),
(21215366, 15, 17, 12, 11),
(21215601, 11, 12, 12, 12),
(21217487, 17, 18, 15, 14),
(21217925, 15, 15, 14, 14),
(21225617, 16, 18, 11, 14),
(21225765, 15, 15, 14, 12),
(200141129, 11, 18, 18, 17);

--
-- Index pour les tables exportées
--

--
-- Index pour la table `matieres`
--
ALTER TABLE `matieres`
  ADD PRIMARY KEY (`id_etu`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
