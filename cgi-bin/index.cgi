#!/usr/bin/perl

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


my $session = CGI::Session->load();
my $admin = $session->param('admin');

# se l'utente non è loggato o non è l'amministratore
if($session->is_expired || $session->is_empty || $admin eq "false" ){ function::randomVideo({number=>"4"}); }

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
		    <div id="random_film" class="center">
		        <div class="infoAdmin">
		            <p>Film totali: $totFilms</p>
		            <form method="post" action="addFilm.cgi">
                        <input name="url" type="hidden"">
                        <input type="submit" value="+ Add Film">
                    </form>
		        </div>
		        <div class="infoAdmin">
		            <p>Serie totali: $totSeries</p>
		              <form method="post" action="addSerie.cgi">
                          <input name="url" type="hidden"">
                          <input type="submit" value="+ Add Serie">
                      </form>
		        </div>
                <div class="infoAdmin">
		            <p>Utenti totali: $totUsers</p>
		        </div>
		        <div class="infoAdmin">
		            <p>Commenti totali: $totComments</p>
		        </div>
	        </div>
	    </div>
	          
CENTER
    
    
}


function->footer();
