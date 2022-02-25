$(function () {
  const div = $('#hello');
  const val = $('#language_code').val();
  const trans = $('#btn_translate');

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/?lang=' + val,
        type: 'GET',
        success: function (data) {
          const result = data.hello;
          console.log(val);
          console.log('success', data);
          div.text('result:' + result);
        }
      });
    }
  });
});
