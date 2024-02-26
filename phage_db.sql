-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: phage_db
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
-- Table structure for table `features_table`
--

DROP TABLE IF EXISTS `features_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `features_table` (
  `Accession` text,
  `Classification` text,
  `molGC (%)` double DEFAULT NULL,
  `Number CDS` int DEFAULT NULL,
  `Positive Strand (%)` double DEFAULT NULL,
  `Negative Strand (%)` double DEFAULT NULL,
  `Coding Capacity (%)` double DEFAULT NULL,
  `tRNAs` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `features_table`
--

LOCK TABLES `features_table` WRITE;
/*!40000 ALTER TABLE `features_table` DISABLE KEYS */;
INSERT INTO `features_table` VALUES ('MZ322319','Pseudomonas phage vB_Pae-PA152 unclassified Enquatrovirus Enquatrovirus Enquatrovirinae Schitoviridae Caudovirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',53.562,115,80.86956522,19.13043478,93.96915388,0),('OQ221551','Bacteroides phage PhiCrAssBcn16 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',34.667,108,41.66666667,58.33333333,93.56130963,21),('OQ221536','Bacteroides phage PhiCrAssBcn1 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.072,102,60.78431373,39.21568627,94.22124215,24),('OQ221559','Bacteroides phage PhiCrAssBcn24 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.185,100,39,61,94.06766648,24),('OQ221557','Bacteroides phage PhiCrAssBcn22 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.091,98,56.12244898,43.87755102,94.59837586,24),('OQ221548','Bacteroides phage PhiCrAssBcn13 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.196,100,61,39,94.37790644,24),('OQ221544','Bacteroides phage PhiCrAssBcn9 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.088,102,38.23529412,61.76470588,94.27179405,24),('OQ221539','Bacteroides phage PhiCrAssBcn4 Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',35.18,101,37.62376238,62.37623762,93.58476431,24),('NC_055832','Bacteroides phage DAC15 Wulfhauvirus bangladeshii Wulfhauvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',37.042,110,39.09090909,60.90909091,93.70615313,13),('NC_055828','Bacteroides phage crAss002 Jahgtovirus secundus Jahgtovirus Churivirinae Intestiviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',31.929,81,41.97530864,58.02469136,93.10867462,0),('NC_048874','Escherichia phage EC6098 Enterogokushovirus EC6098 Enterogokushovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',48.387,6,100,0,93.52629253,0),('NC_003438','Spiroplasma phage 4 Spiromicrovirus SpV4 Spiromicrovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',32.052,6,100,0,78.24021715,0),('NC_002180','Chlamydia phage phiCPAR39 Chlamydiamicrovirus CPAR39 Chlamydiamicrovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',40.622,4,100,0,78.9717564,0),('NC_001422','Escherichia phage phiX174 Sinsheimervirus phiX174 Sinsheimervirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.764,6,100,0,65.83735611,0),('NC_049977','Bacteroides phage crAss001 Kehishuvirus primarius Kehishuvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',34.743,101,42.57425743,57.42574257,93.71244364,24),('NC_021806','Cellulophaga phage phi14:2 Akihdevirus balticus Akihdevirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',29.605,118,59.3220339,40.6779661,94.25800155,0),('AE002163','Chlamydia phage phiCPAR39 Chlamydiamicrovirus CPAR39 Chlamydiamicrovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',40.622,4,100,0,78.9717564,0),('SPVDNA','Spiroplasma phage 4 Spiromicrovirus SpV4 Spiromicrovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',32.052,6,100,0,78.24021715,0),('PX1CG','Escherichia phage phiX174 Sinsheimervirus phiX174 Sinsheimervirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.764,6,100,0,65.83735611,0),('MK629527','Escherichia phage Lilleven Alphatrevirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.45,8,100,0,89.7044335,0),('MN917146','Bacteroides phage crAss002 Jahgtovirus secundus Jahgtovirus Churivirinae Intestiviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',31.929,81,41.97530864,58.02469136,93.10867462,0),('MT947439','Protaetiibacter phage SSC1 Sinsheimervirus phiX174 Sinsheimervirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.709,7,100,0,96.13813591,0),('MT074138','Bacteroides phage DAC17 Wulfhauvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',37.034,111,36.03603604,63.96396396,94.06875632,13),('MT074136','Bacteroides phage DAC15 Wulfhauvirus bangladeshii Wulfhauvirus Asinivirinae Steigviridae Crassvirales Caudoviricetes Uroviricota Heunggongvirae Duplodnaviria Viruses',37.042,110,39.09090909,60.90909091,93.70615313,13),('MT185428','Escherichia phage EC6098 Enterogokushovirus EC6098 Enterogokushovirus Gokushovirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',48.387,6,100,0,93.52629253,0),('MN266305','Shigella phage SGF3 Sinsheimervirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.838,7,71.42857143,28.57142857,86.78054215,0),('NC_007823','Escherichia phage NC28 Alphatrevirus NC28 Alphatrevirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.831,9,100,0,92.2506183,0),('NC_007827','Escherichia phage NC29 Alphatrevirus NC29 Alphatrevirus Bullavirinae Microviridae Petitvirales Malgrandaviricetes Phixviricota Sangervirae Monodnaviria Viruses',44.352,10,100,0,91.26058476,0);
/*!40000 ALTER TABLE `features_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genome_table`
--

DROP TABLE IF EXISTS `genome_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genome_table` (
  `Accession` text,
  `Species` text,
  `Genome Length (bp)` int DEFAULT NULL,
  `Modification Date` text,
  `Sequence` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genome_table`
--

LOCK TABLES `genome_table` WRITE;
/*!40000 ALTER TABLE `genome_table` DISABLE KEYS */;
INSERT INTO `genome_table` VALUES ('MZ322319','Pseudomonas phage vB_Pae-PA152',74434,'18-Jul-23',''),('OQ221551','Bacteroides phage PhiCrAssBcn16',99601,'17-May-23',''),('OQ221536','Bacteroides phage PhiCrAssBcn1',99312,'17-May-23',''),('OQ221559','Bacteroides phage PhiCrAssBcn24',97685,'17-May-23',''),('OQ221557','Bacteroides phage PhiCrAssBcn22',98637,'17-May-23',''),('OQ221548','Bacteroides phage PhiCrAssBcn13',98273,'17-May-23',''),('OQ221544','Bacteroides phage PhiCrAssBcn9',99752,'17-May-23',''),('OQ221539','Bacteroides phage PhiCrAssBcn4',101446,'17-May-23',''),('NC_055832','Bacteroides phage DAC15',99494,'11-Jan-23',''),('NC_055828','Bacteroides phage crAss002',93030,'11-Jan-23',''),('NC_048874','Escherichia phage EC6098',4526,'11-Jan-23',''),('NC_003438','Spiroplasma phage 4',4421,'11-Jan-23',''),('NC_002180','Chlamydia phage phiCPAR39',4532,'11-Jan-23',''),('NC_001422','Escherichia phage phiX174',5386,'11-Jan-23',''),('NC_049977','Bacteroides phage crAss001',102679,'10-Jan-23',''),('NC_021806','Cellulophaga phage phi14:2',100418,'8-Jan-23',''),('AE002163','Chlamydia phage phiCPAR39',4532,'7-Apr-22',''),('SPVDNA','Spiroplasma phage 4',4421,'24-Mar-22',''),('PX1CG','Escherichia phage phiX174',5386,'28-Oct-21',''),('MK629527','Escherichia phage Lilleven',6090,'1-Feb-21',''),('MN917146','Bacteroides phage crAss002',93030,'4-Jan-21',''),('MT947439','Protaetiibacter phage SSC1',5386,'29-Sep-20',''),('MT074138','Bacteroides phage DAC17',98900,'30-Jun-20',''),('MT074136','Bacteroides phage DAC15',99494,'30-Jun-20',''),('MT185428','Escherichia phage EC6098',4526,'1-Apr-20',''),('MN266305','Shigella phage SGF3',5386,'9-Oct-19',''),('NC_007823','Escherichia phage NC28',6065,'28-Jun-19',''),('NC_007827','Escherichia phage NC29',6259,'28-Jun-19','');
/*!40000 ALTER TABLE `genome_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxonomy_table`
--

DROP TABLE IF EXISTS `taxonomy_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxonomy_table` (
  `Species` text,
  `Order` text,
  `Family` text,
  `Genus` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxonomy_table`
--

LOCK TABLES `taxonomy_table` WRITE;
/*!40000 ALTER TABLE `taxonomy_table` DISABLE KEYS */;
INSERT INTO `taxonomy_table` VALUES ('Pseudomonas phage vB_Pae-PA152','Caudovirales','Schitoviridae','Enquatrovirus'),('Bacteroides phage PhiCrAssBcn16','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn1','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn24','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn22','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn13','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn9','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage PhiCrAssBcn4','Crassvirales','Steigviridae','Kehishuvirus'),('Bacteroides phage DAC15','Crassvirales','Steigviridae','Wulfhauvirus'),('Bacteroides phage crAss002','Crassvirales','Intestiviridae','Jahgtovirus'),('Escherichia phage EC6098','Petitvirales','Microviridae','Enterogokushovirus'),('Spiroplasma phage 4','Petitvirales','Microviridae','Spiromicrovirus'),('Chlamydia phage phiCPAR39','Petitvirales','Microviridae','Chlamydiamicrovirus'),('Escherichia phage phiX174','Petitvirales','Microviridae','Sinsheimervirus'),('Bacteroides phage crAss001','Crassvirales','Steigviridae','Kehishuvirus'),('Cellulophaga phage phi14:2','Crassvirales','Steigviridae','Akihdevirus'),('Escherichia phage Lilleven','Petitvirales','Microviridae','Alphatrevirus'),('Protaetiibacter phage SSC1','Petitvirales','Microviridae','Sinsheimervirus'),('Bacteroides phage DAC17','Crassvirales','Steigviridae','Wulfhauvirus'),('Shigella phage SGF3','Petitvirales','Microviridae','Sinsheimervirus'),('Escherichia phage NC28','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage NC29','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage ID52','Petitvirales','Microviridae','Gequatrovirus'),('Escherichia phage ID62','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage WA45','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage NC35','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage ID32','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage ID21','Petitvirales','Microviridae','Alphatrevirus'),('Chlamydia phage 4','Petitvirales','Microviridae','Chlamydiamicrovirus'),('Escherichia phage St-1','Petitvirales','Microviridae','Alphatrevirus'),('Enterobacteria phage WA13','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage ID2 Moscow/ID/2001','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID18','Petitvirales','Microviridae','Gequatrovirus'),('Bdellovibrio phage phiMH2K','Petitvirales','Microviridae','Bdellomicrovirus'),('Chlamydia phage 2','Petitvirales','Microviridae','Chlamydiamicrovirus'),('Chlamydia phage CPG1','Petitvirales','Microviridae','Chlamydiamicrovirus'),('Escherichia phage phiK','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage alpha3','Petitvirales','Microviridae','Alphatrevirus'),('Escherichia phage EMCL318','Petitvirales','Microviridae','Gequatrovirus'),('Salmonella phage alphaalpha','Petitvirales','Microviridae','Sinsheimervirus'),('Escherichia phage G4','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID11','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage MED1','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage FL76 Tallahassee/FL/2012','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage FL68 Tallahassee/FL/2012','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID204 Moscow/ID','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA14','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage NC10','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID12','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA6','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID41','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage NC19','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage NC13','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage NC2','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA5','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage ID8','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA3','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA2','Petitvirales','Microviridae','Gequatrovirus'),('Enterobacteria phage WA11','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage WA10','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage WA4','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC56','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC51','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC41','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC37','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC16','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC11','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC7','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC5','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC1','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage ID45','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage ID34','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage ID22','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage ID1','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC3','Petitvirales','Microviridae','Alphatrevirus'),('Enterobacteria phage S13','Petitvirales','Microviridae','Sinsheimervirus'),('Enterobacteria phage NC6','Petitvirales','Microviridae','Gequatrovirus'),('Chlamydia phage 3','Petitvirales','Microviridae','Chlamydiamicrovirus');
/*!40000 ALTER TABLE `taxonomy_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-26 12:55:33
