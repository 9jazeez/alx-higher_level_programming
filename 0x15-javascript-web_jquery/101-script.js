$(function () {
  const addItem = $('#add_item');
  const removeItem = $('#remove_item');
  const clearItems = $('#clear_list');
  let count = 0;

  const mylist = $('.my_list');

  addItem.on('click', function () {
    if (count <= 0) {
      count = 0;
    }
    mylist.append('<li>Item:' + count + '</li>');
    ++count;
  });

  removeItem.on('click', function () {
    // $('li').eq(count--).remove();
    count--;
    $('li').last().remove();
  });

  clearItems.on('click', function () {
    mylist.empty();
    count = 0;
  });
});
