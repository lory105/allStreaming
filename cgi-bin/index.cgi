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




function->header(); 
function->left("home");
function->right();

print <<CENTER;
		<div id="center_side">
				<h1>Film Consigliati</h1>
				<div id="random_film">
						<div class="film">
							<img src="../images/1.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Sin City</a>
						</div>
						<div class="film">
							<img src="../images/2.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Shining</a>
						</div>
						<div class="film">
							<img src="../images/3.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Harry Potter</a>
						</div>
						<div class="film">
							<img src="../images/4.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:I want you</a>
						</div>
	
				</div>
		</div>

CENTER

function->footer();
