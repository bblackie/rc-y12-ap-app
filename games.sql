CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    release_date TEXT NOT NULL,
    platforms TEXT NOT NULL,
    developer TEXT NOT NULL,
    publisher TEXT NOT NULL,
    metacritic_score INTEGER NOT NULL
);
INSERT INTO games (title, genre, release_date, platforms, developer, publisher, metacritic_score) VALUES
('The Legend of Zelda: Breath of the Wild', 'Action-adventure', '2017-03-03', 'Nintendo Switch, Wii U', 'Nintendo', 'Nintendo', 97),
('Elden Ring', 'Action RPG', '2022-02-25', 'PC, PS4, PS5, Xbox One, Xbox Series X/S', 'FromSoftware', 'Bandai Namco Entertainment', 96),
('The Witcher 3: Wild Hunt', 'Action RPG', '2015-05-19', 'PC, PS4, Xbox One, Nintendo Switch', 'CD Projekt Red', 'CD Projekt', 93),
('Grand Theft Auto V', 'Open-world, Action-adventure', '2013-09-17', 'PC, PS3, PS4, PS5, Xbox 360, Xbox One, Xbox Series X/S', 'Rockstar North', 'Rockstar Games', 96),
('Red Dead Redemption 2', 'Action-adventure', '2018-10-26', 'PC, PS4, PS5, Xbox One, Xbox Series X/S', 'Rockstar Games', 'Rockstar Games', 97),
('Cyberpunk 2077', 'Action RPG', '2020-12-10', 'PC, PS4, PS5, Xbox One, Xbox Series X/S', 'CD Projekt Red', 'CD Projekt', 86),
('Minecraft', 'Sandbox, Survival', '2011-11-18', 'PC, PS4, PS5, Xbox One, Xbox Series X/S, Mobile', 'Mojang', 'Mojang', 93),
('Fortnite', 'Battle Royale', '2017-07-21', 'PC, PS4, PS5, Xbox One, Xbox Series X/S, Mobile', 'Epic Games', 'Epic Games', 81),
('God of War', 'Action-adventure', '2018-04-20', 'PC, PS4, PS5', 'Santa Monica Studio', 'Sony Interactive Entertainment', 94),
('Super Mario Odyssey', 'Platformer', '2017-10-27', 'Nintendo Switch', 'Nintendo', 'Nintendo', 97);
