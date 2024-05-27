CREATE TABLE Person(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150),
	lastName VARCHAR(150),
	birthDate DATE
);

CREATE TABLE Activity(
	id SERIAL PRIMARY KEY,
	description VARCHAR(150)
);

CREATE TABLE PersonActivity( -- DROP TABLE PersonActivity
	id SERIAL PRIMARY KEY,
	idPerson INTEGER,
	idActivity INTEGER,
	done BOOL DEFAULT false,
	expiringDate DATE DEFAULT NULL,
	CONSTRAINT fk_person FOREIGN KEY(idPerson) REFERENCES Person(id),
	CONSTRAINT fk_activity FOREIGN KEY(idActivity) REFERENCES Activity(id)
);