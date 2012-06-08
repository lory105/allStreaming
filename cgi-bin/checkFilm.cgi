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

# controllo se è l'admin
if( function->checkIsAdmin() eq "false" ){
    my $cgi = new CGI;
    print $cgi->header(-location => q[index.cgi]);   
}
else{
	function->header();
	function->left("Film");
	function->right();
	
	my $form = new CGI;
	my $title = $form->param('title');
	my $date = $form->param('date');
	my $family = $form->param('family');
	my $description = $form->param('description');
	my $maxId = function->getMaxId("film");
    $maxId = "$maxId" + 1;
    my $image = "images/films/$maxId.jpg";
	my $upload_dir = "../public_html/images/films";
	my $upload_filehandle = $form->upload("image");
	open(UPLOADFILE, ">$upload_dir/$maxId.jpg") or die "Can't open the file!";
	binmode UPLOADFILE;
	while ( <$upload_filehandle> )
			{
				print UPLOADFILE;
			}
	close UPLOADFILE;
	function::addFilm({ title=>$title, image=>$image, description=>$description, date=>$date, family=>$family });
	    print <<CENTER;
        <div id="center_side">
			<h1>Successo</h1>
			<p>Il film &egrave stato inserito correttamente.</p>
        </div>
CENTER
function->footer();
}


