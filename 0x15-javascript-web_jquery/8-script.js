// Using ajax to send a get request

const ul = $('#list_movies');

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, item) {
        ul.append('<li>' + item.title + '</li>');
      });
    }
  });
});
