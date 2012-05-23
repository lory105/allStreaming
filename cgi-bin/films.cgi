#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("film");
function->right();
       
print<<BODY;
		<div id="center_side">
			<h1>Film disponibili</h1>
			<div id="year">
				<h2>Anno d'uscita</h2></br>
				<a href="film.cgi">2012</a></br>
				<a href="#">2011</a></br>
				<a href="#">2010</a></br>
				<a href="#">2009</a></br>
				<a href="#">2008</a></br>
				<a href="#">2007</a></br>
				<a href="#">2006</a></br>
				<a href="#">2005</a></br>
				<a href="#">2004</a></br>
				<a href="#">2003</a></br>
				<a href="#">2002</a></br>
				<a href="#">2001</a></br>
				<a href="#">2000</a></br>
				<a href="#">pre-2000</br>
			</div>
			<div id="genre">
				<h2>Genere</h2></br>
				<a href="film.cgi">Action</a><hr>
				<a href="#">Thriller</a><hr>
				<a href="#">Horror</a><hr>
				<a href="#">Comics</a><hr>
				<a href="#">Cartoon</a><hr>
				<a href="#">Altro</a><hr>
			</div>
		</div>

BODY

function->footer();
