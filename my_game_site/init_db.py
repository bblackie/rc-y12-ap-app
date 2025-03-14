# init_db.py
import sqlite3

def create_and_populate_db():
    connection = sqlite3.connect('games.db')
    cursor = connection.cursor()

    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS games")

    # Create the 'games' table with three screenshot columns (no video columns)
    cursor.execute("""
        CREATE TABLE games (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            release_date TEXT NOT NULL,
            developer TEXT NOT NULL,
            publisher TEXT NOT NULL,
            metacritic_score INTEGER NOT NULL,
            description TEXT NOT NULL,
            image_url TEXT,
            image_url2 TEXT,
            image_url3 TEXT
        );
    """)

    # Insert sample game data with longer descriptions and three screenshot URLs.
    games_data = [
        (1, 'The Legend of Zelda: Breath of the Wild', 'Action-adventure', '2017-03-03',
         'Nintendo', 'Nintendo', 97,
         'Immerse yourself in a vast, breathtaking world where every corner holds secrets and adventures. Explore ancient ruins, solve intricate puzzles, and battle formidable foes as you rediscover the lost kingdom of Hyrule. This groundbreaking title redefines open-world exploration with its dynamic weather system and physics-based gameplay.',
         'https://static1.srcdn.com/wordpress/wp-content/uploads/2025/01/zelda-botw-link-horseback-with-hyrule-landscape.jpg', 'https://upload.wikimedia.org/wikipedia/en/c/c6/The_Legend_of_Zelda_Breath_of_the_Wild.jpg', 'https://static1.srcdn.com/wordpress/wp-content/uploads/2021/09/BOTW--Pros-Cons-Of-Ignoring-The-Divine-Beasts.jpg'),
        (2, 'Elden Ring', 'Action RPG', '2022-02-25',
         'FromSoftware', 'Bandai Namco Entertainment', 94,
         'Dive into a dark fantasy epic where towering castles and mysterious landscapes set the stage for brutal battles and an intricate lore that challenges your every decision.',
         'https://static.bandainamcoent.eu/high/elden-ring/elden-ring/00-page-setup/elden-ring-new-header-mobile.jpg', 'https://ftw.usatoday.com/wp-content/uploads/sites/90/2022/04/elden-ring-Stormveil-Castle.jpg', 'https://cdn.mos.cms.futurecdn.net/85K44nHtaULdnBoRpCkzr5.jpg'),
        (3, 'The Witcher 3: Wild Hunt', 'RPG', '2015-05-19',
         'CD Projekt Red', 'CD Projekt', 93,
         'Join Geralt of Rivia in an expansive narrative adventure where every choice matters. Experience a monster-infested world filled with morally complex decisions, stunning open landscapes, and engrossing side quests that set a new standard for RPGs.',
         'https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg', 'https://sm.ign.com/ign_za/preview/w/we-played-/we-played-the-witcher-3-wild-hunt-for-6-hours-ign_3v48.jpg', 'https://static1.thegamerimages.com/wordpress/wp-content/uploads/2023/08/6-the-witcher-3-how-to-upgrade-armor.jpg'),
        (4, 'Grand Theft Auto V', 'Open-world, Action-adventure', '2013-09-17',
         'Rockstar North', 'Rockstar Games', 97,
         'Step into the chaotic streets of Los Santos, where crime, corruption, and satirical commentary on modern society merge. With three distinct protagonists and an expansive open world, this revolutionary title offers unparalleled freedom and detail.',
         'https://image.api.playstation.com/vulcan/ap/rnd/202203/0302/bZ1JTRXzoyl3hkcsloKcCgdB.jpg', 'https://www.godisageek.com/wp-content/uploads/GTA-V-Background1.jpg', 'https://static1.srcdn.com/wordpress/wp-content/uploads/2021/06/main-characters-Trevor-Michael-and-Franklin-standing-in-front-of-an-open-car-trunk-in-GTA-5.jpg'),
        (5, 'Red Dead Redemption 2', 'Action-adventure', '2018-10-26',
         'Rockstar Games', 'Rockstar Games', 97,
         'Experience the raw beauty and brutality of the American frontier in this epic tale of loyalty, loss, and survival. Journey through a living, breathing Western landscape in one of the most immersive narrative adventures ever created.',
         'https://media.rockstargames.com/rockstargames-newsite/uploads/bb98bc168c6a89180a326def291efeff23f6bb51.jpg', 'https://www.godisageek.com/wp-content/uploads/Red-Dead-Redemption-2-PC-review-1024x576.jpg', 'https://interfaceingame.com/wp-content/uploads/red-dead-redemption-2/red-dead-redemption-2-logo.jpg'),
        (6, 'Fortnite', 'Battle Royale / Sandbox', '2017-09-26',
         'Epic Games', 'Epic Games', 81,
         'Jump into the ever-changing arena of Fortnite, where fast-paced battles and creative building mechanics combine to deliver a constantly evolving experience. With seasonal events and a vibrant community, every match is a new adventure.',
         'https://wallpapers.com/images/hd/fortnite-1920x1080-hd-cvavgntkwzkn72rg.jpg', 'https://assets-prd.ignimgs.com/2024/09/09/fortnite2024-review-blogroll-1725911546359.jpg', 'https://eu-images.contentstack.com/v3/assets/bltbc1876152fcd9f07/bltc6968413f52c4194/675b120f49f79e73b2c82d5a/Fortnite.jpg'),
        (7, 'Minecraft', 'Sandbox, Survival', '2011-11-18',
         'Mojang', 'Mojang', 93,
         'Unleash your imagination in a limitless blocky world where the only limit is your creativity. Build intricate structures, explore vast underground caverns, and survive against the elements in one of the most influential games of all time.',
         'https://wallpapers.com/images/featured/minecraft-background-cfljc4haleghnajo.jpg', 'https://wallpapers.com/images/featured/minecraft-s2kxfahyg30sob8q.jpg', 'https://thumbs.dreamstime.com/b/lush-overgrown-ruins-minecraft-showcasing-vibrant-greenery-ancient-structures-lush-overgrown-ruins-minecraft-showcasing-363881046.jpg'),
        (8, 'God of War', 'Action', '2018-04-20',
         'Santa Monica Studio', 'Sony Interactive Entertainment', 94,
         'Join Kratos on an emotionally charged journey through Norse mythology in this reimagined epic. With visceral combat, stunning visuals, and deep storytelling, God of War redefines the action genre and delivers a narrative that resonates.',
         'https://i.pinimg.com/736x/eb/7c/81/eb7c819b2a606281bb9318a1a6aacc89.jpg', 'https://images6.alphacoders.com/900/900070.jpg', 'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/07/gow2.jpg'),
        (9, 'Overwatch', 'First-person shooter', '2016-05-24',
         'Blizzard Entertainment', 'Blizzard Entertainment', 91,
         'Team up with heroes from around the globe in this fast-paced, objective-based shooter that emphasizes teamwork and strategy. With a diverse roster and constantly updated gameplay, Overwatch offers a dynamic and engaging experience.',
         'https://images4.alphacoders.com/553/553496.jpg', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Overwatch_cover_art.jpg/220px-Overwatch_cover_art.jpg', 'https://wallpapers.com/images/featured/overwatch-pictures-dpacmg5qk3abi7qn.jpg'),
        (10, 'Call of Duty: Modern Warfare', 'First-person shooter', '2019-10-25',
         'Infinity Ward', 'Activision', 80,
         'Experience modern combat in a gritty, realistic setting where tactical precision meets high-octane action. Call of Duty: Modern Warfare delivers an intense narrative campaign and competitive multiplayer modes that redefine the genre.',
         'https://images5.alphacoders.com/105/1050665.jpg', 'https://thepopinsider.com/wp-content/uploads/sites/6/2019/06/Activision_CallofDuty_ModernWarfare_Feature.jpg', 'https://i.ytimg.com/vi/k2uDCQzCkfE/maxresdefault.jpg')
    ]

    cursor.executemany("""
        INSERT INTO games (id, title, genre, release_date, developer, publisher, metacritic_score, description, image_url, image_url2, image_url3)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, games_data)

    connection.commit()
    connection.close()
    print("Database created and populated successfully with unique game descriptions and three screenshot URLs per game.")

if __name__ == '__main__':
    create_and_populate_db()
