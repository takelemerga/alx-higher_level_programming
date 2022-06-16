// fetches and prints how to say “Hello” depending on the language
function translatelang () {
  const value = $('INPUT#language_code').val();
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=' + value, (data) => {
    $('DIV#hello').html(data.hello);
  });
}

$(function () {
  $('INPUT#btn_translate').click(translatelang);
});

$(function () {
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translatelang();
      return false;
    }
  });
});
