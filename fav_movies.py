import fresh_tomatoes
import media

Harry_Potter = media.Movie("Harry Potter and the Goblet of Fire",
	"The story followsHarry Potter's fourth year at Hogwarts as he is chosen by the Goblet of Fire to compete in the Triwizard Tournament.",
	"http://www.wichitaorpheum.com/wp-content/uploads/2013/05/Harry-Potter-and-the-Goblet-of-Fire-movie-poster.jpg",
	"https://www.youtube.com/watch?v=WVNENtEJyMM")
Chappie = media.Movie("Chappie",
	"The film, set and shot in johannesburg, is about an artificially intelligent law enforcement robot captured and taught by gangsters, who nickname it Chappie.",
	"http://www.joblo.com/images_arrownews/chappie-international-poster.jpg",
	"https://www.youtube.com/watch?v=l6bmTNadhJE")
Star_Trek_Beyond = media.Movie("Star Trek Beyond",
	"Three years into its five year mission, the USS Enterprise arrives at Starbase Yorktown, a massive space station",
	"http://getthechance.wales/wp-content/uploads/2016/08/star-trek-beyond-poster-2.jpg",
	"https://www.youtube.com/watch?v=XRVD32rnzOw")
Air_Force_One = media.Movie("Air Force One", 
	"American and Russian Special Forces capture General Ivan Radek (Jurgen Prochnow), the dictator of a rogue terrorist regime in Kazakhstan that possessed stolen Soviet nuclear weapons, threatening to start a new Cold War.",
	"http://www.impawards.com/1997/posters/air_force_one_ver5.jpg",
	"https://www.youtube.com/watch?v=YdaeVone5qA")
Jurassic_World = media.Movie("Jurassic World",
	"Twenty-two years after Jurassic Park was overrun by cloned dinosaurs on the Central American island of Isla Nublar, a new park, Jurassic World, has become a successful resort. The Masrani Global Corporation",
	"http://www.impawards.com/2015/posters/jurassic_world_ver3.jpg",
	"https://www.youtube.com/watch?v=aJJrkyHas78")
Legend = media.Movie("I Am Legend",
	"In 2009, a genetically re-engineered measles virus, originally created as a cure for cancer, turns into a lethal strain which kills 94 percent of those it infects,",
	"https://www.cinematerial.com/media/posters/md/ow/owjyg8zn.jpg?v=1456238803",
	"https://www.youtube.com/watch?v=ewpYq9rgg3w")

movies = [Harry_Potter, Chappie, Air_Force_One, Jurassic_World, Legend, Star_Trek_Beyond]
fresh_tomatoes.open_movies_page(movies)