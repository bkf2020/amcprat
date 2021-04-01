function changeTheme() {
	var themeStylesheet = document.getElementById("themeStylesheet");
	if(themeStylesheet.getAttribute("href") === "style.css") {
		themeStylesheet.href = "style-dark.css";
	}
	else {
		themeStylesheet.href = "style.css";
	}
}
