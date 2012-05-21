#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;


function->header();
function->left("home");
function->right();

#function->head_not_logged();
# function->navigation();
#function->menu();


print <<CENTER;

		<div id="center_side">

			<h1>Registrazione nuovo utente</h1>
				<div id="random_film">
					<div class="registration" >

						<form name="registration" action="check_registration.cgi" method="post">

							<fieldset>
							
								<!-- align=center è da mettere nel css, ho provato ma non va!! -->
								<legend align="center" >Insert all fields</legend>

								<label for="name">Name:</label>
								<input type="text" name="name" value="nome" /><br />
								
								<label for="surname">Cognome:</label>
								<input type="text" name="surname" value="cognome" /><br />								
								
								<label for="username">Username:</label>
								<input type="text" name="username" id="username" value="username" /><br />
	
								<label for="email">Email:</label>
								<input type="text" name="email" id="email" value="your\@email.com"/><br />
							
								<label for="password">Password:</label>
								<input type="password" name="password" id="password" value="password" /><br />
							
								<label for="confirm_password">Conferma password:</label>
								<input type="password" name="confirm_password" id="confirm_password" value="password" /><br />
							
								<input type="button" value="Invia" /><br />

							
							</fieldset>

						</form>

					</div>
				</div>

		</div>

CENTER

function->footer();
