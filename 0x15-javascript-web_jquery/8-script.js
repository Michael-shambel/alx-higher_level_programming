$.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        success: function(response) {
            var movies = response.results;
            var list = $('#list_movies');
            $.each(movies, function(index, movie) {
                $('<li>').text(movie.title).appendTo(list);
            });
        }
    });
