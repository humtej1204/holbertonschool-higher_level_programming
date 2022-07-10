window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    translateHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
};

function translateHello () {
  const language_code = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + language_code, function (data, status) {
    $('DIV#hello').text(data.hello);
  });
}
