//using the toggle function in jquery
const div = $('#toggle_header');
const header = $('header');
header.addClass('red');

div.on('click',function() {
  if (header[0].className === "green") {
     header.toggleClass('red');
  } else {
    header.toggleClass('green');
    }
});
