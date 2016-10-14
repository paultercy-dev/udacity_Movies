import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title #movie title of instances
		self.storyline = movie_storyline # the movie story line of instances
		self.poster_image_url = poster_image # the url to the movie poster of instance
		self.trailer_youtube_url = trailer_youtube # url to youtube movie trailer 

	#define a function to open a webbrowser to play the you tube trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)