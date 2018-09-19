-- MySQL dump 10.13  Distrib 8.0.11, for Linux (x86_64)
--
-- Host: localhost    Database: gardeneasy
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `events` (
  `ModuleData_ID` bigint(20) NOT NULL,
  `Module_ID` int(11) NOT NULL,
  `Event_Description` text,
  `Event_Name` char(20) NOT NULL DEFAULT 'undefined',
  `Event_Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Module_ID_Affected` int(11) DEFAULT NULL,
  PRIMARY KEY (`ModuleData_ID`,`Module_ID`),
  KEY `fk_events_module_data1_idx` (`ModuleData_ID`),
  KEY `fk_events_modules1_idx` (`Module_ID`),
  KEY `fk_events_modules2_idx` (`Module_ID_Affected`),
  CONSTRAINT `fk_events_module_data1` FOREIGN KEY (`ModuleData_ID`) REFERENCES `module_data` (`moduledata_id`),
  CONSTRAINT `fk_events_modules1` FOREIGN KEY (`Module_ID`) REFERENCES `modules` (`module_id`),
  CONSTRAINT `fk_events_modules2` FOREIGN KEY (`Module_ID_Affected`) REFERENCES `modules` (`module_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module_data`
--

DROP TABLE IF EXISTS `module_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `module_data` (
  `ModuleData_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `Module_ID` int(11) NOT NULL,
  `ModuleData_Value` char(40) DEFAULT NULL,
  `ModuleData_DateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ModuleData_Processed` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ModuleData_ID`),
  KEY `fk_module_data_modules_idx` (`Module_ID`),
  CONSTRAINT `fk_module_data_modules` FOREIGN KEY (`Module_ID`) REFERENCES `modules` (`module_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module_data`
--

LOCK TABLES `module_data` WRITE;
/*!40000 ALTER TABLE `module_data` DISABLE KEYS */;
/*!40000 ALTER TABLE `module_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modules`
--

DROP TABLE IF EXISTS `modules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `modules` (
  `Module_ID` int(11) NOT NULL,
  `Module_Description` text,
  `Module_Name` varchar(60) DEFAULT NULL,
  `Module_Status` enum('A','I') NOT NULL DEFAULT 'I' COMMENT '[''Active''|''Inactive'']',
  `Module_StartValue` char(40) NOT NULL DEFAULT 'undefined',
  `Module_EndValue` char(40) NOT NULL DEFAULT 'undefined',
  PRIMARY KEY (`Module_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modules`
--

LOCK TABLES `modules` WRITE;
/*!40000 ALTER TABLE `modules` DISABLE KEYS */;
INSERT INTO `modules` VALUES (1,'Modulo teste','Teste','A','100','140');
/*!40000 ALTER TABLE `modules` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-10 20:27:22
