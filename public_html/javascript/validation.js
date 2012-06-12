// JavaScript Document

var name=0;
var surname=0;
var user=0;
var mail=0;
var psw=0;
var confirm=0;
var pass = "";
var title=0;
var descr=0;
var data=0;
var url=0;

function checkName() {
		var temp = document.getElementById("name").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("name").style.backgroundColor = "#F00";
			document.getElementById("nameError").style.display = "inline";
			document.getElementById("nameCorrect").style.display = "none";
			name=0;
		}
		if (posizione == 0) {
			document.getElementById("name").style.backgroundColor = "#00CC00";
			document.getElementById("nameError").style.display = "none";
			document.getElementById("nameCorrect").style.display = "inline";
			name=1;
		}
		if (temp == "") {
			document.getElementById("name").style.backgroundColor = "#F00";
			document.getElementById("nameError").style.display = "inline";
			document.getElementById("nameCorrect").style.display = "none";
			name=0;
		}
		total();
}

function checkSurname() {
		var temp = document.getElementById("surname").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("surname").style.backgroundColor = "#F00";
			document.getElementById("surnameError").style.display = "inline";
			document.getElementById("surnameCorrect").style.display = "none";
			surname=0;
		}
		if (posizione == 0) {
			document.getElementById("surname").style.backgroundColor = "#00CC00";
			document.getElementById("surnameError").style.display = "none";
			document.getElementById("surnameCorrect").style.display = "inline";
			surname=1;
		}
		if (temp == "") {
			document.getElementById("surname").style.backgroundColor = "#F00";
			document.getElementById("surnameError").style.display = "inline";
			document.getElementById("surnameCorrect").style.display = "none";
			surname=0;
		}
		total();
}

function checkUser() {
		var temp = document.getElementById("user").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("user").style.backgroundColor = "#F00";
			document.getElementById("userError").style.display = "inline";
			document.getElementById("userCorrect").style.display = "none";
			user=0;
		}
		if (posizione == 0) {
			document.getElementById("user").style.backgroundColor = "#00CC00";
			document.getElementById("userError").style.display = "none";
			document.getElementById("userCorrect").style.display = "inline";
			user=1;
		}
		if (temp == "") {
			document.getElementById("user").style.backgroundColor = "#F00";
			document.getElementById("userError").style.display = "inline";
			document.getElementById("userCorrect").style.display = "none";
			user=0;
		}
		total();
}

function checkEmail() {
	if (document.getElementById) {
		var email = document.getElementById("email").value;
		var posizione = email.search(/^([\w\-\+\.]+)([\w]+)@([\w]+)([\w\-\+\.]+).([\w\-\+\.]+)$/);
		if (posizione != 0 && email != "") {
			document.getElementById("email").style.backgroundColor = "#F00";
			document.getElementById("emailError").style.display = "inline";
			document.getElementById("emailCorrect").style.display = "none";
			mail=0;
		}
		if (posizione == 0) {
			document.getElementById("email").style.backgroundColor = "#00CC00";
			document.getElementById("emailError").style.display = "none";
			document.getElementById("emailCorrect").style.display = "inline";
			mail=1;
		}
		if (email == "") {
			document.getElementById("email").style.backgroundColor = "#FFFFFF";
			document.getElementById("emailError").style.display = "none";
			document.getElementById("emailCorrect").style.display = "none";
			mail=0;
		}
	}
	total();
}

function checkPassword() {
		var password = document.getElementById("password").value;
		var posizione = password.search(/^[a-zA-Z0-9\_\*\-\+\!\?\,\:\;\.\xE0\xE8\xE9\xF9\xF2\xEC\x27]{6,12}/);
		if (posizione != 0 && password != "") {
			document.getElementById("password").style.backgroundColor = "#F00";
			document.getElementById("passwordError").style.display = "inline";
			document.getElementById("passwordCorrect").style.display = "none";
			psw=0;
		}
		if (posizione == 0) {
			document.getElementById("password").style.backgroundColor = "#00CC00";
			document.getElementById("passwordError").style.display = "none";
			document.getElementById("passwordCorrect").style.display = "inline";
			pass=password;
			psw=1;
		}
		if (password == "") {
			document.getElementById("password").style.backgroundColor = "#FFFFFF";
			document.getElementById("passwordError").style.display = "none";
			document.getElementById("passwordCorrect").style.display = "none";
			psw=0;
		}
		repeatPassword();
		total();
}

function repeatPassword() {
	var confirmed = document.getElementById("confirmPassword").value;
	if(confirmed == pass && confirmed != ""){
			document.getElementById("confirmPassword").style.backgroundColor = "#00CC00";
			document.getElementById("confirmedError").style.display = "none";
			document.getElementById("confirmedCorrect").style.display = "inline";
			confirm=1;
	}
	else{
			document.getElementById("confirmPassword").style.backgroundColor = "#F00";
			document.getElementById("confirmedError").style.display = "inline";
			document.getElementById("confirmedCorrect").style.display = "none";
			confirm=0;
	}
	total();
}

function checkTitle() {
		var temp = document.getElementById("title").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			document.getElementById("titleError").style.display = "inline";
			document.getElementById("titleCorrect").style.display = "none";
			title=0;
		}
		if (posizione == 0) {
			document.getElementById("title").style.backgroundColor = "#00CC00";
			document.getElementById("titleError").style.display = "none";
			document.getElementById("titleCorrect").style.display = "inline";
			title=1;
		}
		if (temp == "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			document.getElementById("titleError").style.display = "inline";
			document.getElementById("titleCorrect").style.display = "none";
			title=0;
		}
		totalFilm();
}

function checkTitleSerie() {
		var temp = document.getElementById("title").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			document.getElementById("titleError").style.display = "inline";
			document.getElementById("titleCorrect").style.display = "none";
			title=0;
		}
		if (posizione == 0) {
			document.getElementById("title").style.backgroundColor = "#00CC00";
			document.getElementById("titleError").style.display = "none";
			document.getElementById("titleCorrect").style.display = "inline";
			title=1;
		}
		if (temp == "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			document.getElementById("titleError").style.display = "inline";
			document.getElementById("titleCorrect").style.display = "none";
			title=0;
		}
		totalSerie();
}

function checkDescr() {
		var temp = document.getElementById("description").value;
		if (temp == "") {
			document.getElementById("descrError").style.display = "inline";
			document.getElementById("descrCorrect").style.display = "none";
			descr=0;
		}
		else
		{
			document.getElementById("descrError").style.display = "none";
			document.getElementById("descrCorrect").style.display = "inline";
			descr=1;
		}
		totalFilm();
}

function checkDescrSerie() {
		var temp = document.getElementById("description").value;
		if (temp == "") {
			document.getElementById("descrError").style.display = "inline";
			document.getElementById("descrCorrect").style.display = "none";
			descr=0;
		}
		else
		{
			document.getElementById("descrError").style.display = "none";
			document.getElementById("descrCorrect").style.display = "inline";
			descr=1;
		}
		totalSerie();
}

function total() {
	document.getElementById("end").disabled=false;
	var test = name+surname+mail+user+psw+confirm;
	if(test == 6){
		document.getElementById("end").disabled=false;
	}
	else{
		document.getElementById("end").disabled =true;
	}
}

function checkDate(){
	
		var temp = document.getElementById("date").value;
		var posizione = temp.search(/^\d{4}\-\d{1,2}\-\d{1,2}$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("date").style.backgroundColor = "#F00";
			document.getElementById("dataError").style.display = "inline";
			document.getElementById("dataCorrect").style.display = "none";
			data=0;
		}
		if (posizione == 0) {
			document.getElementById("date").style.backgroundColor = "#00CC00";
			document.getElementById("dataError").style.display = "none";
			document.getElementById("dataCorrect").style.display = "inline";
			data=1;
		}
		if (temp == "") {
			document.getElementById("date").style.backgroundColor = "#F00";
			document.getElementById("dataError").style.display = "inline";
			document.getElementById("dataCorrect").style.display = "none";
			data=0;
		}
		totalFilm();
}

function totalFilm() {
	document.getElementById("newFilm").disabled=false;
	var test = title+descr+data;
	if(test == 3){
		document.getElementById("newFilm").disabled=false;
	}
	else{
		document.getElementById("newFilm").disabled =true;
	}
}

function totalSerie() {
	document.getElementById("newSerie").disabled=false;
	var test = title+descr;
	if(test == 2){
		document.getElementById("newSerie").disabled=false;
	}
	else{
		document.getElementById("newSerie").disabled =true;
	}
	
}

function checkTitleLink() {
		var temp = document.getElementById("title").value;
		var posizione = temp.search(/^\D{3}(\D)*$/);
		if (posizione != 0 && temp != "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			title=0;
		}
		if (posizione == 0) {
			document.getElementById("title").style.backgroundColor = "#00CC00";
			title=1;
		}
		if (temp == "") {
			document.getElementById("title").style.backgroundColor = "#F00";
			title=0;
		}
		totalLink();
}

function checkUrlLink() {
		var temp = document.getElementById("link").value;
		var posizione = temp.search(/[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi);
		if (posizione != 0 && temp != "") {
			document.getElementById("link").style.backgroundColor = "#F00";
			url=0;
		}
		if (posizione == 0) {
			document.getElementById("link").style.backgroundColor = "#00CC00";
			url=1;
		}
		if (temp == "") {
			document.getElementById("link").style.backgroundColor = "#F00";
			url=0;
		}
		totalLink();
}

function totalLink() {
	document.getElementById("newLink").disabled=false;
	var test = title+url;
	if(test == 2){
		document.getElementById("newLink").disabled=false;
	}
	else{
		document.getElementById("newLink").disabled =true;
	}
}


