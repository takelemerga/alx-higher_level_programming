// fetches the character 'name' from given URL

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('DIV#character').html(data.name);
});
