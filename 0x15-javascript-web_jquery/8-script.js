// fetches and lists the title for all movies

$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (url, status) => {
    if (status === 'success') {
      const movies = url.results;
      movies.forEach(movie => {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }
  });
});
