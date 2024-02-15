USE hbtn_0c_0;

-- Convert the table's charset and collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the charset and collation of the 'name' field
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
