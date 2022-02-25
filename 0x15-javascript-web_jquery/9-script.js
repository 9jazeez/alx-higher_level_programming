// Using ajax to send a get request

$(function () {
  const $div = $('#hello');

  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $div.text(data.hello);
    }
  });
});
