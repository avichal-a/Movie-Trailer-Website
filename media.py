import webbrowser
class Movie():
	def __init__(M,title,story,poster,traier):
		M.title = title
		M.m_story = story
		M.poster_image_url =poster
		M.trailer_youtube_url = traier
	def play_trailer(M):
		webbrowser.open(M.trailer_youtube_url)
