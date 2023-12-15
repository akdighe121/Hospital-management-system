create database Hospital;

use Hospital;

CREATE TABLE HOSPITAL (
    nameoftablets VARCHAR(45) NULL,
    Reference_no INT NOT NULL PRIMARY KEY, -- Changed data type to INT
    dose VARCHAR(45) NULL,
    numberoftablets INT NULL, -- Changed data type to INT
    lot VARCHAR(45) NULL,
    issuedate DATE NULL, -- Changed data type to DATE
    expdate DATE NULL, -- Changed data type to DATE
    dailydose VARCHAR(45) NULL,
    storage VARCHAR(45) NULL,
    nhsnumber VARCHAR(45) NULL,
    patientname VARCHAR(45) NULL,
    DOB DATE NULL, -- Changed data type to DATE
    patientaddress VARCHAR(45) NULL
);