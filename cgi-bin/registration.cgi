#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Session ( '-ip_match' );

function->header();
function->left();
function->right();



print <<CENTER;
		<div id="registration">
			<h1>Registrazione nuovo utente</h1>
						<form name="registration" method="post" action="validation::validation(this);">
							<fieldset>
								<legend align="center" >Insert all fields</legend>

								<span class="sx"><label for="name">Name:</label></span>
								<span class="dx"><input type="text" name="name" value="nome" /></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="surname">Cognome:</label></span>
								<span class="dx"><input type="text" name="surname" value="cognome" /></span>
								</br>
								<hr></hr>								
								<span class="sx"><label for="username">Username:</label></span>
								<span class="dx"><input type="text" name="username" id="username" value="username" /></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="email">Email:</label></span>
								<span class="dx"><input type="text" name="email" id="email" value="your\@email.com"/></span>
								</br>
								<hr></hr>						
								<span class="sx"><label for="password">Password:</label></span>
								<span class="dx"><input type="password" name="password" id="password" value="password" /></span>
								</br>
								<hr></hr>							
								<span class="sx"><label for="confirm_password">Conferma password:</label></span>
								<span class="dx"><input type="password" name="confirm_password" id="password" value="password" /></span>
								</br>
								<hr></hr>
								<button type="submit">Invia</button>				
							</fieldset>
						</form>
		</div>

CENTER

function->footer();
