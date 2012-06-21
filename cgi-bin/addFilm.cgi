#!/usr/bin/perl
# script per l'inserimento di un nuovo film

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# se non è l'admin lo redirigo alla home
if( function->checkIsAdmin() eq "false" ){
  	my $page=new CGI;
	print $page->redirect("index.cgi");
}


# altrimenti stampo la pagina
else{
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
								<span class="dx"><input type="text" id="title" name="title" value="title" onblur="checkTitle();" /></span><span class="wrongValue" id="titleError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="titleCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />
								<span class="sx"><label for="image">Image:</label></span>
								<span class="dx"><input type="file" name="image" id="image" value="image" /></span>
								<br />
								<hr />
								<span class="sx"><label for="date">Date (es: 2001-01-27):</label></span>
								<span class="dx"><input type="text" name="date" id="date" onblur="checkDate();"/></span><span class="wrongValue" id="dataError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="dataCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />						
								<span class="sx"><label for="family">Family:</label></span>
								<span class="dx"><select id="family" tabindex="10" name="family">
                                    <option value="Action">Action</option>
                                    <option value="Thriller">Thriller</option>
                                    <option value="Horror">Horror</option>
                                    <option value="Comics">Comics</option>
                                    <option value="Cartoon">Cartoon</option>
                                    <option value="Vario">Altro</option>
                                </select></span>
								<br />
    							<hr />								
								<span class="sx"><label for="description">Description:</label></span>
								<span class="dx"><textarea rows="2" cols="40" id="description" name="description" value="description" onblur="checkDescr();">description</textarea></span><span class="wrongValue" id="descrError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="descrCorrect"><img src="../images/ok.gif" alt="ok"/></span>								
								<br />
								<br />
								<br />
								<hr />							
								<button type="submit" id="newFilm" disabled="false">Invia</button>				
							</fieldset>
						</form>
		</div>
BODY

    function->footer();
}
