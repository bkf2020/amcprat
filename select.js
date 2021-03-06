var allTests = ["AIME", "AMC8", "AMC10", "AMC12"];
var allLevels = ["Easy", "Medium", "Hard", "VeryHard"];
var tests = [];
var levels = new Map();
var problemURLS = [];

function reset() {
	tests = [];
}

function getLevels() {
	reset();
	for(var i = 0; i < allTests.length; i++) {
		var cur_checkbox = document.getElementsByName(allTests[i])[0];
		if(cur_checkbox.checked) tests.push(allTests[i]);
	}
	afterWebsite = "#";
	for(var i = 0; i < tests.length; i++) {
		if(i != 0) afterWebsite += "?";
		afterWebsite += tests[i];
		for(var j = 0; j < allLevels.length; j++) {
			var cur_checkbox = document.getElementsByName(tests[i] + allLevels[j])[0];
			if(cur_checkbox.checked) {
				afterWebsite += "&".concat(allLevels[j]);
			}
		}
	}
	window.location.replace("answerproblems.html" + afterWebsite);
}

// from https://stackoverflow.com/questions/51319147/map-default-value
function getMapValue(map, key) {
	return map.get(key) || false;
}

function getLevelsFromURL() {
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

function getProblems() {
	var visited = new Map();
	for(var i = 0; i < 5; i++) {
		var problemURL = "";
		var index = Math.floor(Math.random() * tests.length);
		var test = tests[index];
		var year;
		var problem;
		if(test === "AIME") {
			year = Math.floor(Math.random() * 5) + 2015;
			year = year.toString();
			if(Math.floor(Math.random() * 2) === 0) year += "/I";
			else year += "/II";
			
			var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
			if(diff === "Easy") problem = Math.floor(Math.random() * 5) + 1;
			else if(diff === "Medium") problem = Math.floor(Math.random() * 5) + 6;
			else if(diff === "Hard") problem = Math.floor(Math.random() * 3) + 11;
			else if(diff === "VeryHard") problem = Math.floor(Math.random() * 2) + 14;
		}
		else if(test === "AMC8") {
			year = Math.floor(Math.random() * 6) + 2014;
			year = year.toString();
			var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
			if(diff === "Easy") problem = Math.floor(Math.random() * 15) + 1;
			else if(diff === "Medium") problem = Math.floor(Math.random() * 3) + 16;
			else if(diff === "Hard") problem = Math.floor(Math.random() * 4) + 19;
			else if(diff === "VeryHard") problem = Math.floor(Math.random() * 3) + 23;
		}
		else {
			year = Math.floor(Math.random() * 6) + 2015;
			year = year.toString();
			if(Math.floor(Math.random() * 2) === 0) year += "/A";
			else year += "/B";
			var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
			if(diff === "Easy") problem = Math.floor(Math.random() * 15) + 1;
			else if(diff === "Medium") problem = Math.floor(Math.random() * 3) + 16;
			else if(diff === "Hard") problem = Math.floor(Math.random() * 4) + 19;
			else if(diff === "VeryHard") problem = Math.floor(Math.random() * 3) + 23;
		}
			
		problem = problem.toString();				
		if(problem.length === 1) problem = "0" + problem;
		problem += ".html";
		problemURL = test + "/" + year + "/" + problem;
						
		// users may run out of problems, if the system remembers problems
		while(getMapValue(visited, problemURL)) {
			visited.set(problemURL, true);
			if(test === "AIME") {
				year = Math.floor(Math.random() * 5) + 2015;
				year = year.toString();
				if(Math.floor(Math.random() * 2) === 0) year += "/I";
				else year += "/II";
				
				var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
				if(diff === "Easy") problem = Math.floor(Math.random() * 5) + 1;
				else if(diff === "Medium") problem = Math.floor(Math.random() * 5) + 6;
				else if(diff === "Hard") problem = Math.floor(Math.random() * 3) + 11;
				else if(diff === "VeryHard") problem = Math.floor(Math.random() * 2) + 14;
			}
			else if(test === "AMC8") {
				year = Math.floor(Math.random() * 6) + 2014;
				year = year.toString();
				var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
				if(diff === "Easy") problem = Math.floor(Math.random() * 15) + 1;
				else if(diff === "Medium") problem = Math.floor(Math.random() * 3) + 16;
				else if(diff === "Hard") problem = Math.floor(Math.random() * 4) + 19;
				else if(diff === "VeryHard") problem = Math.floor(Math.random() * 3) + 23;
			}
			else {
				year = Math.floor(Math.random() * 6) + 2015;
				year = year.toString();
				if(Math.floor(Math.random() * 2) === 0) year += "/A";
				else year += "/B";
				var diff = levels.get(test)[Math.floor(Math.random() * levels.get(test).length)];
				if(diff === "Easy") problem = Math.floor(Math.random() * 15) + 1;
				else if(diff === "Medium") problem = Math.floor(Math.random() * 3) + 16;
				else if(diff === "Hard") problem = Math.floor(Math.random() * 4) + 19;
				else if(diff === "VeryHard") problem = Math.floor(Math.random() * 3) + 23;
			}
			
			problem = problem.toString();				
			if(problem.length === 1) problem = "0" + problem;
			problem += ".html";
			problemURL = test + "/" + year + "/" + problem;
		}
		problemURLS.push(problemURL);
	}
}
