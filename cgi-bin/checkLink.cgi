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




	my $form = new CGI;
	my $type = $form->param('type');
	my $id = $form->param('id');


	if( function->checkIsAdmin() eq "false" ){
		my $cgi = new CGI;
		print $cgi->header(-location => q[index.cgi]);   
	}
	
	if($type eq "film"){
		my $title = $form->param('title');
		my $link = $form->param('link');
	    function::addFilmLinkf({ idFilm=>$id, linkName=>$title, link=>$link });
	    my $page = new CGI;
	    print $page->redirect("film.cgi?id=$id");
	}
	
