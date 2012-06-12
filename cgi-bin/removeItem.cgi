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
use Switch;

# path db films
my $filmsXml = "../xml/films.xml";
# path db serie tv
my $seriesXml = "../xml/series.xml";
# path db utenti
my $usersXml = "../xml/users.xml";
# path db commenti
my $commentsXml = "../xml/comments.xml";


my $q=new CGI;

# se non è un admin
if( function::checkIsAdmin() eq "false"){
    print $q->redirect("index.cgi");
}



my $type = $q->param('type');



switch ($type ) {
    case "film" {  
        my $id = $q->param('id');
	    function::removeItem({ type=>$type, id=>$id });
	    print $q->header(-location => q[index.cgi]);   
	    last;
	}
	case "serie"  {
	    my $id = $q->param('id');
	    function::removeItem({ type=>$type, id=>$id });
	    last;
	}
	case "comment"  {
	    my $id = $q->param('id');
	    function::removeItem({ type=>$type, id=>$id });
	    print $q->header(-location => q[index.cgi]);   
	    last;
	}
	case "link" {
	    my $idFilm = $q->param('idFilm');
	    my $idLink = $q->param('idLink');
	    function::removeLink({ idFilm=>$idFilm, idLink=>$idLink });
	    print $q->redirect("film.cgi?id=$idFilm"); 
        last;
	}

	case "user" {
	    my $idUser = $q->param('id');
	    function::removeUser({ idUser=>$idUser });
        my $session = CGI::Session->load();
        $session->delete();
        my $page=new CGI;
        print $page->redirect("index.cgi");
	    
	    
	    #print $q->redirect("logout.cgi"); 
        last;
	}
    
    
}

