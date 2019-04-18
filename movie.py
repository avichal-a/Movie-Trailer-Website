import media
import fun
captain_marvel = media.Movie("Captain Marvel","one of the avengers super hero story","http://t1.gstatic.com/images?q=tbn:ANd9GcQ1bDkDLq-_bteASakhnC1XYwlkErFuqcof7KMhFpRwVhCTh1Vo","hgttps://www.youtube.com/watch?v=0LHxvxdRnYc")


age_of_ultron = media.Movie("Age of ultron","AI Robot want to destroy humanity stopped by avengers","https://cdn-images-1.medium.com/max/1600/1*V5v7RQnBinQH7i5o1UXKYw.jpeg","https://www.youtube.com/watch?v=tmeOjFno6Do")
rangarok = media.Movie("Thor Rangarok","Thor the god of thunder protect all asgardianns from its planet destruction" ,"https://media.vanityfair.com/photos/59f10041a923ff0fd178ca84/master/w_960,c_limit/Thor-Ragnarok-Review.jpg","https://www.youtube.com/watch?v=ue80QwXMRHg")

black_panther = media.Movie("Balck Panther","one of the avengers super hero story","https://cdn.vox-cdn.com/thumbor/2E5_bNdm8Ews0Zw3O6kbct3tv70=/0x0:915x610/920x613/filters:focal(377x20:523x166):format(webp)/cdn.vox-cdn.com/uploads/chorus_image/image/58796435/boseman.0.jpg","https://www.youtube.com/watch?v=xjDjIWPwcPU")
infinity_war = media.Movie("Avengers Infinty war","Avengers fight against Thanos","https://cdn.arstechnica.net/wp-content/uploads/2018/04/aveng-infinwar-logo-800x417.jpg","https://www.youtube.com/watch?v=6ZfuNTqbHE8")
end_game = media.Movie("Avengers End Game","Avengers Fight with THanos 2","http://cdn.collider.com/wp-content/uploads/2019/04/avengers-endgame-poster.png","https://www.youtube.com/watch?v=oKStYmMgNRA")
#Captain_marvel = media.Movie("Captain Marvel","one of the avengers super hero story","http://t1.gstatic.com/images?q=tbn:ANd9GcQ1bDkDLq-_bteASakhnC1XYwlkErFuqcof7KMhFpRwVhCTh1Vo","https://www.youtube.com/watch?v=0LHxvxdRnYc")

movie_list = [captain_marvel,age_of_ultron,rangarok,black_panther,infinity_war,end_game]
fun.open_movies_page(movie_list)
