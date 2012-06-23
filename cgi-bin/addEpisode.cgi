#!/usr/bin/perl 
# script per l'inserimento di un nuovo episodio ad una stagione di una serie TV

use strict;
use warnings;
use CGI;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use XML::XPath;
use XML::XPath::XMLParser;
use XML::LibXML;


# se non è l'admin lo redirigo alla home
if( function->checkIsAdmin() eq "false" ){
  	my $page=new CGI;
	print $page->redirect("index.cgi");
}


# altrimenti stampo la pagina
else{
    my $q=new CGI;
    my $idSeason = $q->param('idSeason');
    my $id= $q->param('id');
    function->header();
    function->left("Serie");
    function->right();
    
    print<<CENTER;  
	    <div id="center_side">
	    <h1>Aggiunta nuovo Episodio</h1>
	    <form method="post" action="checkLink.cgi">
            <fieldset>
            <legend>Inserisci tutti i campi</legend>
                    <input name="idSeason" value="$idSeason" type="hidden">
					<input name="type" value="episode" type="hidden">
					<input name="id" value="$id" type="hidden">			
					<label for="title">Titolo:</label>
					<input type="text" name="title" id="title" onblur="checkTitleLink();"/>
					<br />
					<label for="link">Link:</label>
					<input type="text" name="link" id="link" onblur="checkUrlLink();"/>
					<br />
					<button type="submit" id="newLink" disabled="disabled">Invia</button>
			</fieldset>
			</form>
			</div>
CENTER

    function->footer();
}
