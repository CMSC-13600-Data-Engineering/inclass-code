CREATE TABLE patient (
	patient_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	doctor_id INTEGER NOT NULL
);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(1,'John','Smith', 1);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(2,'Sally','Hemmings', 1);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(3,'Alice','Taylor', 3);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(4,'Bob','Axelrod', 3);
