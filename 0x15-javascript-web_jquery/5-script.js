// adds a <li> element to a list when clicks on tag

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
