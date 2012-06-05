#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Session ( '-ip_match' );

function->header();
function->left("Registrazione");
function->right();

print <<CENTER;
		<div id="registration">
			<h1>Registrazione nuovo utente</h1>
						<form name="registration" method="post" action="checkRegistration.cgi" enctype="multipart/form-data">
							<fieldset>
								<legend align="center" >Inserisci tutti i campi</legend>

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
								<span class="sx"><label for="upload">Aggiungi avatar:</label></span>
								<span class="dx"><input type="file" name="photo" id="avatar" value=""/></span>
								</br>
								<hr></hr>
								<button type="submit" id="end" disabled="false">Invia</button>				
							</fieldset>
						</form>


CENTER

	my $form = new CGI;
	my $check = $form->param('err');
	if($check eq "true"){
		print "<span class=\"wrongRegistration\" id=\"nameError\">Attenzione: Email o Username gi&agrave esistenti</span>";
	}
	
print <<TEST;
						
		</div>
TEST

function->footer();
