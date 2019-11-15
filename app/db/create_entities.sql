CREATE TABLE Environment (
	"server" VARCHAR(40) PRIMARY KEY,
	ip_address VARCHAR(17),
);

CREATE TABLE App (
	id INTEGER PRIMARY KEY,
	"name" VARCHAR(50),
	"description" VARCHAR(100),
	"server" VARCHAR(40) FOREIGN KEY REFERENCES Environment,
);

CREATE TABLE EventType (
	"type" VARCHAR(30) PRIMARY KEY,
	"description" VARCHAR(70),
);

CREATE TABLE Person (
	id INTEGER PRIMARY KEY,
	name VARCHAR(50),
	login VARCHAR(20),
	--more will be added in future versions
);

CREATE TABLE ItemType (
	"type" VARCHAR(30) PRIMARY KEY,
	model VARCHAR(50),
);

CREATE TABLE Item (
	id INTEGER PRIMARY KEY,
	item_type VARCHAR(30) FOREIGN KEY REFERENCES ItemType,
	ip_address VARCHAR(17),
	mac_address VARCHAR(12),
);

CREATE TABLE "Event" (
	id INTEGER PRIMARY KEY,
	instant DATETIME,
	event_type VARCHAR(30) FOREIGN KEY REFERENCES EventType,
);

CREATE TABLE Passage (
	id INTEGER PRIMARY KEY,
	event_id INTEGER FOREIGN KEY REFERENCES "Event",
	app_id INTEGER FOREIGN KEY REFERENCES App,
	person_id INTEGER FOREIGN KEY REFERENCES Person,
	item_id INTEGER FOREIGN KEY REFERENCES Item,
	start_time DATETIME NOT NULL,
	end_time DATETIME,
);

CREATE TABLE PersonItems (
	person_id INTEGER FOREIGN KEY REFERENCES Person,
	item_id INTEGER FOREIGN KEY REFERENCES Item,
	PRIMARY KEY (person_id, item_id)
);