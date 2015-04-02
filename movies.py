from fresh_tomatoes import open_movies_page

class Movie():
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url



def main():
	man_of_steel = Movie("Man of Steel", "http://upload.wikimedia.org/wikipedia/en/8/85/ManofSteelFinalPoster.jpg", "https://www.youtube.com/watch?v=T6DJcgm3wNY")
	school_of_rock = Movie("School of Rock", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=5afGGGsxvEA")
	spiderman = Movie("Spiderman", "https://image.tmdb.org/t/p/original/jz6NCADCgj4dWU8RM81Xvrokey4.jpg", "https://www.youtube.com/watch?v=EQdOOTQnuvk")
	avengers = Movie("The Avengers", "http://pleasantvalleylibrary.org/files/2015/02/theavengers001.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

	open_movies_page([school_of_rock, spiderman, man_of_steel, avengers])



if __name__=='__main__':
	main()