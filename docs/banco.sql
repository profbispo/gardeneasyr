-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema gardeneasy
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gardeneasy
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gardeneasy` DEFAULT CHARACTER SET utf8 ;
USE `gardeneasy` ;

-- -----------------------------------------------------
-- Table `gardeneasy`.`modules`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gardeneasy`.`modules` (
  `Module_ID` INT NOT NULL,
  `Module_Description` TEXT NULL,
  `Module_Name` VARCHAR(60) NULL,
  `Module_Status` ENUM('A', 'I') NOT NULL DEFAULT 'I' COMMENT '[\'Active\'|\'Inactive\']',
  `Module_StartValue` CHAR(40) NOT NULL DEFAULT 'undefined',
  `Module_EndValue` CHAR(40) NOT NULL DEFAULT 'undefined',
  PRIMARY KEY (`Module_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gardeneasy`.`module_data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gardeneasy`.`module_data` (
  `ModuleData_ID` BIGINT NOT NULL AUTO_INCREMENT,
  `Module_ID` INT NOT NULL,
  `ModuleData_Value` CHAR(40) NULL,
  `ModuleData_DateTime` TIMESTAMP NOT NULL DEFAULT current_timestamp,
  `ModuleData_Processed` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`ModuleData_ID`),
  INDEX `fk_module_data_modules_idx` (`Module_ID` ASC),
  CONSTRAINT `fk_module_data_modules`
    FOREIGN KEY (`Module_ID`)
    REFERENCES `gardeneasy`.`modules` (`Module_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gardeneasy`.`events`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `gardeneasy`.`events` (
  `ModuleData_ID` BIGINT NOT NULL,
  `Module_ID` INT NOT NULL,
  `Event_Description` TEXT NULL,
  `Event_Name` CHAR(20) NOT NULL DEFAULT 'undefined',
  `Event_Date` TIMESTAMP NOT NULL DEFAULT current_timestamp,
  `Module_ID_Affected` INT NULL,
  PRIMARY KEY (`ModuleData_ID`, `Module_ID`),
  INDEX `fk_events_module_data1_idx` (`ModuleData_ID` ASC),
  INDEX `fk_events_modules1_idx` (`Module_ID` ASC),
  INDEX `fk_events_modules2_idx` (`Module_ID_Affected` ASC),
  CONSTRAINT `fk_events_module_data1`
    FOREIGN KEY (`ModuleData_ID`)
    REFERENCES `gardeneasy`.`module_data` (`ModuleData_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_events_modules1`
    FOREIGN KEY (`Module_ID`)
    REFERENCES `gardeneasy`.`modules` (`Module_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_events_modules2`
    FOREIGN KEY (`Module_ID_Affected`)
    REFERENCES `gardeneasy`.`modules` (`Module_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
