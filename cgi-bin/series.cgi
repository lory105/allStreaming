#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;


function->header();
function->left("serie");
function->right();
       
print <<BODY;
		<div id="center_side">
			<h1>Serie Tv disponibili</h1>
				<a href="serie.cgi">Prima serie</a> <hr>
				<a href="serie.cgi">Seconda serie</a> <hr>
				<a href="serie.cgi">Terza serie</a> <hr>
				<a href="serie.cgi">Quarta serie</a> <hr>
				<a href="serie.cgi">Quinta serie</a> <hr>
				<a href="serie.cgi">Sesta serie</a> <hr>
				<a href="serie.cgi">Settima serie</a> <hr>
				<a href="serie.cgi">Ottava serie</a> <hr>
				<a href="serie.cgi">Nona serie</a> <hr>
				<a href="serie.cgi">Decima serie</a> <hr>
		</div>

BODY

function->footer();
