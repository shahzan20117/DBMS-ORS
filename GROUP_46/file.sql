-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: ORS1
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

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
-- Temporary view structure for view `Product_Reviews`
--

DROP TABLE IF EXISTS `Product_Reviews`;
/*!50001 DROP VIEW IF EXISTS `Product_Reviews`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Product_Reviews` AS SELECT 
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `review_comment`,
 1 AS `rating`,
 1 AS `review_date`,
 1 AS `seller_id`,
 1 AS `product_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `Quantity_Of_product_On_Sale`
--

DROP TABLE IF EXISTS `Quantity_Of_product_On_Sale`;
/*!50001 DROP VIEW IF EXISTS `Quantity_Of_product_On_Sale`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Quantity_Of_product_On_Sale` AS SELECT 
 1 AS `product_id`,
 1 AS `quantity_available`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `Seller_Sales`
--

DROP TABLE IF EXISTS `Seller_Sales`;
/*!50001 DROP VIEW IF EXISTS `Seller_Sales`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Seller_Sales` AS SELECT 
 1 AS `seller_id`,
 1 AS `final_cost`,
 1 AS `delivery_status`,
 1 AS `return_status`,
 1 AS `orders_quantity`,
 1 AS `city`,
 1 AS `payment_method`,
 1 AS `place_status`,
 1 AS `orders_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `belongTo`
--

DROP TABLE IF EXISTS `belongTo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `belongTo` (
  `product_id` int NOT NULL,
  `sub_category` varchar(50) NOT NULL,
  PRIMARY KEY (`product_id`,`sub_category`),
  KEY `sub_category` (`sub_category`),
  CONSTRAINT `belongTo_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `belongTo_ibfk_2` FOREIGN KEY (`sub_category`) REFERENCES `subCategory` (`sub_category`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `belongTo`
--

LOCK TABLES `belongTo` WRITE;
/*!40000 ALTER TABLE `belongTo` DISABLE KEYS */;
INSERT INTO `belongTo` VALUES (20,'Bottle'),(1,'Breads'),(18,'Breads'),(6,'Confectionery'),(8,'Confectionery'),(3,'cookies'),(42,'cookies'),(12,'Cookware'),(13,'Cookware'),(16,'Dairy'),(19,'Drinks'),(38,'Drinks'),(17,'Flour'),(9,'Fruit'),(10,'Fruit'),(13,'Furniture'),(15,'Furniture'),(14,'Meat'),(4,'Notebooks'),(7,'Notebooks'),(11,'Nuts'),(7,'Pens'),(5,'Seasoning'),(18,'Television'),(2,'Vegetables'),(39,'Vegetables'),(40,'Vegetables'),(41,'Vegetables');
/*!40000 ALTER TABLE `belongTo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `wallet` int NOT NULL,
  `customer_password` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `index_name` (`first_name`),
  KEY `index1` (`first_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (2,'Delinda','Noades',50,'YFa0EV51n7Ji'),(3,'Muhammad','Brunstan',47,'NJmd8z'),(4,'Lacy','Scotchmur',4745,'aQ1zwDL'),(5,'Konstantin','Carreck',84,'B7Q8zZlPtUf'),(6,'Ines','Llewelyn',1928,'hrNuFIZNg'),(7,'Trueman','Beneyto',376,'utlHeD6GIos1'),(8,'Hewe','Karran',746,'oNWKKvEb'),(9,'Eden','Dorward',938,'JORHJu9UvN'),(10,'Uri','Davidovsky',238,'H59VSSfxB'),(11,'Wolfie','Plows',1928,'JBVShisPSvZS'),(12,'Mariele','Bonham',833,'ZBRX31'),(13,'Elfreda','Weins',382,'9kLx7A'),(14,'Oberon','Parlot',9238,'OSNvVZhQR4'),(15,'Gage','Megainey',839,'QCsGOzj1b'),(16,'Calypso','Ornils',0,'ZXOPXGpNK'),(17,'Kathleen','Librey',0,'7mYu1pXW1'),(18,'Loretta','Sowersby',98,'jlHHIo'),(19,'Idalina','Dwane',8262,'XDb3lJCuauRO'),(20,'Douglas','Keward',83,'4K9JIHL'),(25,'temon','punba',0,'secret'),(44,'yankovich','bella',0,'yogurtNinja'),(45,'sdhkj','kbscj',0,'ldsvn'),(70,'s','dd',0,'ddd'),(75,'huyt','hjui',0,'password'),(77,'divyansh','singh',0,'hoog booga boo'),(78,'divyansh','singh',0,'tommy'),(79,'dd','ddd',0,'ddd'),(80,'shahzan','ahmad',0,'hunga bunga'),(81,'anas','ahmad',0,'hunga bunga'),(99,'yui','opi',0,'sdafjkb'),(123,'abc','def',0,'ghi'),(776,'cidhns','csna',0,'acsnlcsjk'),(1234,'hg','ahsfd',0,'safdhjk');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `cutomer_orders`
--

DROP TABLE IF EXISTS `cutomer_orders`;
/*!50001 DROP VIEW IF EXISTS `cutomer_orders`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `cutomer_orders` AS SELECT 
 1 AS `place_status`,
 1 AS `delivery_status`,
 1 AS `return_status`,
 1 AS `orders_quantity`,
 1 AS `payment_method`,
 1 AS `final_cost`,
 1 AS `orders_date`,
 1 AS `address_line`,
 1 AS `delivery_date`,
 1 AS `product_name`,
 1 AS `seller_name`,
 1 AS `customer_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `orders_id` int NOT NULL AUTO_INCREMENT,
  `place_status` varchar(40) NOT NULL,
  `delivery_status` varchar(40) NOT NULL,
  `return_status` varchar(40) DEFAULT NULL,
  `orders_quantity` int NOT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `final_cost` int NOT NULL,
  `orders_date` date DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `address_line` varchar(100) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `pin_code` int DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `agent_id` int DEFAULT NULL,
  `seller_id` int NOT NULL,
  `product_id` int NOT NULL,
  `delivery_date` date DEFAULT NULL,
  PRIMARY KEY (`orders_id`),
  KEY `customer_id` (`customer_id`),
  KEY `agent_id` (`agent_id`),
  KEY `seller_id` (`seller_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE SET NULL,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`agent_id`) REFERENCES `shippingAgent` (`agent_id`),
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`),
  CONSTRAINT `orders_ibfk_4` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'true','true','ACCEPTED',1,'WALLET',1,'2021-09-12','2068373568','R S','India','34756 Pawling Junction','Gujarat',395003,6,1,1,1,'2021-10-12'),(3,'true','false','ONGOING',3,'COD',3,'2022-01-30','7485472564','Agraharam','India','7 Memorial Road','Andhra Pradesh',532663,3,3,3,3,NULL),(4,'true','false','ACCEPTED',4,'WALLET',4,'2021-10-01','1189850885','Sadar Bazar','India','20037 Southridge Road','Uttar Pradesh',281002,4,4,4,4,NULL),(5,'true','true','REJECTED',5,'WALLET',5,'2021-03-31','2179948895','Sadar Bazar','India','864 Schmedeman Crossing','Uttar Pradesh',281002,5,5,5,5,'2021-08-07'),(6,'true','true',NULL,7,'COD',456,'2020-03-25','1179848595','New Delhi','India','Kondli bazar street-15','Delhi',110094,8,3,9,9,'2022-01-15'),(7,'true','true',NULL,3,'WALLET',787,'2020-08-20','1169808594','Amritsar','India','234-C angel colony ','Punjab',143001,13,7,15,15,'2021-08-20'),(8,'true','true',NULL,14,'WALLET',1065,'2020-11-17','2269508504','Srinagar','India','Tengpora Batamaloo','Jammu and Kashmir',191131,13,7,15,15,'2021-11-17'),(9,'true','true',NULL,14,'WALLET',7656,'2017-11-17','6068615747','RS','India','390 Norway Maple Street','Gujarat',395003,10,4,4,4,NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `place_order` BEFORE UPDATE ON `orders` FOR EACH ROW BEGIN
	IF old.place_status = "false" AND new.place_status = "true" THEN 
		UPDATE sells SET sells.selling_quantity = sells.selling_quantity - new.orders_quantity WHERE sells.product_id = new.product_id AND sells.seller_id = new.seller_id;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `cancel_return` BEFORE UPDATE ON `orders` FOR EACH ROW BEGIN
	##if calcels the order in transit (the cancel request is accepted immediately and the order is sent back to the seller)
	IF OLD.place_status = "true" AND OLD.delivery_status = "false" AND OLD.return_status = NULL AND NEW.return_status = "ACCEPPTED" THEN
		UPDATE sells SET selling_quantity = selling_quantity + NEW.orders_quantity;
	##if returns the order after delivery and the return request is accepted(i.e. delivery boy confirmes that the product is in good shape)
    ELSEIF OLD.place_status = "true" AND OLD.delivery_status = "true" AND OLD.return_status = "ONGOING" AND NEW.return_status = "ACCEPTED" THEN
		UPDATE sells SET selling_quantity = selling_quantity + NEW.orders_quantity WHERE sells.product_id = NEW.product_id AND sells.seller_id = NEW.seller_id ;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `orders_Info_For_shippingAgent`
--

DROP TABLE IF EXISTS `orders_Info_For_shippingAgent`;
/*!50001 DROP VIEW IF EXISTS `orders_Info_For_shippingAgent`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `orders_Info_For_shippingAgent` AS SELECT 
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `agent_id`,
 1 AS `place_status`,
 1 AS `delivery_status`,
 1 AS `return_status`,
 1 AS `payment_method`,
 1 AS `final_cost`,
 1 AS `orders_date`,
 1 AS `phone`,
 1 AS `city`,
 1 AS `country`,
 1 AS `address_line`,
 1 AS `state`,
 1 AS `pin_code`,
 1 AS `delivery_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `curr_status` varchar(50) NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `product_name` (`product_name`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Cinnamon Buns Sticky','OUT_OF_STOCK'),(2,'Tomato - Green','OUT_OF_STOCK'),(3,'Cookies Cereal Nut','IN_STOCK'),(4,'Classmate Notebook','NO_LONGER_AVAILABLE'),(5,'Herb Du Provence - Primerba','IN_STOCK'),(6,'Pastry - Cherry Danish - Mini','NO_LONGER_AVAILABLE'),(7,'Reynolds pen','IN_STOCK'),(8,'Vermacelli - Sprinkles, Assorted','IN_STOCK'),(9,'Fruit Mix - Light','IN_STOCK'),(10,'Blackberries','IN_STOCK'),(11,'Nut - Pine Nuts, Whole','OUT_OF_STOCK'),(12,'Cookware pan','IN_STOCK'),(13,'Foil Cont Round','OUT_OF_STOCK'),(14,'Quail - Jumbo Boneless','IN_STOCK'),(15,'Prashad Sofa','IN_STOCK'),(16,'Cheese - Cream Cheese','OUT_OF_STOCK'),(17,'Shiratamako - Rice Flour','NO_LONGER_AVAILABLE'),(18,'Sony LED TV','IN_STOCK'),(19,'Energy Drink - Redbull 355ml','OUT_OF_STOCK'),(20,'Tupperware Bottle','IN_STOCK'),(38,'sprite','IN_STOCK'),(39,'Tamatar','IN_STOCK'),(40,'Aaloo','IN_STOCK'),(41,'Gajar','IN_STOCK'),(42,'hajmola','IN_STOCK');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productCategory`
--

DROP TABLE IF EXISTS `productCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productCategory` (
  `product_category` varchar(50) NOT NULL,
  PRIMARY KEY (`product_category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productCategory`
--

LOCK TABLES `productCategory` WRITE;
/*!40000 ALTER TABLE `productCategory` DISABLE KEYS */;
INSERT INTO `productCategory` VALUES ('Electronics'),('Food'),('Home'),('Kitchen'),('Office'),('test_cat');
/*!40000 ALTER TABLE `productCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `product_page_For_customer`
--

DROP TABLE IF EXISTS `product_page_For_customer`;
/*!50001 DROP VIEW IF EXISTS `product_page_For_customer`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `product_page_For_customer` AS SELECT 
 1 AS `product_id`,
 1 AS `product_name`,
 1 AS `selling_cost`,
 1 AS `avg_rating`,
 1 AS `discount`,
 1 AS `selling_quantity`,
 1 AS `seller_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `products_Of_subCategory`
--

DROP TABLE IF EXISTS `products_Of_subCategory`;
/*!50001 DROP VIEW IF EXISTS `products_Of_subCategory`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `products_Of_subCategory` AS SELECT 
 1 AS `sub_category`,
 1 AS `product_name`,
 1 AS `curr_status`,
 1 AS `product_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `review_comment` varchar(1000) DEFAULT NULL,
  `review_date` date NOT NULL,
  `customer_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `seller_id` int DEFAULT NULL,
  PRIMARY KEY (`review_id`),
  KEY `customer_id` (`customer_id`),
  KEY `product_id` (`product_id`),
  KEY `seller_id` (`seller_id`),
  CONSTRAINT `review_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE,
  CONSTRAINT `review_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE,
  CONSTRAINT `review_ibfk_3` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES (1,1,'Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.','2021-11-22',6,1,1),(2,2,'Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.','2021-11-07',5,5,5),(4,2,'Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.','2022-02-18',13,15,15),(5,3,'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.','2022-02-16',13,15,15),(6,4,'Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.','2022-02-15',8,9,9);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_avg_rating` AFTER INSERT ON `review` FOR EACH ROW BEGIN
	#SET @avg_value = (SELECT ROUND (AVG(rating), 1) AS avg_rat FROM review WHERE review.seller_id = NEW.seller_id AND review.product_id = NEW.product_id);
    UPDATE sells SET avg_rating = ((SELECT ROUND (AVG(rating), 1) AS avg_rat FROM review WHERE review.seller_id = NEW.seller_id AND review.product_id = NEW.product_id)) WHERE sells.product_id = NEW.product_id AND sells.seller_id = NEW.seller_id;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Temporary view structure for view `reviews_for_seller_product`
--

DROP TABLE IF EXISTS `reviews_for_seller_product`;
/*!50001 DROP VIEW IF EXISTS `reviews_for_seller_product`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `reviews_for_seller_product` AS SELECT 
 1 AS `first_name`,
 1 AS `last_name`,
 1 AS `product_id`,
 1 AS `seller_id`,
 1 AS `rating`,
 1 AS `review_comment`,
 1 AS `review_date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `seller_id` int NOT NULL,
  `seller_name` varchar(50) NOT NULL,
  `curr_status` varchar(50) NOT NULL,
  `seller_password` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES (1,'Morissette-Quigley','WORKING','7oCjO4IWlxTj','8509995211','sarmit0@cyberchimps.com'),(2,'Corwin, Lang and Adams','WORKING','yy5Nul','4604243952','stroyes1@xrea.com'),(3,'Hickle, Kunze and Little','WORKING','7gOv08','6431459636','pandrasch2@ocn.ne.jp'),(4,'Tremblay Inc','NOT_WORKING','zTjgy7mOr','5842268852','mjosiah3@go.com'),(5,'Barrows-Krajcik','WORKING','8H8ueXP','1727363379','ebampton4@symantec.com'),(6,'Baumbach-Rohan','NOT_WORKING','YD65uzZvUr','5225359353','eboutellier5@weibo.com'),(7,'Harber-Saue','NOT_WORKING','Jt6pEL','9256512184','adammarell6@uiuc.edu'),(8,'Schuster Inc','WORKING','AJWmHNVz','4398815564','bmaccourt7@wordpress.com'),(9,'Fay Inc','WORKING','BvdpUcy1k','8958574533','kmussared8@clickbank.net'),(10,'Anderson Inc','WORKING','sQGOgU7x','1737737312','mmettricke9@lycos.com'),(11,'Kautzer, Sporer and Gulgowski','WORKING','4j55VsSbRUr','2719258150','rbilhama@nasa.gov'),(12,'Kessler-Olson','WORKING','aEa2fISV','4048190533','cperesb@eventbrite.com'),(13,'Ziemann LLC','WORKING','kVb661FsS0','1033945785','emaccaughanc@time.com'),(14,'Franecki Inc','WORKING','2DBLbjuTio','6424494691','mbaptistd@mediafire.com'),(15,'Roberts-Kohler','WORKING','R7xZA6kzF7','99','zdivinae@eepurl.com'),(16,'Boyle, Roberts and Bogisich','WORKING','8vXx24ub','4262545796','mjannaschf@twitpic.com'),(17,'Parker and Sons','NOT_WORKING','6lKkCU9O','5129105246','nboolerg@ihg.com'),(18,'Miller-Ruecker','NOT_WORKING','o5Ks0Nuz','1004611761','gquaintonh@vinaora.com'),(19,'Nikolaus-Mayert','WORKING','BCbfqtoMWtxF','6141506543','mpallisteri@kickstarter.com'),(20,'Cremin and Sons','WORKING','OdgiF1','2956854314','beasomj@sogou.com'),(21,'Waters-Stroman','WORKING','T11zMFmX2B','3751635431','sfranceschellik@rakuten.co.jp'),(22,'Goodwin-Bernhard','NOT_WORKING','linU2kzP6dz','5403884349','ckerswelll@amazonaws.com'),(23,'Hamill LLC','NOT_WORKING','tPzMTCIyoEVg','8289928947','bcumberlandm@163.com'),(24,'Fay, Ryan and Macejkovic','NOT_WORKING','WSzGtyY','6807431639','lsweedn@timesonline.co.uk'),(25,'Runte LLC','WORKING','awWHBjfyadP','4125766938','mkilgallono@goodreads.com'),(55,'seller1','WORKING','pass','1234567890','shahzan1@joojle.com'),(89,'seller2','WORKING','password2','78','seller2@hmail.com'),(765,'seller12','WORKING','passwordMania','876578697','seller@hmail.com');
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sells`
--

DROP TABLE IF EXISTS `sells`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sells` (
  `seller_id` int NOT NULL,
  `product_id` int NOT NULL,
  `selling_cost` int DEFAULT NULL,
  `avg_rating` decimal(2,1) NOT NULL,
  `selling_quantity` int NOT NULL,
  `discount` decimal(3,2) NOT NULL,
  PRIMARY KEY (`seller_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `sells_ibfk_1` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`) ON DELETE CASCADE,
  CONSTRAINT `sells_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sells`
--

LOCK TABLES `sells` WRITE;
/*!40000 ALTER TABLE `sells` DISABLE KEYS */;
INSERT INTO `sells` VALUES (1,1,105,1.0,0,0.00),(2,2,283,0.0,0,0.00),(2,3,45,0.0,3,0.00),(3,3,338,0.0,0,0.50),(5,5,527,2.0,5,0.50),(7,7,739,0.0,7,0.70),(8,8,893,0.0,8,0.00),(9,9,9983,4.0,9,0.00),(10,10,1098,0.0,10,0.00),(11,11,105,0.0,0,0.00),(12,12,283,0.0,4,0.00),(13,13,338,0.0,0,0.60),(14,14,438,0.0,9,0.00),(15,10,100,0.0,100,0.40),(15,15,527,2.5,5,0.50),(15,18,100,0.0,100,0.40),(15,41,100,0.0,100,0.40),(16,16,6934,0.0,0,0.00),(18,18,893,0.0,8,0.00),(19,19,9983,0.0,0,0.00),(20,20,1098,0.0,10,0.00),(55,4,300,0.0,200,0.42),(55,7,10,0.0,1000,0.59),(55,10,500,0.0,200,0.50),(55,12,600,0.0,500,0.30),(55,13,9001,0.0,400,0.15),(55,39,500,0.0,100,0.30),(55,42,78,0.0,200,0.56);
/*!40000 ALTER TABLE `sells` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_product_status` AFTER UPDATE ON `sells` FOR EACH ROW BEGIN
	IF	(SELECT SUM(selling_quantity) as product_stock 
		FROM sells 
		WHERE sells.product_id = NEW.product_id) = 0 THEN
        UPDATE product SET curr_status = "OUT_OF_STOCK" WHERE product_id = NEW.product_id; 
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `shippingAgent`
--

DROP TABLE IF EXISTS `shippingAgent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shippingAgent` (
  `agent_id` int NOT NULL,
  `agent_name` varchar(50) NOT NULL,
  `email` varchar(70) NOT NULL,
  `curr_status` varchar(50) NOT NULL,
  `agent_password` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  PRIMARY KEY (`agent_id`),
  KEY `index2` (`agent_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shippingAgent`
--

LOCK TABLES `shippingAgent` WRITE;
/*!40000 ALTER TABLE `shippingAgent` DISABLE KEYS */;
INSERT INTO `shippingAgent` VALUES (1,'Champlin, Breitenberg and Pouros','rbirdis0@opera.com','WORKING','Ny96xoUiS4Ha','2793616367'),(2,'Schmitt, Hermiston and Grimes','jtownley1@ed.gov','NOT_WORKING','lnbrmK','3118483667'),(3,'Ryan-Prohaska','ddoole2@163.com','WORKING','zJV9Hqu52','8097503577'),(4,'O\'Keefe Group','mquennell3@unc.edu','WORKING','vy8Hw5WQos','2967583593'),(5,'Collins-Satterfield','bsire4@unesco.org','NOT_WORKING','sp7pog','6291140841'),(6,'Ferry, Aufderhar and Nikolaus','srodmell5@opera.com','NOT_WORKING','cyFQ3p4IDx','4682844620'),(7,'Oberbrunner, Grimes and Ullrich','odykes6@who.int','WORKING','aQ7et7nYAKS','5787017596'),(8,'Hyatt, Boehm and Douglas','bczapla7@usa.gov','WORKING','Jl4SI5','9111348299'),(9,'Schmitt and Sons','jbanthorpe8@blinklist.com','WORKING','UqK3KeTOlCdj','9987883909'),(10,'Moen, Ankunding and Schoen','vdarrigone9@yolasite.com','NOT_WORKING','18rjFu2ccTz7','7765273256');
/*!40000 ALTER TABLE `shippingAgent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shippingInfo`
--

DROP TABLE IF EXISTS `shippingInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shippingInfo` (
  `country` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pin_code` int NOT NULL,
  `address_line` varchar(500) NOT NULL,
  `customer_id` int NOT NULL,
  `phone` varchar(50) NOT NULL,
  PRIMARY KEY (`country`,`state`,`city`,`pin_code`,`address_line`,`customer_id`,`phone`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `shippingInfo_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shippingInfo`
--

LOCK TABLES `shippingInfo` WRITE;
/*!40000 ALTER TABLE `shippingInfo` DISABLE KEYS */;
INSERT INTO `shippingInfo` VALUES ('India','Andhra Pradesh','Agraharam',532663,'37 Dottie Pass',2,'5137717038'),('India','Uttar Pradesh','Sadar Bazar',281002,'3 Oxford Court',2,'2473437358'),('India','Uttar Pradesh','Sadar Bazar',281002,'356 Mayfield Terrace',3,'1592819500'),('India','Uttar Pradesh','Sadar Bazar',281002,'419 Pond Avenue',3,'2533849096'),('India','Gujarat','R S',395003,'07078 Stephen Alley',4,'5355542770'),('India','Gujarat','R S',395003,'2196 Packers Plaza',4,'4657876905'),('India','Gujarat','R S',395003,'519 Glendale Crossing',5,'5388983546'),('India','Gujarat','R S',395003,'7314 Erie Avenue',5,'5048790793'),('India','Andhra Pradesh','Agraharam',532663,'22 Dawn Alley',6,'2976110194'),('India','Gujarat','R S',395003,'30072 Straubel Road',6,'6832328758'),('India','Andhra Pradesh','Agraharam',532663,'133 Roth Court',7,'8635311608'),('India','Gujarat','R S',395003,'92 Waywood Drive',7,'6432793556'),('India','Gujarat','R S',395003,'6768 Ramsey Drive',8,'2386258222'),('India','Gujarat','R S',395003,'7 Mcguire Alley',8,'2843234645'),('India','Andhra Pradesh','Agraharam',532663,'158 Dapin Alley',9,'7914257003'),('India','Gujarat','R S',395003,'1519 Sachs Terrace',9,'4477967251'),('India','Gujarat','R S',395003,'390 Norway Maple Street',10,'6068615747'),('India','Uttar Pradesh','Sadar Bazar',281002,'87 Prairie Rose Plaza',10,'8266444599'),('India','Uttar Pradesh','Sadar Bazar',281002,'90080 Ryan Street',11,'3462527964'),('India','Andhra Pradesh','Agraharam',532663,'282 Old Gate Parkway',12,'6268082513'),('India','Andhra Pradesh','Agraharam',532663,'9 Goodland Road',13,'1011958808'),('India','Andhra Pradesh','Agraharam',532663,'0 Petterle Terrace',14,'5085649541'),('India','Gujarat','R S',395003,'3054 Spohn Plaza',15,'4559915639'),('India','Andhra Pradesh','Agraharam',532663,'7454 Esch Park',16,'8304275349'),('India','Gujarat','R S',395003,'35110 Namekagon Terrace',17,'4665738745'),('India','Uttar Pradesh','Sadar Bazar',281002,'039 New Castle Place',18,'1972200959'),('India','Andhra Pradesh','Agraharam',532663,'43254 Derek Drive',19,'7006670436'),('India','Andhra Pradesh','Agraharam',532663,'6 Bluestem Circle',20,'1432013055');
/*!40000 ALTER TABLE `shippingInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subCategory`
--

DROP TABLE IF EXISTS `subCategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subCategory` (
  `sub_category` varchar(50) NOT NULL,
  `product_category` varchar(50) NOT NULL,
  PRIMARY KEY (`sub_category`),
  KEY `product_category` (`product_category`),
  CONSTRAINT `subCategory_ibfk_1` FOREIGN KEY (`product_category`) REFERENCES `productCategory` (`product_category`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subCategory`
--

LOCK TABLES `subCategory` WRITE;
/*!40000 ALTER TABLE `subCategory` DISABLE KEYS */;
INSERT INTO `subCategory` VALUES ('Television','Electronics'),('Breads','Food'),('Confectionery','Food'),('cookies','Food'),('Dairy','Food'),('Drinks','Food'),('Flour','Food'),('Fruit','Food'),('Meat','Food'),('Nuts','Food'),('Seasoning','Food'),('Vegetables','Food'),('Furniture','Home'),('Bottle','Kitchen'),('Cookware','Kitchen'),('Notebooks','Office'),('Pens','Office');
/*!40000 ALTER TABLE `subCategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_listings`
--

DROP TABLE IF EXISTS `view_listings`;
/*!50001 DROP VIEW IF EXISTS `view_listings`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_listings` AS SELECT 
 1 AS `seller_id`,
 1 AS `avg_rating`,
 1 AS `selling_cost`,
 1 AS `selling_quantity`,
 1 AS `discount`,
 1 AS `product_id`,
 1 AS `product_name`,
 1 AS `curr_status`*/;
SET character_set_client = @saved_cs_client;

--
-- Dumping events for database 'ORS1'
--

--
-- Dumping routines for database 'ORS1'
--

--
-- Final view structure for view `Product_Reviews`
--

/*!50001 DROP VIEW IF EXISTS `Product_Reviews`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Product_Reviews` AS select `customer`.`first_name` AS `first_name`,`customer`.`last_name` AS `last_name`,`review`.`review_comment` AS `review_comment`,`review`.`rating` AS `rating`,`review`.`review_date` AS `review_date`,`sells`.`seller_id` AS `seller_id`,`sells`.`product_id` AS `product_id` from ((`customer` join `review`) join `sells`) where ((`customer`.`customer_id` = `review`.`customer_id`) and (`review`.`product_id` = `sells`.`product_id`) and (`review`.`seller_id` = `sells`.`seller_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Quantity_Of_product_On_Sale`
--

/*!50001 DROP VIEW IF EXISTS `Quantity_Of_product_On_Sale`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Quantity_Of_product_On_Sale` AS select `sells`.`product_id` AS `product_id`,sum(`sells`.`selling_quantity`) AS `quantity_available` from `sells` group by `sells`.`product_id` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Seller_Sales`
--

/*!50001 DROP VIEW IF EXISTS `Seller_Sales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `Seller_Sales` AS select `orders`.`seller_id` AS `seller_id`,`orders`.`final_cost` AS `final_cost`,`orders`.`delivery_status` AS `delivery_status`,`orders`.`return_status` AS `return_status`,`orders`.`orders_quantity` AS `orders_quantity`,`orders`.`city` AS `city`,`orders`.`payment_method` AS `payment_method`,`orders`.`place_status` AS `place_status`,`orders`.`orders_date` AS `orders_date` from `orders` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `cutomer_orders`
--

/*!50001 DROP VIEW IF EXISTS `cutomer_orders`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `cutomer_orders` AS select `orders`.`place_status` AS `place_status`,`orders`.`delivery_status` AS `delivery_status`,`orders`.`return_status` AS `return_status`,`orders`.`orders_quantity` AS `orders_quantity`,`orders`.`payment_method` AS `payment_method`,`orders`.`final_cost` AS `final_cost`,`orders`.`orders_date` AS `orders_date`,`orders`.`address_line` AS `address_line`,`orders`.`delivery_date` AS `delivery_date`,`product`.`product_name` AS `product_name`,`seller`.`seller_name` AS `seller_name`,`orders`.`customer_id` AS `customer_id` from ((`orders` join `product`) join `seller`) where ((`orders`.`product_id` = `product`.`product_id`) and (`orders`.`seller_id` = `seller`.`seller_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `orders_Info_For_shippingAgent`
--

/*!50001 DROP VIEW IF EXISTS `orders_Info_For_shippingAgent`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `orders_Info_For_shippingAgent` AS select `customer`.`first_name` AS `first_name`,`customer`.`last_name` AS `last_name`,`orders`.`agent_id` AS `agent_id`,`orders`.`place_status` AS `place_status`,`orders`.`delivery_status` AS `delivery_status`,`orders`.`return_status` AS `return_status`,`orders`.`payment_method` AS `payment_method`,`orders`.`final_cost` AS `final_cost`,`orders`.`orders_date` AS `orders_date`,`orders`.`phone` AS `phone`,`orders`.`city` AS `city`,`orders`.`country` AS `country`,`orders`.`address_line` AS `address_line`,`orders`.`state` AS `state`,`orders`.`pin_code` AS `pin_code`,`orders`.`delivery_date` AS `delivery_date` from (`orders` join `customer`) where (`customer`.`customer_id` = `orders`.`orders_id`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `product_page_For_customer`
--

/*!50001 DROP VIEW IF EXISTS `product_page_For_customer`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `product_page_For_customer` AS select `product`.`product_id` AS `product_id`,`product`.`product_name` AS `product_name`,`sells`.`selling_cost` AS `selling_cost`,`sells`.`avg_rating` AS `avg_rating`,`sells`.`discount` AS `discount`,`sells`.`selling_quantity` AS `selling_quantity`,`seller`.`seller_name` AS `seller_name` from ((`product` join `sells`) join `seller`) where ((`product`.`product_id` = `sells`.`product_id`) and (`sells`.`seller_id` = `seller`.`seller_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `products_Of_subCategory`
--

/*!50001 DROP VIEW IF EXISTS `products_Of_subCategory`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `products_Of_subCategory` AS select `subCategory`.`sub_category` AS `sub_category`,`product`.`product_name` AS `product_name`,`product`.`curr_status` AS `curr_status`,`product`.`product_id` AS `product_id` from ((`product` join `belongTo`) join `subCategory`) where ((`product`.`product_id` = `belongTo`.`product_id`) and (`belongTo`.`sub_category` = `subCategory`.`sub_category`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `reviews_for_seller_product`
--

/*!50001 DROP VIEW IF EXISTS `reviews_for_seller_product`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `reviews_for_seller_product` AS select `customer`.`first_name` AS `first_name`,`customer`.`last_name` AS `last_name`,`review`.`product_id` AS `product_id`,`review`.`seller_id` AS `seller_id`,`review`.`rating` AS `rating`,`review`.`review_comment` AS `review_comment`,`review`.`review_date` AS `review_date` from (`review` join `customer`) where (`customer`.`customer_id` = `review`.`customer_id`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `view_listings`
--

/*!50001 DROP VIEW IF EXISTS `view_listings`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_listings` AS select `sells`.`seller_id` AS `seller_id`,`sells`.`avg_rating` AS `avg_rating`,`sells`.`selling_cost` AS `selling_cost`,`sells`.`selling_quantity` AS `selling_quantity`,`sells`.`discount` AS `discount`,`product`.`product_id` AS `product_id`,`product`.`product_name` AS `product_name`,`product`.`curr_status` AS `curr_status` from (`sells` join `product`) where (`product`.`product_id` = `sells`.`product_id`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-27 23:57:42
