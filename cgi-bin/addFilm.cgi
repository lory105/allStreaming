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
						<form name="addFilm" method="post" action="validation::validation(this);">
							<fieldset>
								<legend align="center" >Copila tutti i campi</legend>

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
								<span class="dx"><select id="giorno" tabindex="10" name="giorno">
                                    <option value="horror">Horror</option>
                                    <option value="sex">Sex</option>
                                    <option value="action">Action</option>
                                    <option value="04">4</option>
                                    <option value="05">5</option>
                                    <option value="06">6</option>
                                    <option value="07">7</option>
                                    <option value="08">8</option>
                                </select></span>
								</br>
    							<hr></hr>								
								<span class="sx"><label for="description">Description:</label></span><br />
								<span ><textarea rows=“10" cols="40" id="description" name="description" value="description" >description</textarea></span>								
								</br>
								<hr></hr>							
								<button type="submit">Invia</button>				
							</fieldset>
						</form>
		</div>
BODY

function->footer();