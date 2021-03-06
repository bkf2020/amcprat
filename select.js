var all_test = ["AIME", "AMC8", "AMC10", "AMC12"];
var all_levels = ["Easy", "Medium", "Hard", "VeryHard"];
var tests = [];
var levels = new Map();

function reset() {
	tests = [];
}

function getLevels() {
	reset();
	for(var i = 0; i < all_test.length; i++) {
		var cur_checkbox = document.getElementsByName(all_test[i])[0];
		if(cur_checkbox.checked) tests.push(all_test[i]);
	}
	afterWebsite = "#";
	for(var i = 0; i < tests.length; i++) {
		if(i != 0) afterWebsite += "?";
		afterWebsite += tests[i];
		for(var j = 0; j < all_levels.length; j++) {
			var cur_checkbox = document.getElementsByName(tests[i] + all_levels[j])[0];
			if(cur_checkbox.checked) {
				afterWebsite += "&".concat(all_levels[j]);
			}
		}
	}
	window.location.replace("answerproblems.html" + afterWebsite);
}

function getProblems() {
	reset();
	var toSelect = window.location.hash.substring(1);
	var testsAndLevels = toSelect.split("?");
	for(var i = 0; i < testsAndLevels.length; i++) {
		var currentLevelsWithTest = testsAndLevels[i].split("&");
		tests.push(currentLevelsWithTest[0]);

		var currentLevels = [];
		for(var j = 1; j < currentLevelsWithTest.length; j++) {
			currentLevels.push(currentLevelsWithTest[j]);
		}
		levels.set(tests[i], currentLevels);
	}
	
}
