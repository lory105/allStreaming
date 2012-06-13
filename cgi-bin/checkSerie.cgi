#!/usr/bin/perl
# script che esegue il controllo per l'inserimento di una serie TV

use CGI;
use strict;
use warnings;
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


# altrimenti inserisco la seria
else{
    function->header();
    function->left("Serie");
    function->right();
	
    my $form = new CGI;
    my $title = $form->param('title');
    my $upload_filehandle = $form->upload("image");
    my $description = $form->param('description');
    my $maxId = function->getMaxId("serie");
    $maxId = "$maxId" + 1;
    my $image = "images/series/$maxId.jpg";
    my $upload_dir = "../public_html/images/series";
    open(UPLOADFILE, ">$upload_dir/$maxId.jpg") or die "Can't open the file!";
    binmode UPLOADFILE;
    while ( <$upload_filehandle> ){
	   print UPLOADFILE;
    }
    close UPLOADFILE;

    function::addSerie({ title=>$title, image=>$image, description=>$description });
    print <<CENTER;
        <div id="center_side">
			<h1>Successo</h1>
			<p>La serie &egrave stata inserita correttamente.</p>
        </div>
CENTER
    function->footer();
}
