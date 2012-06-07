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
function->left("Film");
function->right();

       
print<<BODY;
		<div id="registration">
			<h1>Inserimento nuovo film</h1>
						<form name="addFilm" method="post" action="checkFilm.cgi" enctype="multipart/form-data">
							<fieldset>
								<legend align="center" >Compila tutti i campi</legend>

								<span class="sx"><label for="title">Title:</label></span>
								<span class="dx"><input type="text" id="title" name="title" value="title" /></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="image">Image:</label></span>
								<span class="dx"><input type="file" name="image" id="image" value="image" /></span>
								</br>
								<hr></hr>
								<span class="sx"><label for="date">Date (es: 2001-01-27):</label></span>
								<span class="dx"><input type="text" name="date" id="date" /></span>
								</br>
								<hr></hr>						
								<span class="sx"><label for="family">Family:</label></span>
								<span class="dx"><select id="family" tabindex="10" name="family">
                                    <option value="Action">Action</option>
                                    <option value="Thriller">Thriller</option>
                                    <option value="Horror">Horror</option>
                                    <option value="Comics">Comics</option>
                                    <option value="Cartoon">Cartoon</option>
                                    <option value="Altro">Altro</option>
                                </select></span>
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
