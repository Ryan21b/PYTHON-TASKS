-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: lifechoices_database
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_created_users`
--

DROP TABLE IF EXISTS `admin_created_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_created_users` (
  `username` varchar(25) NOT NULL,
  `password` varchar(4) NOT NULL,
  KEY `username` (`username`),
  CONSTRAINT `admin_created_users_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_created_users`
--

LOCK TABLES `admin_created_users` WRITE;
/*!40000 ALTER TABLE `admin_created_users` DISABLE KEYS */;
INSERT INTO `admin_created_users` VALUES ('RGHOST','801'),('Rbarron','9212');
/*!40000 ALTER TABLE `admin_created_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timesheet_login`
--

DROP TABLE IF EXISTS `timesheet_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timesheet_login` (
  `username` varchar(25) NOT NULL,
  `time_in` varchar(20) NOT NULL,
  `date_today` date NOT NULL,
  KEY `username` (`username`),
  CONSTRAINT `timesheet_login_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timesheet_login`
--

LOCK TABLES `timesheet_login` WRITE;
/*!40000 ALTER TABLE `timesheet_login` DISABLE KEYS */;
INSERT INTO `timesheet_login` VALUES ('Rghost','08:45:00','2020-05-11'),('Rbarron','07:31','2020-05-11');
/*!40000 ALTER TABLE `timesheet_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timesheet_logout`
--

DROP TABLE IF EXISTS `timesheet_logout`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timesheet_logout` (
  `username` varchar(25) NOT NULL,
  `time_out` varchar(20) NOT NULL,
  `date_today` date NOT NULL,
  KEY `username` (`username`),
  CONSTRAINT `timesheet_logout_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timesheet_logout`
--

LOCK TABLES `timesheet_logout` WRITE;
/*!40000 ALTER TABLE `timesheet_logout` DISABLE KEYS */;
INSERT INTO `timesheet_logout` VALUES ('Rghost','16:50:00','2020-05-11'),('Rbarron','17:00','2020-05-11');
/*!40000 ALTER TABLE `timesheet_logout` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(4) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (3214,'Ryan','Barron','Rb21','ghs3'),(3452,'Ryan','Barron','Rbarron','3698'),(4390,'Ryan','Barron','Rghost','rg21');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-11 23:01:26
