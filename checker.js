function getCheckedValue( radioName ){
    var radios = document.getElementsByName( radioName ); // Get radio group by-name
    for(var y=0; y<radios.length; y++)
		if(radios[y].checked) return radios[y].value; // return the checked value
}

function getAnswer( qn ) {
	btnType = document.getElementById("submitbtn" + qn).name;
	if(btnType === "amcsb") {
		return getCheckedValue("answer" + qn);
	}
	else { // aimesb
		return document.getElementById("answer" + qn).value;
	}
}
function checkAnswer( qn ) {
	var userAnswer = getAnswer( qn );
	var currentData = problemURLS[qn].split("/");
	var testType = currentData[0];
	var answerURL = "";
	var problemNumber = 0;
	if(testType === "amc8") {
		for(var i = 0; i < 2; i++) {
			answerURL += currentData[i];
			answerURL += "/";
		}
		answerURL += "answers.txt";
		problemNumber = parseInt(currentData[2].substr(0, 2), 10);
	}
	else {
		for(var i = 0; i < 3; i++) {
			answerURL += currentData[i];
			answerURL += "/";
		}
		answerURL += "answers.txt";
		problemNumber = parseInt(currentData[3].substr(0, 2), 10);
	}
	
	if(testType === "aime") {
		userAnswer = parseInt(userAnswer, 10);
		var client = new XMLHttpRequest();
		client.open('GET', answerURL);
		client.onreadystatechange = function() {
			if( client.responseText != '' ) {
				var txt = client.responseText.split("\n");
				correctAnswer = parseInt(txt[problemNumber - 1], 10);
				if(correctAnswer === userAnswer) {
					document.getElementById("problemStatus" + qn).className = "correct";
					document.getElementById("problemStatus" + qn).innerText = "Correct Answer!";
					var submitButton = document.getElementById("submitbtn" + qn);
					var label = document.getElementById("yourAnswer" + qn);
					var textBox = document.getElementById("answer" + qn);
					console.log(submitButton);
					console.log(label);
					console.log(textBox);
					console.log(label.parentNode.removeChild(label));
					console.log(textBox.parentNode.removeChild(textBox));
					console.log(submitButton.parentNode.removeChild(submitButton));
				}
				else {
					document.getElementById("problemStatus" + qn).className = "wrong";
					document.getElementById("problemStatus" + qn).innerText = "Wrong Answer!";
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
				correctAnswer = txt[problemNumber - 1];
				if(correctAnswer === userAnswer) {
					document.getElementById("problemStatus" + qn).className = "correct";
					document.getElementById("problemStatus" + qn).innerText = "Correct Answer!";
				}
				else {
					document.getElementById("problemStatus" + qn).className = "wrong";
					document.getElementById("problemStatus" + qn).innerText = "Wrong Answer!";
				}
			}
		}
		client.send();
	}
}
