#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# controllo se è l'admin
if( function->checkIsAdmin() eq "false" ){
    my $cgi = new CGI;
    print $cgi->header(-location => q[index.cgi]);   
}

function->header();
function->left("Serie");
function->right();

       
print<<BODY;
		<div id="registration">
			<h1>Inserimento nuova serie</h1>
						<form name="addSerie" method="post" action="checkSerie.cgi" enctype="multipart/form-data">
							<fieldset>
								<legend align="center" >Compila tutti i campi</legend>

								<span class="sx"><label for="title">Title:</label></span>
								<span class="dx"><input type="text" id="title" name="title" value="title" /></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="image">Image:</label></span>
								<span class="dx"><input type="file" name="image" value="image" /></span>
								</br>
    							<hr></hr>								
								<span class="sx"><label for="description">Description:</label></span>
								<span class="dx"><textarea rows=“10" cols="40" id="description" name="description" value="description" >description</textarea></span>								
								</br>
								</br>
								</br>
								<hr></hr>							
								<button type="submit">Invia</button>				
							</fieldset>
						</form>
		</div>
BODY

function->footer();
