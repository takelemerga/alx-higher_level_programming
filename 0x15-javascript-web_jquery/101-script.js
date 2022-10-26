// adds, removes and clears LI elements from a list when the user click

document.addEventListener('DOMContentLoaded', function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
