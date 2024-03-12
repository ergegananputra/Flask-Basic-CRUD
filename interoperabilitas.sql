-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2024 at 12:29 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `interoperabilitas`
--

-- --------------------------------------------------------

--
-- Table structure for table `kesehatan_umum`
--

CREATE TABLE `kesehatan_umum` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `tanggal_lahir` varchar(50) NOT NULL,
  `catatan` varchar(255) NOT NULL,
  `berat_badan` float NOT NULL,
  `tinggi_badan` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kesehatan_umum`
--

INSERT INTO `kesehatan_umum` (`id`, `nama`, `tanggal_lahir`, `catatan`, `berat_badan`, `tinggi_badan`) VALUES
(2, 'Adiel Boanerge', '10 Januari 2005', 'Alergi Manis', 60, 170),
(3, 'Shilamum Taza', '7 April 2004', 'Alergi Kecoa', 53, 154),
(8, 'Dwi Agung', '14 Februari 2004', 'Sehat', 56, 170),
(10, 'Marzuki Risal Bakrie 2', '14 Agustus 1880', 'Alergi Kucing', 56, 154),
(11, 'Jameter User', '11 Maret 2024', 'The detailed exploration of the problem statement or research question, focusing on the utilization of IoT technology for monitoring Alzheimer\'s patients and the elderly, does not seem to be concentrated in a single paragraph but is spread throughout the ', 70, 170);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kesehatan_umum`
--
ALTER TABLE `kesehatan_umum`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kesehatan_umum`
--
ALTER TABLE `kesehatan_umum`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
