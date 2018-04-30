import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A stroy of a boy and his toys taht come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=NTdKQzVFeis")


avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")


cloud_atlas = media.Movie("Cloud Atlas",
                          "Science Fiction movie depicting how lives in the \
                          universe are inter-connected",
                          "https://upload.wikimedia.org/wikipedia/en/2/20/Cloud_Atlas_Poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=hWnAqFyaQ5s")

mrnobody = media.Movie("Mr.Nobody",
                       "the life story of Nemo Nobody, a 118-year-old man \
                       who is the last mortal on Earth after the human \
                       race has achieved quasi-immortality",
                       "https://upload.wikimedia.org/wikipedia/en/3/32/Mr._Nobody_%28film_poster%29.jpg",  # noqa
                       "https://www.youtube.com/watch?v=iJAP8q_iPOw")

fight_club = media.Movie("Fight Club",
                         "The narrator who unknownling creates an alter \
                         ego and creates a fight club to take down society",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

interstellar = media.Movie("Interstellar",
                           "Set in a dystopian future where humanity is \
                           struggling to survive, it follows a group of \
                           astronauts who travel through a wormhole in search \
                           of a new home for humanity.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

movies = [toy_story, avatar, cloud_atlas, mrnobody, fight_club, interstellar]

fresh_tomatoes.open_movies_page(movies)
