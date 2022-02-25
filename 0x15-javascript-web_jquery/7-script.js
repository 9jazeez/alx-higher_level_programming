// Using ajax to send a get request

const div = $('#character');

$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (data) {
      div.text('name: ' + data.name);
    }
  });
});
