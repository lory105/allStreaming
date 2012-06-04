// JavaScript Document



function checkName() {
		var temp = document.getElementById("name").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("name").style.backgroundColor = "#F00";
			document.getElementById("nameError").style.display = "inline";
			document.getElementById("nameCorrect").style.display = "none";
		}
		if (posizione == 0) {
			document.getElementById("name").style.backgroundColor = "#00CC00";
			document.getElementById("nameError").style.display = "none";
			document.getElementById("nameCorrect").style.display = "inline";
		}
		if (temp == "") {
			document.getElementById("name").style.backgroundColor = "#F00";
			document.getElementById("nameError").style.display = "inline";
			document.getElementById("nameCorrect").style.display = "none";
		}
}

function checkSurname() {
		var temp = document.getElementById("surname").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("surname").style.backgroundColor = "#F00";
			document.getElementById("surnameError").style.display = "inline";
			document.getElementById("surnameCorrect").style.display = "none";
		}
		if (posizione == 0) {
			document.getElementById("surname").style.backgroundColor = "#00CC00";
			document.getElementById("surnameError").style.display = "none";
			document.getElementById("surnameCorrect").style.display = "inline";
		}
		if (temp == "") {
			document.getElementById("surname").style.backgroundColor = "#F00";
			document.getElementById("surnameError").style.display = "inline";
			document.getElementById("surnameCorrect").style.display = "none";
		}
}

function checkUser() {
		var temp = document.getElementById("user").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("user").style.backgroundColor = "#F00";
			document.getElementById("userError").style.display = "inline";
			document.getElementById("userCorrect").style.display = "none";
		}
		if (posizione == 0) {
			document.getElementById("user").style.backgroundColor = "#00CC00";
			document.getElementById("userError").style.display = "none";
			document.getElementById("userCorrect").style.display = "inline";
		}
		if (temp == "") {
			document.getElementById("user").style.backgroundColor = "#F00";
			document.getElementById("userError").style.display = "inline";
			document.getElementById("userCorrect").style.display = "none";
		}
}

function checkEmail() {
	if (document.getElementById) {
		var email = document.getElementById("email").value;
		var posizione = email.search(/^([\w\-\+\.]+)([\w]+)@([\w]+)([\w\-\+\.]+).([\w\-\+\.]+)$/);
		if (posizione != 0 && email != "") {
			document.getElementById("email").style.backgroundColor = "#F00";
			document.getElementById("emailError").style.display = "inline";
			document.getElementById("emailCorrect").style.display = "none";
		}
		if (posizione == 0) {
			document.getElementById("email").style.backgroundColor = "#00CC00";
			document.getElementById("emailError").style.display = "none";
			document.getElementById("emailCorrect").style.display = "inline";
		}
		if (email == "") {
			document.getElementById("email").style.backgroundColor = "#FFFFFF";
			document.getElementById("emailError").style.display = "none";
			document.getElementById("emailCorrect").style.display = "none";
		}
	}
}

function checkPassword() {
	if (document.getElementById) {
		var password = document.getElementById("password").value;
		var posizione = password.search(/^[a-zA-Z0-9\_\*\-\+\!\?\,\:\;\.\xE0\xE8\xE9\xF9\xF2\xEC\x27]{6,12}/);
		if (posizione != 0 && password != "") {
			document.getElementById("password").style.backgroundColor = "#F00";
			document.getElementById("passwordError").style.display = "inline";
			document.getElementById("passwordCorrect").style.display = "none";
		}
		if (posizione == 0) {
			document.getElementById("password").style.backgroundColor = "#00CC00";
			document.getElementById("passwordError").style.display = "none";
			document.getElementById("passwordCorrect").style.display = "inline";
		}
		if (password == "") {
			document.getElementById("password").style.backgroundColor = "#FFFFFF";
			document.getElementById("passwordError").style.display = "none";
			document.getElementById("passwordCorrect").style.display = "none";
		}
	}
}
