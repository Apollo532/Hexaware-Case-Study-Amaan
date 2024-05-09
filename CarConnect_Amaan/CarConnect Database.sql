CREATE DATABASE Car;
USE Car;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(30),
    LastName VARCHAR(30),
    Email VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255),
    Username VARCHAR(50) UNIQUE,
    Password VARCHAR(255),
    RegistrationDate DATE
);

CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Model VARCHAR(50),
    Make VARCHAR(50),
    Year INT,
    Color VARCHAR(50),
    RegistrationNumber VARCHAR(20) UNIQUE,
    Availability BOOLEAN,
    DailyRate DECIMAL(10, 2)
);

-- Reservation Table
CREATE TABLE Reservations (
    ReservationID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    VehicleID INT,
    StartDate DATE,
    EndDate DATE,
    TotalCost DECIMAL(10, 2),
    Status VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);


CREATE TABLE Admin (
    AdminID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    PhoneNumber VARCHAR(15),
    Username VARCHAR(50) UNIQUE,
    Password VARCHAR(255),
    Role VARCHAR(50),
    JoinDate DATE
);


INSERT INTO Customers (CustomerID, FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate) VALUES
    (1, 'Akira', 'Yamamoto', 'akira.yamamoto@gmail.com', '5551234567', '123 Main St', 'akiray', 'sdfj92#39fj', '2023-01-15'),
    (2, 'Sofia', 'Kumar', 'sofia.kumar@yahoo.com', '5559876543', '456 Elm St', 'sofiak', '3hfs&f8fd3f', '2023-02-20'),
    (3, 'Matteo', 'Santos', 'matteo.santos@outlook.com', '5555555555', '789 Oak St', 'matteos', 'jf72$#@jdfj', '2023-03-25'),
    (4, 'Priya', 'Patel', 'priya.patel@gmail.com', '5551112233', '101 Pine St', 'priyap', '8d&f9jd9ddk', '2023-04-30'),
    (5, 'Lukas', 'Hoffmann', 'lukas.hoffmann@yahoo.com', '5553334444', '202 Cedar St', 'lukash', '0dfJ2jd9f0d', '2023-05-05'),
    (6, 'Yumi', 'Nakamura', 'yumi.nakamura@outlook.com', '5555556666', '303 Maple St', 'yumim', '1h&93jfJdfk', '2023-06-10'),
    (7, 'Aditya', 'Gupta', 'aditya.gupta@gmail.com', '5557778888', '404 Walnut St', 'adityag', 'Jf39jd0$sdj', '2023-07-15'),
    (8, 'Elena', 'Ivanova', 'elena.ivanova@yahoo.com', '5559990000', '505 Pineapple St', 'elenai', 'sdf&j23dfjJ', '2023-08-20');
    

INSERT INTO Vehicles (VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES
    (1,'Toyota Camry', 'Toyota', 2018, 'Black', 'ABC123', 1, 50.00),
    (2, 'Honda Civic', 'Honda', 2019, 'Red', 'DEF456', 1, 60.00),
    (3, 'Ford Mustang', 'Ford', 2020, 'Blue', 'GHI789', 1, 70.00),
    (4, 'Chevrolet Silverado', 'Chevrolet', 2017, 'White', 'JKL012', 1, 80.00),
    (5, 'Tesla Model S', 'Tesla', 2021, 'Silver', 'MNO345', 1, 90.00),
    (6, 'BMW X5', 'BMW', 2022, 'Gray', 'PQR678', 1, 100.00);


INSERT INTO Reservations (ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) VALUES
    (1, 1, 1, '2023-01-20', '2023-01-25', 250.00, 'confirmed'),
    (2, 2, 3, '2023-02-25', '2023-03-05', 560.00, 'confirmed'),
    (3, 3, 5, '2023-03-10', '2023-03-15', 450.00, 'confirmed'),
    (4, 4, 2, '2023-04-05', '2023-04-10', 300.00, 'pending'),
    (5, 5, 4, '2023-05-15', '2023-05-20', 400.00, 'completed'),
    (6, 6, 1, '2023-06-20', '2023-06-25', 300.00, 'pending'),
    (7, 7, 6, '2023-07-05', '2023-07-10', 500.00, 'confirmed'),
    (8, 8, 3, '2023-08-10', '2023-08-15', 420.00, 'completed'),
    (9, 1, 4, '2023-09-05', '2023-09-10', 400.00, 'confirmed'),
    (10, 2, 5, '2023-10-20', '2023-10-25', 450.00, 'confirmed');
    

INSERT INTO Admin (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate) VALUES
    (1, 'John', 'Doe', 'john.doe@gmail.com', '5556667777', 'admin1', 'jf9#3Jsd@', 'super admin', '2022-01-01'),
    (2, 'Rahul', 'Kumar', 'rahul.kumar@yahoo.com', '5557778888', 'admin2', 'Jdf9@3ks9', 'fleet manager', '2022-02-01'),
    (3, 'Maria', 'Garcia', 'maria.garcia@outlook.com', '5558889999', 'admin3', 'sdkf23Jsdf', 'customer support', '2022-03-01'),
    (4, 'Piotr', 'Nowak', 'piotr.nowak@gmail.com', '5559990000', 'admin4', 'Jf93#jds93', 'maintenance', '2022-04-01'),
    (5, 'Yuki', 'Tanaka', 'yuki.tanaka@yahoo.com', '5550001111', 'admin5', 's93J#Jdfk3', 'operations', '2022-05-01');
    
SELECT * FROM Customers;
SELECT * FROM Vehicles;
SELECT * FROM Reservations;
SELECT * FROM Admin;
