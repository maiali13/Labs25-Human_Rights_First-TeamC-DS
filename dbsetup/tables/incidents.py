create_incident_table = """
DROP TABLE IF EXISTS incidents CASCADE;
CREATE TABLE IF NOT EXISTS incidents (
id VARCHAR PRIMARY KEY,
place_id INT,
text VARCHAR NOT NULL,
date VARCHAR,
FOREIGN KEY (place_id) REFERENCES places (id)
);
"""
