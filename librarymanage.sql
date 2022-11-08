-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 06, 2022 at 07:39 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pythondb`
--

-- --------------------------------------------------------

--
-- Table structure for table `librarymanage`
--

CREATE TABLE `librarymanage` (
  `Name` varchar(22) NOT NULL,
  `IdNo` varchar(22) NOT NULL,
  `Adress` varchar(50) NOT NULL,
  `MobileNo` varchar(15) NOT NULL,
  `BookId` varchar(22) NOT NULL,
  `BookTitle` varchar(22) NOT NULL,
  `DateBorrow` varchar(22) NOT NULL,
  `DueDate` varchar(22) NOT NULL,
  `DaysOnBook` varchar(5) NOT NULL,
  `LateFine` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `librarymanage`
--

INSERT INTO `librarymanage` (`Name`, `IdNo`, `Adress`, `MobileNo`, `BookId`, `BookTitle`, `DateBorrow`, `DueDate`, `DaysOnBook`, `LateFine`) VALUES
('', '', '', '', '', '', '', '', '', ''),
('mohit kumar', '2', 'MH', '987643213', 'BKID2012', 'core mannual', '2022-09-03 12:10:01.64', '2022-09-16 12:10:01.64', '10', 'Rs. 50'),
('Rahul', '1', '3/2 mandi hp', '70988654321', 'BKID2009', 'java mannual', '2022-09-03 12:12:08.31', '2022-09-10 12:12:08.31', '10', 'Rs. 50'),
('Harry porter', '4', '3249 gujrat', '98765543212', 'BKID2010', 'c++ mannual', '2022-09-03 12:15:22.98', '2022-09-16 12:15:22.98', '10', 'Rs. 50');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
