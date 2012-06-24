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
				<a href="researchFilm.cgi?type=Year&value=all" tabindex="5" ><b>Tutti</b></a><br />
				<a href="researchFilm.cgi?type=Year&value=2012" tabindex="5" >2012</a><br />
				<a href="researchFilm.cgi?type=Year&value=2011" tabindex="5" >2011</a><br />
				<a href="researchFilm.cgi?type=Year&value=2010" tabindex="5" >2010</a><br />
				<a href="researchFilm.cgi?type=Year&value=2009" tabindex="5" >2009</a><br />
				<a href="researchFilm.cgi?type=Year&value=2008" tabindex="5" >2008</a><br />
				<a href="researchFilm.cgi?type=Year&value=2007" tabindex="5" >2007</a><br />
				<a href="researchFilm.cgi?type=Year&value=2006" tabindex="5" >2006</a><br />
				<a href="researchFilm.cgi?type=Year&value=2005" tabindex="5" >2005</a><br />
				<a href="researchFilm.cgi?type=Year&value=2004" tabindex="5" >2004</a><br />
				<a href="researchFilm.cgi?type=Year&value=2003" tabindex="5" >2003</a><br />
				<a href="researchFilm.cgi?type=Year&value=2002" tabindex="5" >2002</a><br />
				<a href="researchFilm.cgi?type=Year&value=2001" tabindex="5" >2001</a><br />
				<a href="researchFilm.cgi?type=Year&value=pre-2001" tabindex="5" >pre-2001</a><br />
			</div>
			<div id="genre">
				<h2>Genere</h2><br />
				<a href="researchFilm.cgi?type=Family&value=Action" tabindex="5" >Action</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Thriller" tabindex="5" >Thriller</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Horror" tabindex="5" >Horror</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Comics" tabindex="5" >Comics</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Cartoon" tabindex="5" >Cartoon</a><hr />
				<a href="researchFilm.cgi?type=Family&value=Vario" tabindex="5" >Altro</a><hr />
			</div>
		</div>

BODY

function->footer();
