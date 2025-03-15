# init_db.py
import sqlite3

def create_and_populate_db():
    connection = sqlite3.connect('games.db')
    cursor = connection.cursor()

    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS games")

    # Create the 'games' table with additional column for cover_image
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
            cover_image TEXT,
            image_url TEXT,
            image_url2 TEXT,
            image_url3 TEXT,
            nz_age_rating TEXT,
            nz_age_rating_reason TEXT
        );
    """)

    # Insert sample game data (20 records in total) with NZ age rating info and cover_image links
    games_data = [
        # Original 10 games with added NZ age ratings and explanations
        (1, 'The Legend of Zelda: Breath of the Wild', 'Action-adventure', '2017-03-03',
         'Nintendo', 'Nintendo', 97,
         'Immerse yourself in a vast, breathtaking world where every corner holds secrets and adventures. Explore ancient ruins, solve intricate puzzles, and battle formidable foes as you rediscover the lost kingdom of Hyrule. This groundbreaking title redefines open-world exploration with its dynamic weather system and physics-based gameplay.',
         'https://upload.wikimedia.org/wikipedia/en/c/c6/The_Legend_of_Zelda_Breath_of_the_Wild.jpg',
         'https://play.nintendo.com/images/Gallery_Lozbotw_1.aaaec624.2d958659.jpg', 
         'https://cdn.europosters.eu/image/1300/canvas-print-the-legend-of-zelda-breath-of-the-wild-view-i111060.jpg', 
         'https://wallpapers.com/images/hd/legend-of-zelda-breath-of-the-wild-painting-k9bmo0nvyagk9hma.jpg',
         'M', 'Fantasy violence and minimal realistic content make it suitable for younger players with parental guidance.'),
        (2, 'Elden Ring', 'Action RPG', '2022-02-25',
         'FromSoftware', 'Bandai Namco Entertainment', 94,
         'Dive into a dark fantasy epic where towering castles and mysterious landscapes set the stage for brutal battles and an intricate lore that challenges your every decision.',
         'https://m.media-amazon.com/images/I/6110RSDn3PL._AC_UF894,1000_QL80_.jpg',
         'https://cdn.mos.cms.futurecdn.net/ckpbJfmNhTHjRY6S7fdzeE-1200-80.jpg', 
         'https://static.bandainamcoent.eu/high/elden-ring/elden-ring/00-page-setup/elden-ring-new-header-mobile.jpg', 
         'https://cdn.shortpixel.ai/spai/q_glossy+ret_img+to_auto/www.slantmagazine.com/wp-content/uploads/2022/05/eldenring.jpg',
         'R13', 'Medium - High violence and mature themes require an adult audience.'),
        (3, 'The Witcher 3: Wild Hunt', 'RPG', '2015-05-19',
         'CD Projekt Red', 'CD Projekt', 93,
         'Join Geralt of Rivia in an expansive narrative adventure where every choice matters. Experience a monster-infested world filled with morally complex decisions, stunning open landscapes, and engrossing side quests that set a new standard for RPGs.',
         'https://upload.wikimedia.org/wikipedia/en/0/0c/Witcher_3_cover_art.jpg',
         'https://sm.ign.com/ign_za/review/t/the-witche/the-witcher-3-the-wild-hunt-review_wvw4.jpg', 
         'https://en.cdprojektred.com/wp-content/uploads-cdpr-en/2021/07/th-98654-38843.jpg', 
         'https://image.api.playstation.com/vulcan/ap/rnd/202211/2813/5DSZkROrbrlYN2PXGfDGedeM.jpg',
         'R16', 'Strong violence, mature narrative, and occasional explicit content necessitate an adult rating.'),
        (4, 'Grand Theft Auto V', 'Open-world, Action-adventure', '2013-09-17',
         'Rockstar North', 'Rockstar Games', 97,
         'Step into the chaotic streets of Los Santos, where crime, corruption, and satirical commentary on modern society merge. With three distinct protagonists and an expansive open world, this revolutionary title offers unparalleled freedom and detail.',
         'https://i.pinimg.com/736x/e0/ce/25/e0ce25ef5bc485378b82b639363916a8.jpg',
         'https://wallpapers.com/images/featured/gta-5-qpjtjdxwbwrk4gyj.jpg', 
         'https://www.igrandtheftauto.com/content/images/gtav-box-art-1280x1580.jpg', 
         'https://media.rockstargames.com/rockstargames/img/global/news/upload/actual_1380583804.jpg',
         'R18', 'Realistic violence, strong language, and mature themes restrict it to adult audiences.'),
        (5, 'Red Dead Redemption 2', 'Action-adventure', '2018-10-26',
         'Rockstar Games', 'Rockstar Games', 97,
         'Experience the raw beauty and brutality of the American frontier in this epic tale of loyalty, loss, and survival. Journey through a living, breathing Western landscape in one of the most immersive narrative adventures ever created.',
         'https://i.redd.it/hstv1dhma2k41.jpg',
         'https://cdn.mos.cms.futurecdn.net/TXCXM3kfwn8T6H6zQuWLJ6-1200-80.jpg', 
         'https://cdn1.epicgames.com/b30b6d1b4dfd4dcc93b5490be5e094e5/offer/RDR2476298253_Epic_Games_Wishlist_RDR2_2560x1440_V01-2560x1440-2a9ebe1f7ee202102555be202d5632ec.jpg', 
         'https://static01.nyt.com/images/2018/11/25/opinion/25SUDERMAN/25SUDERMAN-superJumbo.jpg',
         'R16', 'Intense, realistic violence and mature narrative themes call for an R16 rating.'),
        (6, 'Fortnite', 'Battle Royale / Sandbox', '2017-09-26',
         'Epic Games', 'Epic Games', 81,
         'Jump into the ever-changing arena of Fortnite, where fast-paced battles and creative building mechanics combine to deliver a constantly evolving experience. With seasonal events and a vibrant community, every match is a new adventure.',
         'https://i.pinimg.com/222x/24/c7/2c/24c72c57b91ffaac29c45a9473471ec5.jpg',
         'https://cdn2.unrealengine.com/social-image-chapter4-s3-3840x2160-d35912cc25ad.jpg', 
         'https://eu-images.contentstack.com/v3/assets/bltbc1876152fcd9f07/bltc6968413f52c4194/675b120f49f79e73b2c82d5a/Fortnite.jpg', 
         'https://cdn2.unrealengine.com/fortnite-myths-and-mortals-battle-pass-1920x1080-56228b70b9b3.jpg',
         'PG', 'Cartoon-style violence and fantastical elements; generally acceptable for all ages with guidance.'),
        (7, 'Minecraft', 'Sandbox, Survival', '2011-11-18',
         'Mojang', 'Mojang', 93,
         'Unleash your imagination in a limitless blocky world where the only limit is your creativity. Build intricate structures, explore vast underground caverns, and survive against the elements in one of the most influential games of all time.',
         'https://cdn.mobygames.com/covers/3741959-minecraft-windows-apps-front-cover.jpg',
         'https://wallpapers.com/images/featured/minecraft-s2kxfahyg30sob8q.jpg', 
         'https://wallpapers.com/images/featured/minecraft-background-cfljc4haleghnajo.jpg', 
         'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2025/01/5-2-1.jpg',
         'G', 'Non-violent, creative gameplay makes it suitable for all audiences.'),
        (8, 'God of War', 'Action', '2018-04-20',
         'Santa Monica Studio', 'Sony Interactive Entertainment', 94,
         'Join Kratos on an emotionally charged journey through Norse mythology in this reimagined epic. With visceral combat, stunning visuals, and deep storytelling, God of War redefines the action genre and delivers a narrative that resonates.',
         'https://posterspy.com/wp-content/uploads/2024/03/poster_15.jpg',
         'https://i.pinimg.com/736x/eb/7c/81/eb7c819b2a606281bb9318a1a6aacc89.jpg', 
         'https://image.api.playstation.com/vulcan/img/rnd/202010/2217/LsaRVLF2IU2L1FNtu9d3MKLq.jpg', 
         'https://live.staticflickr.com/65535/51607429309_615d50b7b8_o.jpg',
         'R13', 'Strong combat violence and intense themes make it suitable only for older teens.'),
        (9, 'Overwatch', 'First-person shooter', '2016-05-24',
         'Blizzard Entertainment', 'Blizzard Entertainment', 91,
         'Team up with heroes from around the globe in this fast-paced, objective-based shooter that emphasizes teamwork and strategy. With a diverse roster and constantly updated gameplay, Overwatch offers a dynamic and engaging experience.',
         'https://upload.wikimedia.org/wikipedia/en/5/51/Overwatch_cover_art.jpg',
         'https://wallpapers.com/images/featured/overwatch-pictures-dpacmg5qk3abi7qn.jpg', 
         'https://images4.alphacoders.com/553/553496.jpg', 
         'https://wallpapers.com/images/hd/overwatch-main-protagonists-logo-a3l8ys802edqn1p5.jpg',
         'PG', 'Cartoon-style action and minimal realistic violence; suitable for teens.'),
        (10, 'Call of Duty: Modern Warfare', 'First-person shooter', '2019-10-25',
         'Infinity Ward', 'Activision', 80,
         'Experience modern combat in a gritty, realistic setting where tactical precision meets high-octane action. Call of Duty: Modern Warfare delivers an intense narrative campaign and competitive multiplayer modes that redefine the genre.',
         'https://upload.wikimedia.org/wikipedia/en/1/1f/Call_of_Duty_Modern_Warfare_%282019%29_cover.jpg',
         'https://wallpapers.com/images/hd/amazing-call-of-duty-modern-warfare-poster-adx4vdfo8tykk3un.jpg', 
         'https://images.squarespace-cdn.com/content/v1/5b592fe9b27e39b6d9d06c9d/1596868712842-3FHQLMO0UFISW34PG77H/call-of-duty-modern-warfare-hero-banner-03-ps4-us-30may19.jpg', 
         'https://media.wired.com/photos/5db9e04d182de80009f7fe42/master/pass/Cul-CallofDuty-Campaign_6.jpg',
         'R16', 'Realistic modern combat scenarios and strong language warrant a rating for older teens.'),

        # New 10 games (IDs 11 to 20) with release dates between 2000 and 2024
        (11, 'Halo: Combat Evolved', 'First-person shooter', '2001-11-15',
         'Bungie', 'Microsoft Game Studios', 97,
         'Halo: Combat Evolved revolutionized console first-person shooters with its immersive sci-fi story, iconic multiplayer, and groundbreaking gameplay mechanics.',
         'https://upload.wikimedia.org/wikipedia/en/8/80/Halo_-_Combat_Evolved_%28XBox_version_-_box_art%29.jpg',
         'https://images.squarespace-cdn.com/content/v1/530b8213e4b00fa2f7290a31/1525627181436-GTAHSK28W5SHFT7GP23N/Master-chief-Wallpaper-tsc.jpg', 
         'https://wallpapercat.com/w/full/d/6/d/1/2172433-1920x1080-desktop-1080p-halo-combat-evolved-background.jpg', 
         'https://xxboxnews.blob.core.windows.net/prod/sites/2/2020/03/Halo-Master-Chief-Collection-2020-HCEA-Campaign_3rd-Person_01_Watermarked_1920x1080.jpg',
         'R16', 'Sci-fi violence is stylized; generally acceptable for teenagers with guidance.'),
        (12, 'Bioshock', 'First-person shooter / Adventure', '2007-08-21',
         '2K Boston / Irrational Games', '2K Games', 96,
         'Bioshock offers a gripping narrative set in an underwater dystopia, blending horror and action for a unique experience.',
         'https://archive.mith.umd.edu/eng738T/wp-content/uploads/2012/02/Breaking_the_mold1.jpg',
         'https://cdn.mos.cms.futurecdn.net/3Mg5ZqAX2qvcyMtZXhZmcK.jpg', 
         'https://upload.wikimedia.org/wikipedia/en/thumb/6/6d/BioShock_cover.jpg/220px-BioShock_cover.jpg', 
         'https://i.pinimg.com/736x/43/6a/64/436a643883b9a5323ec74b528789872a.jpg',
         'R16', 'Mature themes and disturbing content; intended for older audiences.'),
        (13, 'Portal 2', 'Puzzle, First-person shooter', '2011-04-19',
         'Valve Corporation', 'Valve Corporation', 95,
         'Portal 2 builds on its predecessor with innovative puzzles, clever humor, and a memorable story for a unique gaming experience.',
         'https://cdn.mobygames.com/covers/6296552-portal-2-windows-front-cover.jpg',
         'https://static1.thegamerimages.com/wordpress/wp-content/uploads/2021/09/Portal-2-Chell-and-GlaDOS.jpg', 
         'https://cdn.mos.cms.futurecdn.net/rtEXSTFGZzEkLC9GYTpUUW.jpg', 
         'https://www.ericsbinaryworld.com/images/2011/05/2011-04-19_00011.jpg',
         'PG', 'Light-hearted humor and puzzle gameplay; accessible to a wide audience.'),
        (14, 'Dark Souls', 'Action RPG', '2011-09-22',
         'FromSoftware', 'Namco Bandai Games', 89,
         'Dark Souls challenges players with its unforgiving combat and intricate world design, rewarding perseverance in a dark, atmospheric setting.',
         'https://www.creativeuncut.com/gallery-18/art/ds-cover.jpg',
         'https://www.dreadxp.com/wp-content/uploads/2022/09/ss_c34cdf130b9ac71c99196007d1e78c05305652b9.1920x1080.jpg', 
         'https://upload.wikimedia.org/wikipedia/en/8/8d/Dark_Souls_Cover_Art.jpg', 
         'https://cdn.mos.cms.futurecdn.net/ciqzruT7pZVcq5CeuqnVNA.jpg',
         'R13', 'Challenging combat and bleak imagery; for older teens.'),
        (15, 'Mass Effect 2', 'Action RPG', '2010-01-26',
         'BioWare', 'Electronic Arts', 94,
         'Mass Effect 2 refines its sci-fi universe with deep character development and strategic combat in a richly detailed setting.',
         'https://masseffect2.wiki.fextralife.com/file/Mass-Effect-2/mass_effect2_about_mass_effect2_wiki_guide_300px.jpg',
         'https://amostagreeablepastime.com/wp-content/uploads/2014/07/mass-effect-2-screenshot.jpg', 
         'https://cdn.mos.cms.futurecdn.net/5WnJSkxWLscNNVrYDdvFxA.jpg', 
         'hhttps://static1.srcdn.com/wordpress/wp-content/uploads/2021/05/Mass-Effect-2--All-Legendary-Edition-Changes-Differences.jpg',
         'R13', 'Mature themes balanced by storytelling; recommended for older teens.'),
        (16, 'Fallout 3', 'Action RPG', '2008-10-28',
         'Bethesda Game Studios', 'Bethesda Softworks', 91,
         'Fallout 3 immerses you in a post-apocalyptic America with deep RPG elements and a compelling narrative in a devastated world.',
         'https://m.media-amazon.com/images/I/81-t5VgtNEL._AC_UF1000,1000_QL80_.jpg',
         'https://static1.srcdn.com/wordpress/wp-content/uploads/2024/05/characters-from-fallout-3.jpg', 
         'https://images.fallout.wiki/4/4c/Fo--games--fallout-3.jpg', 
         'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2020/07/Feature-23.jpg',
         'R18', 'Graphic violence and adult themes; intended for mature audiences.'),
        (17, 'Uncharted 2: Among Thieves', 'Action-adventure', '2009-10-13',
         'Naughty Dog', 'Sony Computer Entertainment', 96,
         'Uncharted 2 delivers cinematic storytelling and thrilling action in a high-adventure experience filled with breathtaking set-pieces.',
         'https://m.media-amazon.com/images/M/MV5BYzAxNDY2NjktNTI0Yi00NmJjLTkyMjYtNDk2ZGZkZTg0ZTg2XkEyXkFqcGc@._V1_UY1200_CR85,0,630,1200_AL_.jpg',
         'https://static1.thegamerimages.com/wordpress/wp-content/uploads/2024/10/mixcollage-14-oct-2024-11-57-am-1916.jpg', 
         'https://images3.alphacoders.com/775/thumb-1920-77599.jpg', 
         'https://c4.wallpaperflare.com/wallpaper/994/118/509/uncharted-2-among-thieves-uncharted-2-danger-nathan-drake-wallpaper-preview.jpg',
         'R16', 'Cinematic action and moderate violence; suitable for older teens.'),
        (18, "Assassin's Creed II", 'Action-adventure', '2009-11-17',
         'Ubisoft Montreal', 'Ubisoft', 91,
         "Assassin's Creed II immerses you in Renaissance Italy with stealth and combat in a rich historical narrative.",
         'https://wallpapercat.com/w/full/0/d/a/66615-1080x1920-iphone-1080p-assassins-creed-background.jpg',
         'https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/jmgQ9HLxYdObvhzpru54c/405d00bd6ab8e4d60caddee8a1e9d65c/-ACII-_Screenshots_-_7.jpg', 
         'https://images.alphacoders.com/863/86343.jpg', 
         'https://static1.srcdn.com/wordpress/wp-content/uploads/2022/05/Assassins-Creed-2-Showed-Ubisofts-Problems-First.jpg',
         'R16', 'Historical violence and mature themes; recommended for older teens.'),
        (19, 'Batman: Arkham City', 'Action-adventure', '2011-10-18',
         'Rocksteady Studios', 'Warner Bros. Interactive Entertainment', 96,
         'Batman: Arkham City offers a dark, atmospheric experience with innovative combat that captures the essence of Gotham City.',
         'https://cdn.europosters.eu/image/1300/art-photo/batman-arkham-city-i167588.jpg',
         'https://i.redd.it/iwq34es4cku91.jpg', 
         'https://i.pinimg.com/736x/da/d0/27/dad027b642dc0d9896797005bee34a88.jpg', 
         'https://i.pinimg.com/736x/40/36/8f/40368fc085746cafbf8097488adcd405.jpg',
         'M', 'Dark themes and intense action; intended for mature audiences.'),
        (20, 'The Last of Us', 'Action-adventure, Survival', '2013-06-14',
         'Naughty Dog', 'Sony Computer Entertainment', 95,
         'The Last of Us combines intense survival gameplay with a deeply emotional narrative in a post-apocalyptic world.',
         'https://upload.wikimedia.org/wikipedia/commons/6/66/The_Last_of_Us_logo.png',
         'https://static0.gamerantimages.com/wordpress/wp-content/uploads/2023/07/the-last-of-us-2013-stealth.jpg', 
         'https://www.joystickchik.com/wp-content/uploads/2014/04/last-of-us.jpg', 
         'https://c4.wallpaperflare.com/wallpaper/994/844/997/the-last-of-us-2013-game-wallpaper-preview.jpg',
         'R18', 'Strong language, intense violence, and mature themes; intended for mature audiences.')
    ]

    cursor.executemany("""
        INSERT INTO games (id, title, genre, release_date, developer, publisher, metacritic_score, description, cover_image, image_url, image_url2, image_url3, nz_age_rating, nz_age_rating_reason)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, games_data)

    connection.commit()
    connection.close()
    print("Database created and populated successfully with 20 games and cover images.")

if __name__ == '__main__':
    create_and_populate_db()
