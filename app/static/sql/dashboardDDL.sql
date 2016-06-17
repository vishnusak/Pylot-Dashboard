-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema dashboard2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dashboard2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dashboard2` DEFAULT CHARACTER SET utf8 ;
USE `dashboard2` ;

-- -----------------------------------------------------
-- Table `dashboard2`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard2`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `user_level` INT NOT NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dashboard2`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard2`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `for_id` INT NOT NULL,
  `msg_text` TEXT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_messages_users_idx` (`user_id` ASC),
  INDEX `fk_messages_users1_idx` (`for_id` ASC),
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `dashboard2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`for_id`)
    REFERENCES `dashboard2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dashboard2`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dashboard2`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `msg_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `for_id` INT NOT NULL,
  `cmt_text` TEXT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `fk_comments_messages1_idx` (`msg_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  INDEX `fk_comments_users2_idx` (`for_id` ASC),
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`msg_id`)
    REFERENCES `dashboard2`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dashboard2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users2`
    FOREIGN KEY (`for_id`)
    REFERENCES `dashboard2`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
