function getCheckedValue( radioName ){
	// Get radio group by-name
    var radios = document.getElementsByName( radioName );
    for(var y = 0; y < radios.length; y++)
		// return the checked value
		if(radios[y].checked) return radios[y].value;
}

function getAnswer( qn ) {
	testType = problemURLS[qn].split("/")[0];
	if(testType === "aime") {
		return document.getElementById("aimeAnswer" + qn).value;
		
	}
	else {
		return getCheckedValue("amcAnswer" + qn);
	}
}
var ua, ca;
function checkAnswer( qn ) {
	var userAnswer = getAnswer( qn );
	var currentData = problemURLS[qn].split("/");
	var testType = currentData[0];
	var answerURL = "";
	var solutionsURL =
		"https://artofproblemsolving.com/wiki/index.php/";
	var problemNumber = 0;
	if(testType === "amc8") {
		solutionsURL += currentData[1];
		solutionsURL += "_AMC_8_Problems/Problem_";
		for(var i = 0; i < 2; i++) {
			answerURL += currentData[i];
			answerURL += "/";
		}
		answerURL += "answers.txt";
		problemNumber = parseInt(currentData[2].substr(0, 2), 10);
	}
	else {
		solutionsURL += currentData[1];
		if(testType === "aime") {
			solutionsURL +=
				"_AIME_" + currentData[2] + "_Problems/Problem_";
		}
		else if(testType === "amc10") {
			solutionsURL +=
				"_AMC_10" + currentData[2] + "_Problems/Problem_";
		}
		else {
			solutionsURL +=
				"_AMC_12" + currentData[2] + "_Problems/Problem_";
		}
		for(var i = 0; i < 3; i++) {
			answerURL += currentData[i];
			answerURL += "/";
		}
		answerURL += "answers.txt";
		problemNumber = parseInt(currentData[3].substr(0, 2), 10);
	}
	solutionsURL += problemNumber.toString();
	
	var statusText = document.getElementById("problemStatus" + qn);
	if(testType === "aime") {
		userAnswer = parseInt(userAnswer, 10);
		var client = new XMLHttpRequest();
		client.open('GET', answerURL);
		client.onreadystatechange = function() {
			if( client.responseText != '' ) {
				var txt = client.responseText.split("\n");
				correctAnswer = parseInt(txt[problemNumber - 1], 10);
				if(correctAnswer === userAnswer) {
					statusText.className = "correct";
					
					var correctAnswerPlusSolution =
					'Correct Answer! <a href="' + solutionsURL +
					'" class="sol" target="_blank" rel="noopener' +
					'noreferrer">View Solution on AoPS Wiki</a>';
					statusText.innerHTML = correctAnswerPlusSolution;
					
					var submitForm =
						document.getElementById("aimeSubmitForm" + qn);
					if(submitForm != null) {
						submitForm.parentNode.removeChild(submitForm);
					}
				}
				else {
					statusText.className = "wrong";
					statusText.innerText = "Wrong Answer!";
				}
			}
		}
		client.send();
	}
	else {
		var client = new XMLHttpRequest();
		client.open('GET', answerURL);
		client.onreadystatechange = function() {
			if( client.responseText != '' ) {
				var txt = client.responseText.split("\n");
				correctAnswerTemp = txt[problemNumber - 1];
				var correctAnswer = "";
				for(var i = 0; i < correctAnswerTemp.length; i++) {
					if(!(correctAnswerTemp[i] == '\n'
						 || correctAnswerTemp[i] == '\r')) {
							correctAnswer += correctAnswerTemp[i];
					}
				}
				ca = correctAnswer;
				ua = userAnswer;
				if(correctAnswer === userAnswer) {
					statusText.className = "correct";
					
					var correctAnswerPlusSolution =
					'Correct Answer! <a href="' + solutionsURL +
					'" class="sol" target="_blank" rel="noopener' +
					'noreferrer">View Solution on AoPS Wiki</a>';
					statusText.innerHTML = correctAnswerPlusSolution;
					
					var submitForm =
						document.getElementById("amcSubmitForm" + qn);
					if(submitForm != null) {
						submitForm.parentNode.removeChild(submitForm);
					}
				}
				else {
					statusText.className = "wrong";
					statusText.innerText = "Wrong Answer!";
				}
			}
		}
		client.send();
	}
}
