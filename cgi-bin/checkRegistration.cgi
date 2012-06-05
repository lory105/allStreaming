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



	my $form = new CGI;
	my $name = $form->param('name');
	my $surname = $form->param('surname');
	my $user = $form->param('username');
	my $email = $form->param('email');
	my $password = $form->param('password');
	
	my $testing = function->checkUserRegistration($user,$email);
	if ($testing->size() > 0){
		print $form->redirect('registration.cgi?err=true');
	}
	else{
		function->header(); 
		function->left();
		function->right();
		print <<CENTER;
		<div id="center_side">
				<h1>Benvenuto!</h1>
				<p>Ora potrai commentare e seguire attivamente tutte le nuove uscite di film e serie tv.</p>
				<p>Effettua il login con lo username e la password che hai appena inserito.</p>
				<p>Buona visione su allStreaming!</p>
		</div>

CENTER
}

function->footer();


