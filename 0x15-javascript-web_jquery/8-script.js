$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  for (const [key, value] of Object.entries(data)) {
    if (key === 'results') {
      value.forEach(element => {
        for (const [ky, val] of Object.entries(element)) {
          if (ky === 'title') {
            $('#list_movies').append(`<li>${val}</li>`);
          }
        }
      });
    }
  }
});
