USE dev; -- USE test;

CREATE TABLE Environment (
	server VARCHAR(40) PRIMARY KEY,
	ip_address VARCHAR(17)
);

CREATE TABLE App (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	description VARCHAR(100),
	server VARCHAR(40), CONSTRAINT fk_app_server FOREIGN KEY (server) REFERENCES Environment(server)
);

CREATE TABLE EventType (
	type VARCHAR(30) PRIMARY KEY,
	description VARCHAR(70)
);

CREATE TABLE Person (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(50),
	login VARCHAR(20)
	-- more will be added in future versions
);

CREATE TABLE ItemType (
	type VARCHAR(30) PRIMARY KEY,
	model VARCHAR(50)
);

CREATE TABLE Item (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	item_type VARCHAR(30), CONSTRAINT fk_item_type FOREIGN KEY (item_type) REFERENCES ItemType(type),
	ip_address VARCHAR(17),
	mac_address VARCHAR(12)
);

CREATE TABLE Event (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	instant DATETIME,
	event_type VARCHAR(30), CONSTRAINT fk_event_type FOREIGN KEY (event_type) REFERENCES EventType(type)
);

CREATE TABLE Passage (
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	event_id INTEGER, CONSTRAINT fk_passage_event FOREIGN KEY (event_id) REFERENCES Event(id),
	app_id INTEGER, CONSTRAINT fk_passage_app FOREIGN KEY (app_id) REFERENCES App(id),
	person_id INTEGER, CONSTRAINT fk_passage_person FOREIGN KEY (person_id) REFERENCES Person(id),
	item_id INTEGER, CONSTRAINT fk_passage_item FOREIGN KEY (item_id) REFERENCES Item(id),
	start_time DATETIME NOT NULL,
	end_time DATETIME
);

CREATE TABLE PersonItems (
	person_id INTEGER, CONSTRAINT fk_personitems_person FOREIGN KEY (person_id) REFERENCES Person(id),
	item_id INTEGER, CONSTRAINT fk_personitems_item FOREIGN KEY (item_id) REFERENCES Item(id),
	PRIMARY KEY (person_id, item_id)
);