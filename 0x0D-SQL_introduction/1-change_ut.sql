-- To change the CHARACTER SET of a database named htbn_0c_0 to UTF8
USE news;
ALTER DATABASE news CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
