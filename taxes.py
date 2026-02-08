
class VideoGames:
    def __init__(self, rating, genre, name):
        VideoGames.rating = rating
        VideoGames.genre = genre
        VideoGames.name = name
VideoGames(3.5, 'Action', 'Uncharted')
print(vars(VideoGames))