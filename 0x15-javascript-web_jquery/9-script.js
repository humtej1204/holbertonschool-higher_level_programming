$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
    $('#hello').text(data.hello);
  });
});
