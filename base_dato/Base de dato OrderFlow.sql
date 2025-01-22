-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: gpon
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas` (
  `AreaID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`AreaID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'INSTALACION'),(2,'SOPORTE TECNICO');
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cajas`
--

DROP TABLE IF EXISTS `cajas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cajas` (
  `cajaID` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) NOT NULL,
  `Latitud` decimal(10,8) DEFAULT NULL,
  `Longitud` decimal(11,8) DEFAULT NULL,
  PRIMARY KEY (`cajaID`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cajas`
--

LOCK TABLES `cajas` WRITE;
/*!40000 ALTER TABLE `cajas` DISABLE KEYS */;
INSERT INTO `cajas` VALUES (1,'NAP SIN ASIGNAR',0.00000000,0.00000000),(2,'CTO SIN ASIGNAR',0.00000000,0.00000000),(25,'NAP-001',-11.95109000,-77.05667218),(26,'CTO-002',-11.95247301,-77.05710821),(27,'CTO-003',-11.95487633,-77.05896352),(28,'CTO-004',-11.95474162,-77.05778528),(29,'CTO-005',-11.95235767,-77.05867741),(30,'CTO-006',-11.95313229,-77.05922614),(31,'NAP-007',-11.95164884,-77.05906020),(32,'NAP-008',-11.96696011,-77.07027151),(33,'NAP-009',-11.96605600,-77.06900000),(34,'NAP-010',-11.96465943,-77.07190708),(35,'NAP-011',-11.96518510,-77.07199511),(36,'NAP-012',-11.96633300,-77.07227800),(37,'NAP-013',-11.96751000,-77.07370500),(38,'NAP-014',-11.95621579,-77.05715978),(39,'NAP-015',-11.95841008,-77.05779578),(40,'NAP-016',-11.96024370,-77.05443671),(41,'NAP-017',-11.95706439,-77.05508573),(42,'NAP-018',-11.95758447,-77.05340790),(43,'NAP-019',-11.95671126,-77.05860611),(44,'NAP-020',-11.95841499,-77.05916896),(45,'NAP-021',-11.96113500,-77.05961100),(46,'NAP-022',-11.99244251,-77.06486175),(47,'NAP-023',-11.99255900,-77.06687000),(48,'NAP-024',-11.99151641,-77.06788424),(49,'NAP-025',-11.99295019,-77.06954764),(50,'NAP-026',-11.99263300,-77.06284800),(51,'NAP-027',-11.96682102,-77.06248089),(52,'NAP-028',-11.96933100,-77.06192300),(53,'NAP-029',-11.96542537,-77.06246737),(54,'NAP-030',-11.95924037,-77.06834292),(55,'NAP-031',-11.96187398,-77.07145106),(56,'NAP-032',-11.96051244,-77.07165691),(57,'NAP-033',-11.96026400,-77.06999700),(58,'NAP-034',-11.97143700,-77.07145950),(59,'NAP-035',-11.97104221,-77.06895170),(60,'NAP-036',-11.95199310,-77.05617437),(61,'NAP-037',-11.95553801,-77.05294297),(62,'NAP-038',-11.95321800,-77.05652400),(63,'NAP-039',-11.95366700,-77.05516700),(64,'NAP-040',-11.95430100,-77.05398200),(65,'NAP-041',-11.95441300,-77.05352800),(66,'NAP-042',-11.94877500,-77.05810400),(67,'NAP-043',-11.94688840,-77.05902212),(68,'NAP-044',-11.94720736,-77.05938313),(69,'NAP-045',-11.95889400,-77.05630500),(70,'NAP-046',-11.96921042,-77.05917370),(71,'NAP-047',-11.96942877,-77.06007445),(72,'NAP-048',-11.97025068,-77.05963677),(73,'NAP-049',-11.96976550,-77.05805755),(74,'NAP-050',-11.96772469,-77.05728317),(75,'NAP-051',-11.96578500,-77.05704600),(76,'NAP-052',-11.96548086,-77.05782271),(77,'NAP-053',-11.96501400,-77.05806513),(78,'NAP-054',-11.96576465,-77.05861087),(79,'NAP-055',-11.97646749,-77.05695710),(80,'NAP-056',-11.97999784,-77.05627771),(81,'NAP-057',-11.97868531,-77.05873739),(82,'NAP-058',-11.97997500,-77.05785000),(83,'NAP-059',-11.97721642,-77.05750018),(84,'NAP-060',-11.97475449,-77.05640799),(85,'NAP-061',-11.98082000,-77.05448600),(86,'NAP-062',-11.98111207,-77.05561633),(87,'NAP-063',-11.98334454,-77.05606724),(88,'NAP-064',-11.98183887,-77.05492862),(89,'NAP-065',-11.98097737,-77.05288671),(90,'NAP-066',-11.97892999,-77.04932879),(91,'NAP-067',-11.97865004,-77.04768202),(92,'NAP-068',-11.97790452,-77.05573763),(93,'NAP-069',-11.97697966,-77.05521475),(94,'NAP-070',-11.97692857,-77.05354715),(95,'NAP-071',-11.97668978,-77.05425422),(96,'NAP-072',-11.96231409,-77.05843811),(97,'NAP-073',-11.96182200,-77.05994500),(98,'NAP-074',-11.96388828,-77.06067571),(99,'NAP-075',-11.96170600,-77.05708200),(100,'NAP-076',-11.98668525,-77.05470749),(101,'NAP-077',-11.98297137,-77.04626876),(102,'NAP-078',-11.97615137,-77.03779423),(103,'NAP-079',-11.97761866,-77.03798427),(104,'NAP-080',-11.97958186,-77.04638012),(105,'NAP-081',-11.97935322,-77.04541926),(106,'NAP-082',-11.97884176,-77.04357498),(107,'NAP-083',-11.97789500,-77.04032900),(108,'NAP-084',-11.97703698,-77.03816357),(109,'NAP-085',-11.97499000,-77.03742100),(110,'NAP-086',-11.97554500,-77.05784500),(111,'NAP-087',-11.97503500,-77.05770500),(112,'NAP-088',-11.97601145,-77.05611375),(113,'NAP-089',-11.96638776,-77.05525131),(114,'NAP-090',-11.96692657,-77.05271241),(115,'NAP-091',-11.97332509,-77.04708171),(116,'NAP-092',-11.97708196,-77.04862247),(117,'NAP-093',-11.97548661,-77.04907290),(118,'NAP-094',-11.97463200,-77.04682900),(119,'NAP-095',-11.97267725,-77.04522867),(120,'NAP-096',-11.97176372,-77.04309875),(121,'NAP-097',-11.97291092,-77.04185173),(122,'NAP-098',-11.97439314,-77.05244611),(123,'NAP-099',-11.97479879,-77.05457957),(124,'NAP-100',-11.97415273,-77.05502082);
/*!40000 ALTER TABLE `cajas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `ClienteID` int NOT NULL AUTO_INCREMENT,
  `NumeroIdentificacion` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `TipoDocumento` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `NombreCompleto` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Direccion` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `DepartamentoID` int NOT NULL,
  `ProvinciaID` int NOT NULL,
  `DistritoID` int NOT NULL,
  `CoordenadasGPS` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Telefono` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Correo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `RecomendadoPor` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `NombreRecomendado` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `TipoServicioID` int NOT NULL,
  `PlanID` int DEFAULT NULL,
  `PromoID` int DEFAULT NULL,
  `Fecha` date DEFAULT NULL,
  `AreaID` int NOT NULL,
  `CantidadTVBox` int DEFAULT NULL,
  `CantidadRepetidor` int DEFAULT NULL,
  `EstadoID` int DEFAULT NULL,
  `FechaCreacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `FechaActualizacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Evaluacion` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `UsuarioID` int DEFAULT NULL,
  `cajaID` int DEFAULT NULL,
  `CondominioID` int DEFAULT NULL,
  `tipo_cliente` enum('Nuevo','Existente') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'Nuevo',
  PRIMARY KEY (`ClienteID`),
  KEY `DepartamentoID` (`DepartamentoID`),
  KEY `ProvinciaID` (`ProvinciaID`),
  KEY `DistritoID` (`DistritoID`),
  KEY `TipoServicioID` (`TipoServicioID`),
  KEY `PlanID` (`PlanID`),
  KEY `PromoID` (`PromoID`),
  KEY `AreaID` (`AreaID`),
  KEY `FK_EstadoCliente` (`EstadoID`),
  KEY `fk_cliente_usuario` (`UsuarioID`),
  KEY `fk_cajanap` (`cajaID`),
  KEY `fk_condominio` (`CondominioID`),
  CONSTRAINT `fk_clientes_areas` FOREIGN KEY (`AreaID`) REFERENCES `areas` (`AreaID`),
  CONSTRAINT `fk_clientes_cajas` FOREIGN KEY (`cajaID`) REFERENCES `cajas` (`cajaID`),
  CONSTRAINT `fk_clientes_condominio` FOREIGN KEY (`CondominioID`) REFERENCES `condominios` (`CondominioID`),
  CONSTRAINT `fk_clientes_departamento` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamentos` (`DepartamentoID`),
  CONSTRAINT `fk_clientes_distrito` FOREIGN KEY (`DistritoID`) REFERENCES `distritos` (`DistritoID`),
  CONSTRAINT `fk_clientes_estado` FOREIGN KEY (`EstadoID`) REFERENCES `estadoscliente` (`EstadoID`),
  CONSTRAINT `fk_clientes_planes` FOREIGN KEY (`PlanID`) REFERENCES `planes` (`PlanID`),
  CONSTRAINT `fk_clientes_promociones` FOREIGN KEY (`PromoID`) REFERENCES `promociones` (`PromoID`),
  CONSTRAINT `fk_clientes_provincia` FOREIGN KEY (`ProvinciaID`) REFERENCES `provincias` (`ProvinciaID`),
  CONSTRAINT `fk_clientes_tiposervicios` FOREIGN KEY (`TipoServicioID`) REFERENCES `tiposservicios` (`TipoServicioID`),
  CONSTRAINT `fk_clientes_usuarios` FOREIGN KEY (`UsuarioID`) REFERENCES `usuarios` (`UsuarioID`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=290 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (259,'149964216','44835869','GIANCARLO FABIAN SOLANO TORRES','URB. EL PINAR PARCELA I   CALLE 16 B2-05',1,1,1,'-11.9203887,-77.0550473','916092161','giancarlosst@gmail.com','FB',NULL,5,1,1,'2024-12-13',2,0,0,3,'2024-12-14 00:09:48','2025-01-22 08:47:14','rojo',16,1,NULL,'Existente'),(260,'abcdsddd','09739247','preesa','CONDOMINIO LAS ACACIAS TORRE 3 PISO 13 DEP 1303',1,1,1,'-11,-77','930471406','renaty@hotmaillll.com','Faceboock',NULL,4,1,1,'2025-01-19',2,0,10,8,'2024-12-14 00:18:38','2025-01-22 14:46:44','amarillo',28,1,NULL,'Existente'),(261,'149964216','44835869','GIANCARLO FABIAN SOLANO TORRES','URB. EL PINAR PARCELA I   CALLE 16 B2-05',1,1,1,'-11.9203887,-77.0550473','916092161','giancarlosst@gmail.com','FB',NULL,7,1,1,'2024-12-13',2,0,0,3,'2024-12-14 00:30:41','2024-12-14 00:30:41','rojo',28,1,NULL,'Existente'),(262,'87654321','DNI','Cesar Juan Perez Gamboa','Av. Siempre Viva 742',2,1,2,'-12.046374,-77.042793','987654321','juan.perez@example.com','Pedro','Pedro Martínez',1,2,3,'2024-12-11',1,2,1,1,'2024-12-14 21:38:01','2024-12-14 21:38:01','Verde',74,1,3,'Existente'),(263,'41747245','DNI','ARTHUR JONNATHAN DELGADO BURGA','mi casita',1,1,4,'-11,-77','963852741','lima@correo.com','FB',NULL,4,8,3,'2024-12-14',1,0,0,3,'2024-12-14 21:39:51','2024-12-14 21:39:51','verde',16,46,NULL,'Nuevo'),(264,'149966501','49032232','CARRASCO CALDERON MILKA MELISA ','JR GUAYANA CON ASUNCIÓN #124 URB EL PARRAL ',1,1,1,'-11.953993, -77.054091','910463807','carrascomilka.93@Gmail.com','FB',NULL,4,1,1,'2024-12-14',2,0,0,3,'2024-12-14 22:00:20','2024-12-14 22:00:20','rojo',28,1,NULL,'Existente'),(265,'41747245','DNI','ARTHUR JONNATHAN DELGADO BURGA','los olivos',1,1,1,'-11,-77','963852741','correo@corre.com','FB',NULL,3,8,3,'2024-12-15',1,0,0,NULL,'2024-12-16 20:40:20','2024-12-16 22:11:50','verde',16,47,NULL,'Nuevo'),(286,'149966527','09739247','SISLEY MONTERO RENATO JOSE','CONDOMINIO LAS ACACIAS TORRE 3 PISO 13 DEP 1303',1,1,1,'-11,-77','930471406','renatowey@hotmail.com','FB',NULL,4,1,1,'2025-01-21',2,0,0,8,'2025-01-22 02:44:20','2025-01-22 09:09:37','rojo',15,1,NULL,'Nuevo'),(287,'149966527','987799247','SISLEY MONTERO RENATO JOSE','COND LAS ACACIAS TORRE 3 PISO 13 DEP 1303',1,1,1,'-11.77','993447486','renato@example.com','FB',NULL,4,1,1,'2025-01-21',2,0,0,1,'2025-01-22 07:09:01','2025-01-22 07:09:01','ocho',13,1,NULL,'Nuevo'),(289,'abcdsddd','09739247','preesa','CONDOMINIO LAS ACACIAS TORRE 3 PISO 13 DEP 1303',1,1,1,'-11,-77','930471406','renaty@hotmaillll.com','Faceboock',NULL,4,1,1,'2025-01-19',2,0,10,8,'2025-01-22 09:43:26','2025-01-22 14:47:12','amarillo',16,1,NULL,'Existente');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientesusuarios`
--

DROP TABLE IF EXISTS `clientesusuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientesusuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `UsuarioID` int NOT NULL,
  `ClienteID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_clientesusuarios_usuarios` (`UsuarioID`),
  KEY `fk_clientesusuarios_clientes` (`ClienteID`),
  CONSTRAINT `fk_clientesusuarios_clientes` FOREIGN KEY (`ClienteID`) REFERENCES `clientes` (`ClienteID`),
  CONSTRAINT `fk_clientesusuarios_usuarios` FOREIGN KEY (`UsuarioID`) REFERENCES `usuarios` (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientesusuarios`
--

LOCK TABLES `clientesusuarios` WRITE;
/*!40000 ALTER TABLE `clientesusuarios` DISABLE KEYS */;
INSERT INTO `clientesusuarios` VALUES (2,16,259),(5,15,260),(6,16,287);
/*!40000 ALTER TABLE `clientesusuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentariosclientes`
--

DROP TABLE IF EXISTS `comentariosclientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentariosclientes` (
  `ComentarioID` int NOT NULL AUTO_INCREMENT,
  `ClienteID` int DEFAULT NULL,
  `UsuarioID` int DEFAULT NULL,
  `Comentario` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `FechaHora` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ComentarioID`),
  KEY `ClienteID` (`ClienteID`),
  KEY `UsuarioID` (`UsuarioID`),
  CONSTRAINT `fk_comentariosclientes_clientes` FOREIGN KEY (`ClienteID`) REFERENCES `clientes` (`ClienteID`),
  CONSTRAINT `fk_comentariosclientes_usuarios` FOREIGN KEY (`UsuarioID`) REFERENCES `usuarios` (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=411 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentariosclientes`
--

LOCK TABLES `comentariosclientes` WRITE;
/*!40000 ALTER TABLE `comentariosclientes` DISABLE KEYS */;
INSERT INTO `comentariosclientes` VALUES (401,260,16,'Cliente requiere cambio de nuevo plancito rrr jajaja.','2025-01-19 04:35:59'),(402,260,16,'Cliente requiere cambio de nuevo plancito jajaja pancita bbbrrrr jajaja.','2025-01-19 05:18:31'),(407,260,16,'Prueba automática de fecha y hora','2025-01-19 04:56:58'),(408,260,16,'Prueba de fecha y hora','2025-01-19 05:02:52'),(409,260,16,'pereza y hambre tengo jajaja.','2025-01-22 10:42:08'),(410,260,15,'Prueba de fecha y hora qqqq','2025-01-19 05:17:59');
/*!40000 ALTER TABLE `comentariosclientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `condominios`
--

DROP TABLE IF EXISTS `condominios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `condominios` (
  `CondominioID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `DistritoID` int NOT NULL,
  PRIMARY KEY (`CondominioID`),
  KEY `DistritoID` (`DistritoID`),
  CONSTRAINT `fk_condominios_distritos` FOREIGN KEY (`DistritoID`) REFERENCES `distritos` (`DistritoID`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `condominios`
--

LOCK TABLES `condominios` WRITE;
/*!40000 ALTER TABLE `condominios` DISABLE KEYS */;
INSERT INTO `condominios` VALUES (1,'SIN ASIGNAR',1),(2,'ACACIAS',1),(3,'ALAMEDA DEL RIMAC \"A\" 1E',1),(4,'ALAMEDA DEL RIMAC \"A\" 2E',1),(5,'ALAMEDA DEL RIMAC \"B\" 1E',1),(6,'ALAMEDA DEL RIMAC \"B\" 2E',1),(7,'ALTOS DEL RIMAC 1',1),(8,'ALTOS DEL RIMAC 2',1),(9,'ALTOS DEL RIMAC 3',1),(10,'ALTOS DEL RIMAC 4',1),(11,'ALTOS DEL RIMAC 5',1),(12,'BUGANVILLA',1),(13,'CEREZOS',1),(14,'CIPRESES',1),(15,'CIUDAD VERDE',1),(16,'ENCANTO DE SAN DIEGO',1),(17,'GERANIOS',1),(18,'GIRASOLES',1),(19,'GIRASOLES 2',1),(20,'JACARANDA',1),(21,'LAURELES 1',1),(22,'LAURELES 2',1),(23,'LAURELES 3',1),(24,'LAURELES 4',1),(25,'MAGNOLIAS',1),(26,'MAMBO 1',1),(27,'MAMBO 2',1),(28,'MAMBO 3',1),(29,'MAMBO 4',1),(30,'MOLLES',1),(31,'NOGALES',1),(32,'PARQUE DE LOS OLIVOS',1),(33,'PRADERAS DEL RIMAC',1),(34,'TORRES LOS OLIVOS',1),(35,'RESIDENCIAL',1);
/*!40000 ALTER TABLE `condominios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamentos` (
  `DepartamentoID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`DepartamentoID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamentos`
--

LOCK TABLES `departamentos` WRITE;
/*!40000 ALTER TABLE `departamentos` DISABLE KEYS */;
INSERT INTO `departamentos` VALUES (1,'Lima'),(2,'Cusco');
/*!40000 ALTER TABLE `departamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `distritos`
--

DROP TABLE IF EXISTS `distritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `distritos` (
  `DistritoID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ProvinciaID` int NOT NULL,
  PRIMARY KEY (`DistritoID`),
  KEY `ProvinciaID` (`ProvinciaID`),
  CONSTRAINT `fk_distritos_provincias` FOREIGN KEY (`ProvinciaID`) REFERENCES `provincias` (`ProvinciaID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `distritos`
--

LOCK TABLES `distritos` WRITE;
/*!40000 ALTER TABLE `distritos` DISABLE KEYS */;
INSERT INTO `distritos` VALUES (1,'Comas',1),(2,'Puente Piedra',1),(3,'San Martin de Porres',1),(4,'Los Olivios',1),(5,'Rimac',1),(6,'Cusco',2),(7,'San Sebastián',2),(8,'Wanchaq',2),(9,'Santiago',2),(10,'San Jeronimo',2),(11,'Independencia',1);
/*!40000 ALTER TABLE `distritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estadoscliente`
--

DROP TABLE IF EXISTS `estadoscliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estadoscliente` (
  `EstadoID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`EstadoID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estadoscliente`
--

LOCK TABLES `estadoscliente` WRITE;
/*!40000 ALTER TABLE `estadoscliente` DISABLE KEYS */;
INSERT INTO `estadoscliente` VALUES (1,'REPROGRAMADO'),(2,'TERMINADO'),(3,'PENDIENTE'),(4,'EN EJECUCION'),(5,'AMPLIACION'),(6,'SEGUIMIENTO'),(7,'OBSERVADO'),(8,'URGENTE'),(9,'CANCELADO');
/*!40000 ALTER TABLE `estadoscliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_sesiones`
--

DROP TABLE IF EXISTS `log_sesiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_sesiones` (
  `LogID` int NOT NULL AUTO_INCREMENT,
  `UsuarioID` int NOT NULL,
  `HoraInicio` datetime NOT NULL,
  `HoraFin` datetime DEFAULT NULL,
  `TiempoSesion` time DEFAULT NULL,
  PRIMARY KEY (`LogID`),
  KEY `UsuarioID` (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=966 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_sesiones`
--

LOCK TABLES `log_sesiones` WRITE;
/*!40000 ALTER TABLE `log_sesiones` DISABLE KEYS */;
INSERT INTO `log_sesiones` VALUES (890,21,'2024-12-13 11:39:18',NULL,NULL),(891,13,'2024-12-13 11:39:33',NULL,NULL),(892,21,'2024-12-13 12:04:22',NULL,NULL),(893,13,'2024-12-13 12:14:05',NULL,NULL),(894,13,'2024-12-13 12:29:45',NULL,NULL),(895,13,'2024-12-13 12:31:21',NULL,NULL),(896,13,'2024-12-13 12:36:24',NULL,NULL),(897,21,'2024-12-13 13:49:19',NULL,NULL),(898,16,'2024-12-13 14:05:51',NULL,NULL),(899,28,'2024-12-13 14:06:35',NULL,NULL),(900,15,'2024-12-13 14:06:59',NULL,NULL),(901,28,'2024-12-13 14:09:06',NULL,NULL),(902,28,'2024-12-13 14:18:05',NULL,NULL),(903,28,'2024-12-14 15:09:50',NULL,NULL),(904,74,'2024-12-14 15:11:44',NULL,NULL),(905,74,'2024-12-14 15:23:10',NULL,NULL),(906,74,'2024-12-14 15:36:02',NULL,NULL),(907,74,'2024-12-14 15:43:33',NULL,NULL),(908,28,'2024-12-14 15:48:25',NULL,NULL),(909,28,'2024-12-14 16:04:50',NULL,NULL),(910,28,'2024-12-14 16:07:24',NULL,NULL),(911,28,'2024-12-14 16:10:30',NULL,NULL),(912,28,'2024-12-14 16:11:58',NULL,NULL),(913,28,'2024-12-14 16:14:56',NULL,NULL),(914,16,'2024-12-14 16:26:44',NULL,NULL),(915,74,'2024-12-14 16:28:19',NULL,NULL),(916,28,'2024-12-14 16:33:01',NULL,NULL),(917,16,'2024-12-14 16:34:35',NULL,NULL),(918,16,'2024-12-14 16:42:53',NULL,NULL),(919,28,'2024-12-14 16:49:59',NULL,NULL),(920,28,'2024-12-14 16:56:08',NULL,NULL),(921,28,'2024-12-14 16:58:47',NULL,NULL),(922,28,'2024-12-14 17:01:43',NULL,NULL),(923,28,'2024-12-14 17:03:47',NULL,NULL),(924,28,'2024-12-14 17:06:22',NULL,NULL),(925,28,'2024-12-14 17:09:16',NULL,NULL),(926,28,'2024-12-14 17:10:57',NULL,NULL),(927,28,'2024-12-14 17:12:20',NULL,NULL),(928,16,'2024-12-14 17:13:02',NULL,NULL),(929,28,'2024-12-14 17:14:32',NULL,NULL),(930,28,'2024-12-14 17:21:33',NULL,NULL),(931,28,'2024-12-14 23:55:56',NULL,NULL),(932,28,'2024-12-14 23:58:22',NULL,NULL),(933,16,'2024-12-15 00:28:46',NULL,NULL),(934,16,'2024-12-15 01:15:10',NULL,NULL),(935,16,'2024-12-15 01:18:09',NULL,NULL),(936,16,'2024-12-16 14:24:24',NULL,NULL),(937,28,'2024-12-16 14:58:40',NULL,NULL),(938,16,'2024-12-16 14:59:48',NULL,NULL),(939,15,'2024-12-16 15:00:49',NULL,NULL),(940,28,'2024-12-16 15:01:19',NULL,NULL),(941,28,'2024-12-16 15:01:37',NULL,NULL),(942,16,'2024-12-16 15:02:10',NULL,NULL),(943,28,'2024-12-16 15:34:14',NULL,NULL),(944,28,'2024-12-16 15:35:57',NULL,NULL),(945,16,'2024-12-16 15:38:01',NULL,NULL),(946,16,'2024-12-16 15:39:50',NULL,NULL),(947,28,'2024-12-16 15:43:01',NULL,NULL),(948,28,'2024-12-16 15:54:54',NULL,NULL),(949,28,'2024-12-16 15:56:42',NULL,NULL),(950,28,'2024-12-16 15:58:46',NULL,NULL),(951,28,'2024-12-16 16:04:44',NULL,NULL),(952,28,'2024-12-16 16:08:19',NULL,NULL),(953,28,'2024-12-16 16:09:25',NULL,NULL),(954,28,'2024-12-16 16:10:47',NULL,NULL),(955,28,'2024-12-16 16:14:00',NULL,NULL),(956,28,'2024-12-16 16:17:13',NULL,NULL),(957,16,'2024-12-16 16:19:57',NULL,NULL),(958,16,'2024-12-16 16:36:24',NULL,NULL),(959,16,'2024-12-16 16:40:20',NULL,NULL),(960,16,'2024-12-16 17:11:02',NULL,NULL),(961,16,'2024-12-16 17:11:27',NULL,NULL),(962,16,'2024-12-16 19:07:33',NULL,NULL),(963,28,'2024-12-16 19:07:56',NULL,NULL),(964,16,'2024-12-16 20:08:17',NULL,NULL),(965,16,'2024-12-16 20:24:25',NULL,NULL);
/*!40000 ALTER TABLE `log_sesiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planes`
--

DROP TABLE IF EXISTS `planes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planes` (
  `PlanID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `FechaInicio` date DEFAULT NULL,
  `FechaFin` date DEFAULT NULL,
  `Estado` enum('Activo','Inactivo') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'Inactivo',
  PRIMARY KEY (`PlanID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planes`
--

LOCK TABLES `planes` WRITE;
/*!40000 ALTER TABLE `planes` DISABLE KEYS */;
INSERT INTO `planes` VALUES (1,'Plan','2024-01-01','2026-02-01','Activo'),(2,'Plan Estándar','2024-02-01','2024-10-30','Activo'),(3,'Plan Premium','2024-03-01','2024-09-30','Inactivo'),(4,'Plan Empresarial','2024-01-15','2024-10-24','Activo'),(5,'Plan Familiar','2024-04-01','2024-11-30','Activo'),(6,'Plan Avanzado Plus','2024-05-01','2024-12-31','Activo'),(8,'SIH_600','2024-11-01','2024-12-31','Activo'),(9,'SIH_300','2024-11-01','2024-12-31','Activo'),(10,'COMERCIAL_600','2024-11-01','2024-12-31','Activo'),(11,'SIH_200','2024-11-01','2024-12-31','Activo'),(12,'SIH_100','2024-11-01','2024-12-31','Activo'),(13,'SIH_800','2024-11-01','2024-12-31','Activo');
/*!40000 ALTER TABLE `planes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promociones`
--

DROP TABLE IF EXISTS `promociones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promociones` (
  `PromoID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `FechaInicio` date DEFAULT NULL,
  `FechaFin` date DEFAULT NULL,
  `Estado` enum('Activo','Inactivo') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'Inactivo',
  PRIMARY KEY (`PromoID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promociones`
--

LOCK TABLES `promociones` WRITE;
/*!40000 ALTER TABLE `promociones` DISABLE KEYS */;
INSERT INTO `promociones` VALUES (1,'Promo 10%','2024-01-01','2024-12-23','Activo'),(2,'Promo 20%','2024-02-01','2024-12-23','Activo'),(3,'Promo 30%','2024-01-01','2024-12-30','Activo'),(7,'Descuento Navidad','2024-12-01','2024-12-03','Activo');
/*!40000 ALTER TABLE `promociones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincias`
--

DROP TABLE IF EXISTS `provincias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provincias` (
  `ProvinciaID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `DepartamentoID` int NOT NULL,
  PRIMARY KEY (`ProvinciaID`),
  KEY `DepartamentoID` (`DepartamentoID`),
  CONSTRAINT `fk_provincias_departamentos` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamentos` (`DepartamentoID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincias`
--

LOCK TABLES `provincias` WRITE;
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` VALUES (1,'Lima',1),(2,'Cusco',2),(10,'Provincia X',1);
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `RolID` int NOT NULL AUTO_INCREMENT,
  `NombreRol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`RolID`),
  UNIQUE KEY `NombreRol` (`NombreRol`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Administrador'),(5,'Instalador'),(8,'Noc'),(6,'Soporte'),(2,'Superadmin'),(7,'Tac'),(3,'Tecnico'),(4,'Vendedor');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiposservicios`
--

DROP TABLE IF EXISTS `tiposservicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiposservicios` (
  `TipoServicioID` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`TipoServicioID`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiposservicios`
--

LOCK TABLES `tiposservicios` WRITE;
/*!40000 ALTER TABLE `tiposservicios` DISABLE KEYS */;
INSERT INTO `tiposservicios` VALUES (1,'SPT DECO'),(2,'INTERNET + DECO'),(3,'INTERNET + MESH + DECO'),(4,'SPT LENTITUD'),(5,'INTERNET'),(6,'RECOGER ROUTER'),(7,'CAMBIO DE ROUTER'),(8,'SOLO MESH'),(9,'SPT INTERNET'),(10,'SPT WIFI'),(11,'SPT DECO'),(12,'A SOLICITUD DEL CLIENTE'),(13,'CABLEADO UTP'),(14,'CAMBIO DE CARGADOR'),(15,'ATENUACION'),(16,'CAMBIO DE TITULAR'),(17,'CAMBIO TECNOLOGICO'),(18,'CANALES CONGELADOS'),(19,'CONFIGURACIÓN DE DVR/NVR'),(20,'CONVENIO'),(21,'DIFICULTAD EN EL APLICATIVO MOVIL'),(22,'GPON EMPRENDE PLUS 600 MBPS'),(23,'GPON TV DESCONFIGURADO'),(24,'INSUFICIENCIA DE HARDWARE'),(25,'INT20+BX6M+GTV'),(26,'INT20B12M+REP'),(27,'INT20B6M'),(28,'INT20B6M +GTV'),(29,'INT20B6M+DGOBAS'),(30,'INT20B6M+GTV'),(31,'INT20B6M+L1MAX'),(32,'INT20B6M+REP'),(33,'INTB6M'),(34,'INTB6M+GTV'),(35,'INTERMITENCIA WIFI'),(36,'INTERNET'),(37,'NAVEGACION LENTA'),(38,'BAJA COBERTURA WIFI'),(39,'PROBLEMA EQUIPO DEL CLIENTE'),(40,'RECOGER CONTRATO'),(41,'RECOGER ROUTER'),(42,'RECOGER ROUTER + MESH'),(43,'RECOGER ROUTER + REPETIDOR'),(44,'CONTROL DE CHROME CAST'),(45,'REPETIDOR WIFI  + CABLE DE UTP'),(46,'ROUTER ALARMADO'),(47,'SIN ACCESO A INTERNET'),(48,'SIN SEÑAL TV'),(49,'SOPORTE GPONTV'),(50,'SPT DECO'),(51,'SPT IPTV'),(52,'SPT OFFLINE'),(53,'SPT REPETIDOR'),(54,'TRASLADO EXTERNO'),(55,'TRASLADO INTERNO'),(56,'TVBOX DESCONFIGURADO'),(57,'VENTA DE REPETIDOR Y CABLE DE UTP');
/*!40000 ALTER TABLE `tiposservicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `UsuarioID` int NOT NULL AUTO_INCREMENT,
  `NombreUsuario` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Contrasena` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Nombres` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Apellidos` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `TipoDocumento` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `NumeroIdentificacion` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Estado` enum('activo','inactivo') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT 'activo',
  `Email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `DepartamentoID` int DEFAULT NULL,
  PRIMARY KEY (`UsuarioID`),
  KEY `FK_Usuarios_departamentos` (`DepartamentoID`),
  CONSTRAINT `FK_Usuarios_departamentos` FOREIGN KEY (`DepartamentoID`) REFERENCES `departamentos` (`DepartamentoID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (13,'flavio','flavio123','Flavio Zapata',NULL,'DNI','123456578','activo',NULL,1),(14,'Cesar','cesar123','Cesar Espinoza',NULL,'DNI','12345678','activo','cesar@gmail.com',2),(15,'kelvin','kelvin123','Kelvin Kilo',NULL,'DNI','12345678','activo','kelvin@gmail.com',1),(16,'norelia','norelia123','Norelia Gonzaga',NULL,'DNI','12345678','activo','noreliagonzaga@gmail.com',1),(20,'tecnico4','tecnico4','TL - NO ASIGNADO',NULL,'','','activo','',1),(26,'TECNICO NO ASIGNADO','TECNICO NO ASIGNADO','TC - NO ASIGNADO',NULL,'','','activo',NULL,2),(28,'diego','diego123','Diego Flores',NULL,'DNI','1234567','activo','diegoflores@gmail.com',1),(74,'SL - NO ASIGNADO BETA8888888888888888','1234568','SL - NO ASIGNADO',NULL,'','','activo','',1),(75,'SC - NO ASIGNADO','123456','SC - NO ASIGNADO',NULL,'','','activo','',2);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuariosroles`
--

DROP TABLE IF EXISTS `usuariosroles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuariosroles` (
  `usuariosroles_id` int NOT NULL AUTO_INCREMENT,
  `UsuarioID` int NOT NULL,
  `RolID` int NOT NULL,
  `estado` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`usuariosroles_id`,`UsuarioID`,`RolID`),
  UNIQUE KEY `UsuarioID` (`UsuarioID`,`RolID`),
  KEY `RolID` (`RolID`),
  KEY `RolPersonalizadoID` (`estado`),
  KEY `FK_usuariosroles_Usuario_idx` (`UsuarioID`),
  CONSTRAINT `FK_usuariosroles_roles` FOREIGN KEY (`RolID`) REFERENCES `roles` (`RolID`),
  CONSTRAINT `FK_usuariosroles_Usuarios` FOREIGN KEY (`UsuarioID`) REFERENCES `usuarios` (`UsuarioID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuariosroles`
--

LOCK TABLES `usuariosroles` WRITE;
/*!40000 ALTER TABLE `usuariosroles` DISABLE KEYS */;
INSERT INTO `usuariosroles` VALUES (3,15,3,1),(6,16,2,1);
/*!40000 ALTER TABLE `usuariosroles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-22  5:47:30
