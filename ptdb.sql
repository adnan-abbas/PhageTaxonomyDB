-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: ptdb
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Bacterial Host`
--

DROP TABLE IF EXISTS `Bacterial Host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bacterial Host` (
  `BacteriaID` varchar(45) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`BacteriaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bacterial Host`
--

LOCK TABLES `Bacterial Host` WRITE;
/*!40000 ALTER TABLE `Bacterial Host` DISABLE KEYS */;
/*!40000 ALTER TABLE `Bacterial Host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Features`
--

DROP TABLE IF EXISTS `Features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Features` (
  `AccessionID` int NOT NULL,
  `%Coding Capacity%` int DEFAULT NULL,
  `#CDS` int DEFAULT NULL,
  `Classification` blob,
  `PositiveStrand%` int DEFAULT NULL,
  `NegativeStrand%` int DEFAULT NULL,
  `%molGC` int DEFAULT NULL,
  `#tRNA` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`AccessionID`),
  UNIQUE KEY `idFeatures_UNIQUE` (`AccessionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Features`
--

LOCK TABLES `Features` WRITE;
/*!40000 ALTER TABLE `Features` DISABLE KEYS */;
/*!40000 ALTER TABLE `Features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Genome`
--

DROP TABLE IF EXISTS `Genome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genome` (
  `AccessionID` int NOT NULL,
  `Length` int DEFAULT NULL,
  `Jumbo Phage` varchar(3) DEFAULT NULL,
  `Species` varchar(45) DEFAULT NULL,
  `Description` longtext,
  `Modification Date` date DEFAULT NULL,
  `Sequence` longtext,
  PRIMARY KEY (`AccessionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genome`
--

LOCK TABLES `Genome` WRITE;
/*!40000 ALTER TABLE `Genome` DISABLE KEYS */;
INSERT INTO `Genome` VALUES (123456,56,NULL,NULL,NULL,NULL,NULL),(234543,32,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Genome` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Species Attacks`
--

DROP TABLE IF EXISTS `Species Attacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Species Attacks` (
  `Species` varchar(45) NOT NULL,
  `BacteriaID` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Species`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Species Attacks`
--

LOCK TABLES `Species Attacks` WRITE;
/*!40000 ALTER TABLE `Species Attacks` DISABLE KEYS */;
/*!40000 ALTER TABLE `Species Attacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Taxonomy`
--

DROP TABLE IF EXISTS `Taxonomy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Taxonomy` (
  `Species` varchar(45) NOT NULL,
  `Order` varchar(45) DEFAULT NULL,
  `Family` varchar(45) DEFAULT NULL,
  `Genus` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Species`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Taxonomy`
--

LOCK TABLES `Taxonomy` WRITE;
/*!40000 ALTER TABLE `Taxonomy` DISABLE KEYS */;
/*!40000 ALTER TABLE `Taxonomy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-22 15:04:18
