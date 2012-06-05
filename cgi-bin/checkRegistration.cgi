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

    my $filename =~ /([^<>]*)/;
    $filename = $1;
    open(FILEHANDLE, "<", $filename);

	my $form = new CGI;
	my $name = $form->param('name');
	my $surname = $form->param('surname');
	my $user = $form->param('username');
	my $email = $form->param('email');
	my $password = $form->param('password');
	my $dateRegistration   = DateTime->now;
	my $avatar = "../avatar/jack.png";
	
	my $upload_dir = "../public_html/images/avatars";


	
	my $testing = function->checkUserRegistration($user,$email);
	

	
	
	if ($testing->size() > 0){
		print $form->redirect('registration.cgi?err=true');
	}
	else{
		function->header(); 
		function->left();
		function->right();
		my $upload_filehandle = $form->upload("photo");
		open(UPLOADFILE, ">$upload_dir/$user.jpg") or die "Can't open '$upload_dir/$filename': $!";
		binmode UPLOADFILE;

		while ( <$upload_filehandle> )
			{
				print UPLOADFILE;
			}
		close UPLOADFILE;
	
		
		function::addUser({ name=>$name, surname=>$surname, username=>$user, password=>$password, email=>$email, avatar=>$avatar, dateRegistration=>$dateRegistration, admin=>"false" });
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



