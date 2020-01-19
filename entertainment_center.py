import media
import fresh_tomatoes
#toy_story,avatar,ironman,school_of_rock,midnight_in_paris,resident_evil
toy_story = media.Movie("Toy Story disney",
			"A story of a boy and his toys that come to life",
			"https://contentserver.com.au/assets/594265_p17420_p_v8_ab.jpg",
			"https://www.youtube.com/watch?v=LDXYRzerjzU")

#print (toy_story.storyline)

avatar= media.Movie("AVATAR",
			"A marine on an alien planet",
			"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
			"https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

iron_man = media.Movie("IRON MAN-Robert Junior",
			"technology based robotics implimentation in human",
			"https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
			"https://www.youtube.com/watch?v=8hYlB38asDY")
#print(iron_man.title)
#print(iron_man.storyline)
#iron_man.show_trailer()


school_of_rock = media.Movie("School Of Rock",
				"using rock music to learn",
				"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
				"https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
				"Going back in time to meet authors",
				"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
				"https://www.youtube.com/watch?v=FAfR8omt-CY")

resident_evil = media.Movie("Resident EVIl: 2002",
				"a top-secret genetic research facility-(T virus)",
				"https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg",
				"https://www.youtube.com/watch?v=kEutwdia8n0")

movie = [toy_story,avatar,iron_man,school_of_rock,midnight_in_paris,resident_evil]

#fresh_tomatoes.open_movies_page(movie)
print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
#print (media.Movie.__name__)
print (media.Movie.__module__)


