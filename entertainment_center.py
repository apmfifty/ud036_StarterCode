import media
import fresh_tomatoes

lord_of_rings = media.Movie("The Lord of the Rings",
                        "The Lord of the Rings is a film series consisting of three high fantasy adventure films directed by Peter Jackson. They are based on the novel The Lord of the Rings by J. R. R. Tolkien. ",
                        "https://upload.wikimedia.org/wikipedia/en/8/87/Ringstrilogyposter.jpg",
                        "https://www.youtube.com/watch?v=rCZ3SN65kIs")
forest_gump = media.Movie("Forrest Gump",
                          "the story about one American man's growth",
                          "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                          "https://www.youtube.com/watch?v=Oc_JXiRanlI")
titanic = media.Movie("Titanic",
                      "The love story after one ship hits the iceberg",
                      "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
pearl_harbor = media.Movie("Pearl Harbor",
                          "the story on the historical event- Japanese army attacked US pearl harbor",
                          "https://upload.wikimedia.org/wikipedia/en/3/3c/Pearl_harbor_movie_poster.jpg",
                          "https://www.youtube.com/watch?v=oGYcxjywx0o")
braveheart = media.Movie("Braveheart",
                         "the legendary Scottish hero's story",
                         "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
                         "https://www.youtube.com/watch?v=wj0I8xVTV18")
godfather = media.Movie("The Godfather",
                        "the story of Italian mafia in Newwork",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

movies=[lord_of_rings,forest_gump,titanic,pearl_harbor,braveheart,godfather]
fresh_tomatoes.open_movies_page(movies)
