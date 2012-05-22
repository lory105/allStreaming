#!/usr/bin/perl

use CGI;
use strict;
use warnings;
use function;

use Digest::MD5 qw(md5 md5_hex md5_base64);


# controlla se lo username e la password inseriti sono corretti


# recupero i valori inseriti nella form
my %input = function->take_form_values();


# controllare nel db la presenza dello username e in caso positivo ne restituisce la password che e criptata
my $crypted_password = function->get_password( $input{username} );

# verifico l'uguaglianza tra le due password
if( md5($input{password}) eq $crypted_password ){
# login ok

}
else{
# login non ok

}


# se il login va a buon fine carico la pagina con l'utente loggato, altrimenti no.


function->header();
function->left("home");
function->right();

print <<CENTER;
		<div id="center_side">
			<h1>Film Consigliati</h1>
				<div id="random_film">
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
