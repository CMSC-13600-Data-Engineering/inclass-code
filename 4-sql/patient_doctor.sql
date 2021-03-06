
CREATE TABLE patient (
	patient_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	doctor_id INTEGER NOT NULL,
   FOREIGN KEY (doctor_id) REFERENCES doctor (doctor_id)
);

CREATE TABLE doctor (
	doctor_id INTEGER PRIMARY KEY,
	doctor_name TEXT NOT NULL,
	doctor_office TEXT NOT NULL
);

INSERT INTO doctor (doctor_id, doctor_name, doctor_office)
VALUES(1,'Davis Helmans','Dy 146');

INSERT INTO doctor (doctor_id, doctor_name, doctor_office)
VALUES(2,'Sarah Cohen','Ax 132');

INSERT INTO doctor (doctor_id, doctor_name, doctor_office)
VALUES(3,'Jenny Taylor','Ax 151');


INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(1,'John','Smith', 1);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(2,'Sally','Hemmings', 1);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(3,'Alice','Taylor', 2);

INSERT INTO patient (patient_id, first_name, last_name, doctor_id)
VALUES(4,'Bob','Axelrod', 3);
