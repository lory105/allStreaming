#!/usr/bin/perl 
# script che esegue il controllo per l'inserimento di link ad un film 
# o di un episodio ad una serie TV

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


# altrimenti inserisco il link o l'episodio
else{
    my $form = new CGI;
    my $type = $form->param('type');
    my $id = $form->param('id');

    if($type eq "film"){
    	my $title = $form->param('title');
	   my $link = $form->param('link');
        function::addFilmLinkf({ idFilm=>$id, linkName=>$title, link=>$link });
        my $page = new CGI;
        print $page->redirect("film.cgi?id=$id");
    }

    if($type eq "episode"){
	   my $idSeason = $form->param('idSeason');
	   my $title = $form->param('title');
	   my $link = $form->param('link');
	   function::addEpisode({idSerie=>$id, idSeason=>$idSeason, title=>$title, link=>$link});
        my $page = new CGI;
        print $page->redirect("serie.cgi?id=$id");
    }
    
}
