#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Session ( '-ip_match' );

print "Content-type: text/html\n\n";
print <<HEADER;
	<?xml version="1.0" encoding="iso-8859-1"?>
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
		<head>
			<title>AllStreaming</title>
			<link rel="shortcut icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="icon" href="images/logo.ico" type="image/x-icon" />
			<link rel="stylesheet" href="../styles/style.css" type="text/css" />
			<script src="../javascript/validation.js" type="text/javascript" ></script>
		</head> 
	
HEADER
function->left();
function->right();

my %input = ("name" => "default");

print <<CENTER;
		<div id="registration">
			<h1>Registrazione nuovo utente</h1>
						<form name="registration" method="post">
							<fieldset>
								<legend align="center" >Insert all fields</legend>

								<span class="sx"><label for="name">Name:</label></span>
								<span class="dx"><input type="text" name="name" id="name" value="nome" onblur="checkName();"  /></span><span class="wrongValue" id="nameError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="nameCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="surname">Cognome:</label></span>
								<span class="dx"><input type="text" name="surname" id="surname" value="cognome" onblur="checkSurname();"/></span><span class="wrongValue" id="surnameError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="surnameCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>								
								<span class="sx"><label for="username">Username:</label></span>
								<span class="dx"><input type="text" name="username" id="user" value="username" onblur="checkUser();"/></span><span class="wrongValue" id="userError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="userCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="email">Email:</label></span>
								<span class="dx"><input type="text" name="email" id="email" value="your\@email.com" onblur="checkEmail();"/></span><span class="wrongValue" id="emailError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="emailCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>						
								<span class="sx"><label for="password">Password:</label></span>
								<span class="dx"><input type="password" name="password" id="password" value="password" onblur="checkPassword();"/></span><span class="wrongValue" id="passwordError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="passwordCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>							
								<span class="sx"><label for="confirm_password">Conferma password:</label></span>
								<span class="dx"><input type="password" name="confirmPassword" id="confirmPassword" value="password" onblur="repeatPassword();"/></span><span class="wrongValue" id="confirmedError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="confirmedCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								</br>
								<hr></hr>
								<button type="submit" onClick="total();" id="end" disabled="false">Invia</button>				
							</fieldset>
						</form>
		</div>

CENTER

function->footer();
