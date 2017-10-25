import webbrowser


class Movie():
    """
    The Movie() class will be able to store its title,storyline, poster image
     and trailer website.
    """

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        """ This function will init the Movie class which requires the input
        of title,storyline, poster image and trailer website.
        :param movie_title:
        :param movie_storyline:
        :param poster_image:
        :param trailer_youtube:
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        This function will open the website of the movie's trailer by calling
        the module of webbrowser.
        """
        webbrowser.open((self.trailer_youtube_url))
