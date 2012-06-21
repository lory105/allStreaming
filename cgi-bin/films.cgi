#!/usr/bin/perl
# script per la visualizzazione dei film

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("Film");
function->right();
       
print<<BODY;
		<div id="center_side">
			<h1>Film disponibili</h1>
			<div id="year">
				<h2>Anno d'uscita</h2>
				<a href="researchFilm.cgi?type=Year&value=2012">2012</a><br />
				<a href="researchFilm.cgi?type=Year&value=2011">2011</a><br />
				<a href="researchFilm.cgi?type=Year&value=2010">2010</a><br />
				<a href="researchFilm.cgi?type=Year&value=2009">2009</a><br />
				<a href="researchFilm.cgi?type=Year&value=2008">2008</a><br />
				<a href="researchFilm.cgi?type=Year&value=2007">2007</a><br />
				<a href="researchFilm.cgi?type=Year&value=2006">2006</a><br />
				<a href="researchFilm.cgi?type=Year&value=2005">2005</a><br />
				<a href="researchFilm.cgi?type=Year&value=2004">2004</a><br />
				<a href="researchFilm.cgi?type=Year&value=2003">2003</a><br />
				<a href="researchFilm.cgi?type=Year&value=2002">2002</a><br />
				<a href="researchFilm.cgi?type=Year&value=2001">2001</a><br />
				<a href="researchFilm.cgi?type=Year&value=2000">2000</a><br />
				<a href="researchFilm.cgi?type=Year&value=pre-2000">pre-2000</a><br />
			</div>
			<div id="genre">
				<h2>Genere</h2><br />
				<a href="researchFilm.cgi?type=Family&value=Action">Action</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Thriller">Thriller</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Horror">Horror</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Comics">Comics</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Cartoon">Cartoon</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Vario">Altro</a><hr />
			</div>
		</div>

BODY

function->footer();
