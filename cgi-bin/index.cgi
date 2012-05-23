#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header(); 
function->left("home");
function->right();

print <<CENTER;
		<div id="center_side">
			
				<div id="random_film"><h1>Film Consigliati</h1>
						<div class="film">
							<img src="../images/sin-city.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Sin City</a>
						</div>
						<div class="film">
							<img src="../images/shining.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Shining</a>
						</div>

						<div class="film">
							<img src="../images/harry.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:Harry Potter</a>
						</div>
						<div class="film">
							<img src="../images/want.jpg" class="locandina" />
							</br>
							<a href="../film.html">Film:I want you</a>
						</div>
				</div>
		</div>

CENTER

function->footer();
