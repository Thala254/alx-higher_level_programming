$(() => $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, status) => {
  if (status === 'success') {
    data.results.forEach((result) => $('UL#list_movies').append(`<li>${result.title}</li>`));
  }
}));
