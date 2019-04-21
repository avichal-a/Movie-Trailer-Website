import media
import fun


"""   Creating the instace of captain_marvel movie
           by passing argumnets like 1. Movie name
           2. story line. 3 Image URL` 4.youtube Taylor url
"""
captain_marvel = media.Movie("Captain Marvel", (
                "one of the avengers super hero story"),
                "http://t1.gstatic.com/images?q=tbn:ANd9GcQ1bDkDLq-" +
                "_bteASakhnC1XYwlkErFuqcof7KMhFpRwVhCTh1Vo",
                "https://www.youtube.com/watch?v=0LHxvxdRnYc")


"""   Creating the instace of AGE OF ULTRON movie
       by passing argumnets like 1. Movie name
       2. story line. 3 Image URL` 4.youtube Taylor url
"""
age_of_ultron = media.Movie("Age of ultron", (
                "AI Robot want to destroy humanity stopped by avengers"),
                "https://cdn-images-1.medium.com/" +
                "max/1600/1*V5v7RQnBinQH7i5o1UXKYw.jpeg",
                "https://www.youtube.com/watch?v=tmeOjFno6Do")


"""   Creating the instace of THOR Rangarok movie
       by passing argumnets like 1. Movie name
       2. story line. 3 Image URL` 4.youtube Taylor url
"""
rangarok = media.Movie("Thor Rangarok", (
            "Thor the god of thunder protect all asgardianns" +
            "from its planet destruction"),
            "https://media.vanityfair.com/photos/59f10041a923ff0fd178ca84/" +
            "master/w_960,c_limit/Thor-Ragnarok-Review.jpg",
            "https://www.youtube.com/watch?v=ue80QwXMRHg")


"""   Creating the instace of BLACK PATHER movie
       by passing argumnets like 1. Movie name
       2. story line. 3 Image URL` 4.youtube Taylor url
"""
black_panther = media.Movie("Balck Panther", (
    "one of the avengers super hero story"),
    "https://cdn.vox-cdn.com/thumbor/2E5_bNdm8Ews0Zw3O6kbct3tv70=" +
    "/0x0:915x610/920x613/filters:focal(377x20:523x166):format(webp)/" +
    "cdn.vox-cdn.com/uploads/chorus_image/image/58796435/boseman.0.jpg",
    "https://www.youtube.com/watch?v=xjDjIWPwcPU")


"""   Creating the instace of INFINITY WAR movie
       by passing argumnets like 1. Movie name
       2. story line. 3 Image URL` 4.youtube Taylor url
"""
infinity_war = media.Movie("Avengers Infinty war", (
    "Avengers fight against Thanos"),
    "https://cdn.arstechnica.net/wp-content/uploads/2018" +
    "/04/aveng-infinwar-logo-800x417.jpg",
    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")


"""   Creating the instace of END GAme movie
       by passing argumnets like 1. Movie name
       2. story line. 3 Image URL` 4.youtube Taylor url
"""
end_game = media.Movie("Avengers End Game", (
    "Avengers Fight with THanos 2"),
    "http://cdn.collider.com/wp-content/uploads/2019/04/" +
    "avengers-endgame-poster.png",
    "https://www.youtube.com/watch?v=oKStYmMgNRA")


""" Creating the list of movies from the instances
    of movies created above.
"""
movie_list = [captain_marvel, age_of_ultron, rangarok, (
            black_panther), infinity_war, end_game]


""" Paasing thw Movie list in open_movies_page
    function to create htmp page of movie list
"""
fun.open_movies_page(movie_list)
