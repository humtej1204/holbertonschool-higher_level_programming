$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data, status) {
  for (const [key, value] of Object.entries(data)) {
    if (key === 'name') {
      $('#character').text(value);
    }
  }
});
