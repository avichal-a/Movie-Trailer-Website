import webbrowser


class Movie():

    """ Defining Class Movie
    Data members : Movie Title , Stoty line
    Poster image URL, Youtube triller URL
    """

    def __init__(M, title, story, poster, traier):
    	    """ Constructor of class Movie
            Takes arguments: Movie Title , Stoty line
            Poster image URL, Youtube triller URL
            """
            M.title = title
            M.m_story = story
            M.poster_image_url = poster
            M.trailer_youtube_url = traier

    def play_trailer(M):
        """ OPens the yoube trailer URL in browser
        """
        webbrowser.open(M.trailer_youtube_url)
