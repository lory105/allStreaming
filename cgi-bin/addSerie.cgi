#!/usr/bin/perl
# script per l'inserimento di una nuova serie TV 

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
    function->left("Serie");
    function->right();
       
    print<<BODY;
		<div id="registration">
			<h1>Inserimento nuova serie</h1>
						<form name="addSerie" method="post" action="checkSerie.cgi" enctype="multipart/form-data">
							<fieldset>
								<legend>Compila tutti i campi</legend>
								<span class="sx"><label for="title">Title:</label></span>
								<span class="dx"><input type="text" id="title" name="title" value="title" onblur="checkTitleSerie();" tabindex="5" /></span><span class="wrongValue" id="titleError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="titleCorrect"><img src="../images/ok.gif" alt="ok"/></span>
								<br />
								<hr />
								<span class="sx"><label for="image">Image:</label></span>
								<span class="dx"><input type="file" name="image" value="image" tabindex="5" /></span>
								<br />
    							<hr />								
								<span class="sx"><label for="description">Description:</label></span>
								<span class="dx"><textarea rows="2" cols="40" id="description" name="description" value="description" onblur="checkDescrSerie();" tabindex="5" >description</textarea></span><span class="wrongValue" id="descrError"><img src="../images/no.gif" alt="errore"/></span><span class="correctValue" id="descrCorrect"><img src="../images/ok.gif" alt="ok"/></span>							
								<br />
								<br />
								<br />
								<hr />							
								<button type="submit" id="newSerie" disabled="disabled" tabindex="5" >Invia</button>				
							</fieldset>
						</form>
		</div>
BODY

    function->footer();
}
