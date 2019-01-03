FS001 = ["/", "d",
         ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
         ["home", "d",
          ["psychology", "d", ["trauma", "d", ["pills.py"], ["coffee.jpg"]], ["versus.py", "f"],
           ["crazy", "d", ["stars.jpg", "f"], ["custody.avi", "f"]]],
          ["street", "d", ["ritman.py", "f"], ["future.txt", "f"]]]]
C001 = ["cd home/psychology/",
        "mkdir ../psychology/crazy/prison",
        "rmdir /home/./street",
        "cd .././..//studio",
        "rm ../home/psychology/versus.py",
        "cp zero.py /home/"]
R001 = ("SUCCESS", ["/", "d",
                    ["studio", "d", ["zero.py", "f"], ["thakur.jpg", "f"]],
                    ["home", "d",
                     ["psychology", "d", ["trauma", "d", ["pills.py"], ["coffee.jpg"]],
                      ["crazy", "d", ["stars.jpg", "f"],
                       ["custody.avi", "f"], ["prison", "d"]]], ["zero.py", "f"]]], "/studio")

FS002 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C002 = ["cd series/netflix",
        "rmdir .././/../musics/ajdar",
        "cd .."]
R002 = ("ERROR", "rmdir .././/../musics/ajdar", "/series/netflix")

FS003 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C003 = ["cd series/netflix",
        "exec black.avi",
        "exec /musics/ajdar/turp_gibi.mp3",
        "rm ../..//movies/2018",
        "cd /movies/2018"]
R003 = ("ERROR", "rm ../..//movies/2018", "/series/netflix")

FS004 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C004 = ["cd photos",
        "rm ../series/netflix/black.avi",
        "cp /movies/2010 ../musics/",
        "exec /series/netflix/mirror.mkv"]
R004 = ("ERROR", "cp /movies/2010 ../musics/", "/photos")

FS005 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C005 = ["cd musics/tarkan",
        "rmdir ../.././//./musics/tarkan"]
R005 = ("SUCCESS", ["/", "d",
                    ["movies", "d", ["2018", "d"], ["2010", "d"]],
                    ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
                    ["photos", "d"],
                    ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["2010", "d"]]], "/musics/tarkan")

FS006 = ["/", "d",
         ["movies", "d", ["2018", "d"], ["2010", "d"]],
         ["series", "d", ["netflix", "d", ["black.avi", "f"], ["mirror.mkv", "f"]]],
         ["photos", "d"],
         ["musics", "d", ["ajdar", "d", ["turp_gibi.mp3", "f"]], ["tarkan", "d"], ["2010", "d"]]]
C006 = ["exec movies/2018"]
R006 = ("ERROR", "exec movies/2018", "/")

FS007 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C007 = ["cd software",
        "mkdir ../games/finished",
        "cp valecnik_rpg /games/finished/",
        "cd ..//games/finished/valecnik_rpg"]
R007 = ("SUCCESS", ["/", "d",
                    ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
                    ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
                    ["plans", "d", ["website", "d", ["index.php", "f"]]],
                    ["games", "d", ["finished", "d", ["valecnik_rpg", "d", ["main.py", "f"]]]],
                    ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]],
        "/games/finished/valecnik_rpg")

FS008 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C008 = ["cd work",
        "cd .../plans",
        "cd ../*"]
R008 = ("ERROR", "cd .../plans", "/work")

FS009 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C009 = ["cd plans/website/index.php"]
R009 = ("ERROR", "cd plans/website/index.php", "/")

FS010 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C010 = ["cd software/valecnik_rpg",
        "rmdir ../../work",
        "cd /work"]
R010 = ("ERROR", "cd /work", "/software/valecnik_rpg")

FS011 = ["/", "d",
         ["downloads", "d"], ["documents", "d", ["photoshop", "d"]],
         ["work", "d", ["cv.pdf", "f"], ["photos", "d"]],
         ["plans", "d", ["website", "d", ["index.php", "f"]]],
         ["games", "d"], ["software", "d", ["valecnik_rpg", "d", ["main.py", "f"]]], ["other", "d"]]
C011 = ["cd plans/*"]
R011 = ("ERROR", "cd plans/*", "/")

FS012 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C012 = ["cd earth",
        "rm .././water/sea"]
R012 = ("ERROR", "rm .././water/sea", "/earth")

FS013 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C013 = ["cd water/sea",
        "rmdir /earth/mountain.jpg"]
R013 = ("ERROR", "rmdir /earth/mountain.jpg", "/water/sea")

FS014 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C014 = ["cd fire",
        "rmdir .."]
R014 = ("ERROR", "rmdir ..", "/fire")

FS015 = ["/", "d",
         ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]],
         ["earth", "d", ["mountain.jpg", "f"]], ["air", "d"]]
C015 = ["cp earth/mountain.jpg /water/sea/",
        "cd earth",
        "rm mountain.jpg",
        "exec ../water/sea/mountain.jpg"]
R015 = ("SUCCESS",
        ["/", "d", ["fire", "d"], ["water", "d", ["sea", "d"], ["lake", "d"]], ["earth", "d", ["mountain.jpg", "f"]],
         ["air", "d"]], "/earth")
