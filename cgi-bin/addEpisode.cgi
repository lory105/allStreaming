#!/usr/bin/perl 

use strict;
use warnings;
use CGI;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use XML::XPath;
use XML::XPath::XMLParser;
use XML::LibXML;

	my $isAdmin = function::checkIsAdmin(); 
	if( $isAdmin eq "true"){
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
					<legend align="center" >Inserisci tutti i campi</legend>
					<input name="idSeason" value="$idSeason" type="hidden">
					<input name="type" value="episode" type="hidden">
					<input name="id" value="$id" type="hidden">			
					<label for="title">Titolo:</label>
					<input type="text" name="title" />
					<label for="link">Link:</label>
					<input type="text" name="link" />
					<input type="submit" value="Invia">
				</fieldset>
			 </form>
			</div>
CENTER
		function->footer();
		
	}
		
	else{
		
		my $page=new CGI;
		print $page->redirect("index.cgi");
    
	}


