DROP TABLE IF EXISTS let;

CREATE TABLE tip (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv TEXT NOT NULL
);

CREATE TABLE lokacija (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    naziv TEXT NOT NULL
);

CREATE TABLE let (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  tip INTEGER NOT NULL,
  polazna_lokacija INTEGER NOT NULL,
  dolazna_lokacija INTEGER NOT NULL,
  datum_polaska DATE NOT NULL,

  FOREIGN KEY (tip) REFERENCES tip (id),
  FOREIGN KEY (polazna_lokacija) REFERENCES lokacija (id),
  FOREIGN KEY (dolazna_lokacija) REFERENCES lokacija (id)
);

INSERT INTO tip (naziv) VALUES ("U jednom smjeru"), ("Povratni");
INSERT INTO lokacija (naziv) VALUES ("Banja luka"), ("Mostar"), ("Sarajevo"), ("Tuzla"), ("Zagreb"), ("Beograd"), ("Berlin"), ("Moskva"), ("Pariz"), ("Tokyo")