#!/usr/bin/perl
# script per la visualizzazione della home page

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );
use XML::XPath;
use XML::XPath::XMLParser;
use XML::LibXML;


function->header();
function->left("Home");
function->right();


# se l'utente non è loggato o non è l'amministratore
if( function->isLogged() eq "false" || function->checkIsAdmin() eq "false" ){ 
    function::randomVideo({number=>"4"});
}

# se è l'amministratore
else{
    my $totFilms = function::findItem({ type=>"film", query=>"//collection/film"});
    $totFilms = $totFilms->size();
    my $totSeries = function::findItem({ type=>"serie", query=>"//collection/serie"});
    $totSeries = $totSeries->size();
    my $totUsers = function::findItem({ type=>"user", query=>"//collection/user"});
    $totUsers = $totUsers->size();
    my $totComments = function::findItem({ type=>"comment", query=>"//collection/comment"});
    $totComments = $totComments->size();
    
    print <<CENTER;
        <div id="center_side">
		    <h1>Pannello Admin</h1>
		        <div class="infoAdmin">
		            <p><b>Film totali:</b> $totFilms</p>
		            <form method="post" action="addFilm.cgi">
						<fieldset>
                        <input name="url" type="hidden">
                        <input type="submit" value="+ Aggiungi Film" tabindex="6">
                        </fieldset>
                    </form>
		        </div>
		        <div class="infoAdmin">
		            <p><b>Serie totali:</b> $totSeries</p>
		              <form method="post" action="addSerie.cgi">
						<fieldset>
                          <input name="url" type="hidden"">
                          <input type="submit" value="+ Aggiungi Serie" tabindex="7">
                        </fieldset>
                      </form>
		        </div>

                <div class="infoAdmin">
		            <p><b>Utenti totali:</b> $totUsers</p>
		        </div>
		        <div class="infoAdmin">
		            <p><b>Commenti totali:</b> $totComments</p>
		        </div>

	    </div>
	          
CENTER
}

function->footer();
