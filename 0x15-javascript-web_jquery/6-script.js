// using jquery to add new elements

const div = $('#update_header');
const header = $('header');

div.on('click', function () {
  header.text('New Header!!!');
});
