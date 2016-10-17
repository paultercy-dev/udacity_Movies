import fresh_tomatoes #file that renders a html of movie
import media #import class Movie

#Movies that will be displayed in the html file
Harry_Potter = media.Movie("Harry Potter and the Goblet of Fire",
	"Harry Potter's  is chosen by the Goblet of Fire to compete in the Triwizard Tournament.",
	"http://www.wichitaorpheum.com/wp-content/uploads/2013/05/Harry-Potter-and-the-Goblet-of-Fire-movie-poster.jpg",
	"https://www.youtube.com/watch?v=WVNENtEJyMM")
Chappie = media.Movie("Chappie",
	"Is about an artificially intelligent law enforcement robot captured",
	"http://www.joblo.com/images_arrownews/chappie-international-poster.jpg",
	"https://www.youtube.com/watch?v=l6bmTNadhJE")
Star_Trek_Beyond = media.Movie("Star Trek Beyond",
	"The USS Enterprise arrives at Starbase Yorktown, a massive space station",
	"http://getthechance.wales/wp-content/uploads/2016/08/star-trek-beyond-poster-2.jpg",
	"https://www.youtube.com/watch?v=XRVD32rnzOw")
Air_Force_One = media.Movie("Air Force One", 
	"Amercian presdient kidnapped inside Air Force One", 
	"http://www.impawards.com/1997/posters/air_force_one_ver5.jpg",
	"https://www.youtube.com/watch?v=YdaeVone5qA")
Jurassic_World = media.Movie("Jurassic World",
	"Twenty-two years after Jurassic Park was overrun by cloned dinosaur and  a new park was built", 
	"http://www.impawards.com/2015/posters/jurassic_world_ver3.jpg",
	"https://www.youtube.com/watch?v=aJJrkyHas78")
Legend = media.Movie("I Am Legend",
	"A genetically re-engineered measles virus, turns into a lethal",
	"http://moviefiles.alphacoders.com/558/poster-558.jpg",
	"https://www.youtube.com/watch?v=ewpYq9rgg3w")
movies = [Harry_Potter, Chappie, Air_Force_One, Jurassic_World, Legend, Star_Trek_Beyond]
#takes array of movies so fresh_tomatoes class can render the html file
fresh_tomatoes.open_movies_page(movies)