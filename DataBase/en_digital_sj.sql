-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-02-2025 a las 17:57:13
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `en_digital_sj`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `id_curso` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `duracion` int(150) NOT NULL COMMENT 'En meses',
  `descripcion` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `curso`
--

INSERT INTO `curso` (`id_curso`, `nombre`, `duracion`, `descripcion`) VALUES
(1, 'Programacion', 6, 'Introduccion a la programacion'),
(2, 'Diseño Grafico', 6, 'Aprende Illustrator y Photoshop'),
(3, 'Comunity Manage', 5, 'Aprende a gestionar una comunidad digital');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ed_estudiante`
--

CREATE TABLE `ed_estudiante` (
  `id_estudiante` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `edad` int(3) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `email` varchar(150) NOT NULL,
  `id_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `ed_estudiante`
--

INSERT INTO `ed_estudiante` (`id_estudiante`, `nombre`, `apellido`, `edad`, `sexo`, `email`, `id_curso`) VALUES
(1, 'Gabriel', 'Moreno', 19, 'Masculino', 'moreno@gmail.com', 1),
(2, 'Clara', 'Castillo', 17, 'Femenino', 'clara@gmail.com', 1),
(3, 'Jose', 'Perez', 18, 'Masculino', 'perez@gmail.com', 2),
(4, 'Carlos', 'Perez', 18, 'Masculino', 'perez@gmail.com', 2),
(6, 'Maria', 'Moreno', 16, 'Femenino', 'maria@gmail.com', 3),
(7, 'Valeria', 'Santaella', 20, 'Femenino', 'santaella@gmail.com', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id_profesor` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `edad` int(120) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `id_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id_profesor`, `nombre`, `apellido`, `edad`, `correo`, `id_curso`) VALUES
(1, 'Gabo', 'Diaz', 38, 'diaz@gmail.com', 3),
(2, 'Jenny', 'Rojas', 38, 'rojas@gmail.com', 1),
(3, 'Jose', 'Perez', 27, 'perez@gmail.com', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indices de la tabla `ed_estudiante`
--
ALTER TABLE `ed_estudiante`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id_profesor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `curso`
--
ALTER TABLE `curso`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `ed_estudiante`
--
ALTER TABLE `ed_estudiante`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
