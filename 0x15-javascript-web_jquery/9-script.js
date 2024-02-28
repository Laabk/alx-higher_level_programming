// Queries an API for wind speed in SF and replaces the text
$(document).ready(function () {
	$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function (data) {
		$("DIV#hello").text(data.hello);
	});
});
