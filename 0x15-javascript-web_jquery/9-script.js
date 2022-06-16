// displays the value of hello

$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (url, status) => {
    if (status === 'success') {
      $('div#hello').text(url.hello);
    }
  });
});
