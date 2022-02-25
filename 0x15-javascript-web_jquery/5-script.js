// using jquery to add new elements

const div = $('#add_item');
const ul = $('.my_list');

div.on('click', function () {
  ul.append('<li>Item</li>');
});
