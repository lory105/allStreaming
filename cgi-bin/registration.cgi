#!/usr/bin/perl
# script per la visualizzazione della pagina di registrazione

use CGI;
use strict;
use warnings;
use function;
use CGI::Session ( '-ip_match' );



# se l'utente è già loggato lo redirigo alla home
if( function->isLogged() eq "true"){
  	my $page=new CGI;
	print $page->redirect("index.cgi");
}

# altrimenti stampo la pagine per la registrazione
else{
    function->header();
    function->left("Registrazione");
    function->right();

    print <<CENTER;
		<div id="registration">
			<h1>Registrazione nuovo utente</h1>
						<form name="registration" method="post" action="checkRegistration.cgi" enctype="multipart/form-data">
							<fieldset>
								<legend>Inserisci tutti i campi</legend>

								<span class="sx"><label for="name" tabindex="5">Name:</label></span>
								<span class="dx"><input type="text" name="name" id="name" value="nome" onblur="checkName();"  /></span><span class="wrongValue" id="nameError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="nameCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />
								<span class="sx"><label for="surname" tabindex="5">Cognome:</label></span>
								<span class="dx"><input type="text" name="surname" id="surname" value="cognome" onblur="checkSurname();"/></span><span class="wrongValue" id="surnameError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="surnameCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />								
								<span class="sx"><label for="user" tabindex="5">Username:</label></span>
								<span class="dx"><input type="text" name="username" id="user" value="username" onblur="checkUser();"/></span><span class="wrongValue" id="userError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="userCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />
								<span class="sx"><label for="email" tabindex="5">Email:</label></span>
								<span class="dx"><input type="text" name="email" id="email" value="your\@email.com" onblur="checkEmail();"/></span><span class="wrongValue" id="emailError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="emailCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />						
								<span class="sx"><label for="Password" tabindex="5">Password:</label></span>
								<span class="dx"><input type="password" name="password" id="Password" value="password" onblur="checkPassword();"/></span><span class="wrongValue" id="passwordError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="passwordCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />							
								<span class="sx"><label for="confirmPassword" tabindex="5">Conferma password:</label></span>
								<span class="dx"><input type="password" name="confirmPassword" id="confirmPassword" value="password" onblur="repeatPassword();"/></span><span class="wrongValue" id="confirmedError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="confirmedCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />
								<span class="sx"><label for="avatar" tabindex="5">Aggiungi avatar:</label></span>
								<span class="dx"><input type="file" name="photo" id="avatar" value=""/></span>
								<br />
								<hr />
								<button type="submit" id="end" disabled="disabled" tabindex="5">Invia</button>				
							</fieldset>
						</form>


CENTER

    my $form = new CGI;
    my $check = $form->param('err');
    if($check eq "true"){
	   print "<span class=\"wrongRegistration\" id=\"nameError\">Attenzione: Email o Username gi&agrave esistenti</span>";
    }
	
    print "</div>";

    function->footer();
}
    
