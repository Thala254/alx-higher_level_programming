$('document').ready(() => {
  const url = 'https://stefanbohacek.com/hellosalut/?';
  const hello = event => $.get(url + $.param({ lang: $('INPUT#language_code').val() }), data => $('DIV#hello').text(data.hello));
  $('INPUT#btn_translate').on('click', hello);
  $('INPUT#language_code').on('keypress', event => {
    const k = event.KeyCode ? event.KeyCode : event.which;
    if (k === 13) hello(event);
  });
});
