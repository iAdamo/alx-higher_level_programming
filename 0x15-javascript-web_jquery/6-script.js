/**
 * Script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
 */

$('DIV#update_header').on('click', () => {
  $('header').text('New Header!!!');
});
