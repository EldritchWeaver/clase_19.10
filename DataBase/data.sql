-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-03-2025 a las 03:28:00
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
-- Base de datos: `data`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clinicas`
--

CREATE TABLE `clinicas` (
  `ID_clinica` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `Direccion` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Clinicas en SJM';

--
-- Volcado de datos para la tabla `clinicas`
--

INSERT INTO `clinicas` (`ID_clinica`, `nombre`, `Direccion`) VALUES
(1, 'Cruz Roja', 'Av. Miranda'),
(2, 'Fundacliu', 'Av. Bolivar'),
(3, 'Policlinica', 'Av. Guaiquera'),
(4, 'Fundacliu', 'Calle Salias'),
(5, 'Clinica Cedeño', 'Av. Bolivar');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `enfermeros`
--

CREATE TABLE `enfermeros` (
  `ID_enfermero` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `jornada` varchar(100) NOT NULL,
  `ID_clinica` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Enfermeros en SJM';

--
-- Volcado de datos para la tabla `enfermeros`
--

INSERT INTO `enfermeros` (`ID_enfermero`, `nombre`, `apellido`, `jornada`, `ID_clinica`) VALUES
(1, 'Jennifer', 'Medrano', 'Lunes-Miercoles', 5),
(2, 'Natalia', 'Jimenez', 'Viernes-Domingos', 3),
(3, 'Jose', 'Garcia', 'Miercoles-Viernes', 4),
(4, 'Alonso', 'Pacheco', 'Lunes-Jueves', 2),
(5, 'Sofia', 'Luna', 'Martes-Sabados', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `ID_paciente` int(5) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `Condicion` varchar(100) NOT NULL,
  `Sexo` varchar(100) NOT NULL,
  `ID_enfermero` int(5) NOT NULL,
  `habitacion` int(3) NOT NULL,
  `ID_clinica` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='Pacientes en SJM';

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`ID_paciente`, `nombre`, `apellido`, `estado`, `Condicion`, `Sexo`, `ID_enfermero`, `habitacion`, `ID_clinica`) VALUES
(1, 'Maria', 'Hernandez', 'Hospitalizada', 'Post-Parto', 'Femenino', 2, 10, 3),
(2, 'Juan', 'Gonzalez', 'De alta', 'asfixia mecanica', 'masculino', 1, 5, 5),
(3, 'Daniel', 'Mendoza', 'Hospitalizado', 'Anemia', 'masculino', 4, 20, 2),
(4, 'Josefina', 'Mendoza', 'Hospitalizada', 'insuficiencia renal', 'femenino', 5, 35, 3),
(5, 'Martina', 'Torres', 'De alta', 'Desmayos por dolor', 'femenino', 3, 15, 4);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clinicas`
--
ALTER TABLE `clinicas`
  ADD PRIMARY KEY (`ID_clinica`);

--
-- Indices de la tabla `enfermeros`
--
ALTER TABLE `enfermeros`
  ADD PRIMARY KEY (`ID_enfermero`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`ID_paciente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clinicas`
--
ALTER TABLE `clinicas`
  MODIFY `ID_clinica` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `enfermeros`
--
ALTER TABLE `enfermeros`
  MODIFY `ID_enfermero` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `ID_paciente` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
