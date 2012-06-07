#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


# controllo se è l'admin
if( function->checkIsAdmin() eq "false" ){
    my $cgi = new CGI;
    print $cgi->header(-location => q[index.cgi]);   
}
else
{
	my $form = new CGI;
	my $title = $form->param('title');
	my $date = $form->param('date');
	my $family = $form->param('family');
	my $description = $form->param('description');
	
	my $upload_dir = "../public_html/images/films";

	my $upload_filehandle = $form->upload("image");
	open(UPLOADFILE, ">$upload_dir/$title.jpg") or die "Can't open the file!";
	binmode UPLOADFILE;
	while ( <$upload_filehandle> )
			{
				print UPLOADFILE;
			}
	close UPLOADFILE;

	function->header();
	function->left();
	function->right();
}
