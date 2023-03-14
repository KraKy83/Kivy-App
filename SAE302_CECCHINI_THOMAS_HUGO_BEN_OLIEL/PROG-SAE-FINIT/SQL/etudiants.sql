-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Client :  localhost
-- Généré le :  Jeu 19 Janvier 2023 à 14:30
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
-- Structure de la table `etudiants`
--

CREATE TABLE `etudiants` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `annee` int(11) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `statut` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `etudiants`
--

INSERT INTO `etudiants` (`id`, `nom`, `prenom`, `annee`, `password`, `statut`) VALUES
(11, 'Madjarov', 'Ivan', 2023, '$2y$10$pN.oEq9SexXEt.pTUhkSrOPLdNSz/093C7/BaATKejpptpKttX8Om', 'Profs'),
(2122753, 'Collot', 'Enzo', 2023, '$2y$10$unnQ6QJXvfRUzIncl/qVZu9u.NrqHGL3sFMbdskCSLxSuLzDFOrOG', '2A'),
(20014866, 'Meylan', 'Kenan', 2023, '$2y$10$Xai23Voxbnmk1w680UFVce49LwQHLDJVkDTViTPXx7eWHSHHOB.du', '2A'),
(21201772, 'Ben Oliel', 'Hugo', 2023, '$2y$10$I41OetTloPjfbwzc4pEEYOZ3Y9TRv9xSkBQdtOJP00fEIOxYyWTBS', '2A'),
(21202056, 'Fournier', 'Jeremy', 2023, '$2y$10$qNXbrZnBLvEstFhXYhtsUeoZ.By6WPfxHHwGic8kaJMXxBYW67spW', '2A'),
(21202188, 'Flandin', 'Vincent', 2023, '$2y$10$nIChrGoUqDvUExollWC1YeAadHCjYTYsdzv6q4DoZXCM.kRpYE4qG', '2A'),
(21202469, 'Sbai', 'Hatim', 2023, '$2y$10$p6nUkA3HJAbM.Lk2HD.tfOiYORWsaSBVbMc9MjvBGlOXl2bUAas22', '2A'),
(21202654, 'Gignac', 'Jason', 2023, '$2y$10$C.kPOGAoBuDLUlRzYYxvQ.ELdrL94AzkOKa4RCauDDENhaTbBeRja', '2A'),
(21202671, 'Bourgeon', 'Dorian', 2023, '$2y$10$AweTRme/BFPVg1jnY5wflundZWCOVp.OfWIOSMuF7MrHj5objio7a', '2A'),
(21203819, 'Aurouze', 'Eliott', 2023, '$2y$10$AC9dplLPlJvmR8.Usqsc6uDUEEPhBlmIiiU.TSeZZy6yLjeiXCM66', '2A'),
(21204871, 'Mathieu', 'Hugo', 2023, '$2y$10$fqM2JnaThGf16NlSE7JHm.eLSxNk3RWKTNzWT5OoaeCuTM.WxqIi6', '2A'),
(21204894, 'Robert', 'Nicolas', 2023, '$2y$10$bJPbwEYwKp2CFNYQnoq68uFUfb90v4QAv1AnDvFc4QxYj9rD4BO/.', '2A'),
(21205262, 'Goriot', 'Leo', 2023, '$2y$10$L9KnoZ00BPqmHGhGGbWBkecRiFypRp5t/NwDUkJ3pesBIWsPqn60y', '2A'),
(21205661, 'Pavy', 'Killian', 2023, '$2y$10$jozJwoUmuuRR5WHNEZtSpOyKg2DiYWnH7PDhxD0xkc//Df63xzhiS', '2A'),
(21207700, 'Ripiego', 'Jorane', 2023, '$2y$10$25zuKakbexH9OlwuoTEa5eXOrlFV2yhbFbT.7861.UobDhoSWdtXu', '2A'),
(21211145, 'Delchiappo', 'Quentin', 2023, '$2y$10$ZNhQ3L7qDfNYnuEOblXiOeaXEtcqBIHtCFi.8prNlVxaUEd9KhnhG', '2A'),
(21212434, 'Soragna', 'Quentin', 2023, '$2y$10$lqmiCgz3fYmethiX8E2.ruudQ4XTKcHhfymZwjmQS6ZC4zN1lIFsG', '2A'),
(21214787, 'Baptiste', 'Maxime', 2023, '$2y$10$sFHEb4UwLPnVxLZTPa5II.C65j4pKmVVwaUxbeA2zEjbQ7sChf3DS', '2A'),
(21215366, 'Mouigni', 'Hadji', 2023, '$2y$10$j6dxPFETRYd4FworuGppf.NQpHHjiyXIVj.o1ssUTFzmO/lnAFUoW', '2A'),
(21215601, 'Maresic', 'Baptiste', 2023, '$2y$10$UYP2jr5sq0rLXRkVrgZHqeBSgJz3ipU5afXloL4/7ig1GfLdB81cK', '2A'),
(21217487, 'Planas', 'Antoine', 2023, '$2y$10$DS00uyDclSkQrbsI8fZFSOtIyiMDWjIhwxSO41fEsdOW1J9HZ8CYi', '2A'),
(21217925, 'Ocana', 'Kevin', 2023, '$2y$10$lQWo8po4xDQuzVw7VY7QCeARdUJmvlA3EwLtZ9htsDJ1oc7SKML2W', '2A'),
(21225617, 'Blaas', 'Victor', 2023, '$2y$10$BZIUnFUhN4VxGJ53GSlOee2c.ZnJL2K9lznIIk90LDodwSv/Z7eP6', '2A'),
(21225765, 'Saint Martin', 'Dorian', 2023, '$2y$10$BGtvrMQ7LOKwmcZ9kkQ6UeoM/eg4CFFctBYEfkjs5XNVnRlHhl9V2', '2A'),
(200141129, 'Garda', 'Quentin', 2023, '$2y$10$bLzx6Xur0PCT1H2IrTAA7O.Nf3AHDTowzH/izOlQos.yDIdJb2fDO', '2A');

--
-- Index pour les tables exportées
--

--
-- Index pour la table `etudiants`
--
ALTER TABLE `etudiants`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `etudiants`
--
ALTER TABLE `etudiants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2122222223;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
