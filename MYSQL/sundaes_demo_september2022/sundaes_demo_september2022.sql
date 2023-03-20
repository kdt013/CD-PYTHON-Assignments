-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sundaes_demo_september2022
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sundaes_demo_september2022
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sundaes_demo_september2022` DEFAULT CHARACTER SET utf8 ;
USE `sundaes_demo_september2022` ;

-- -----------------------------------------------------
-- Table `sundaes_demo_september2022`.`sundaes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sundaes_demo_september2022`.`sundaes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `flavor` VARCHAR(255) NULL,
  `num_scoops` INT NULL,
  `topping` VARCHAR(255) NULL,
  `sauce` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
