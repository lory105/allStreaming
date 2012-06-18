#!/usr/bin/perl
# script riguardante le informazioni di allStreaming

use CGI;
use strict;
use warnings;
use function;
use CGI::Carp qw/fatalsToBrowser warningsToBrowser/;
use CGI::Session ( '-ip_match' );


function->header();
function->left("Chi Siamo");
function->right();


print<<CENTER;
<div id="aboutUs">

<h2>Film Gratis Online In STREAMING - AVVERTENZE:</h2> 
Questo e' un portale di appassionati cinefili. <strong>Nessun</strong> video &egrave; hostato sui server di AllStreaming. Tutti i link dei film sono presi prevalentemente da <a href="../www.videopremium.net">www.videopremium.net</a> e <a href="www.putlocker.com">www.putlocker.com</a> o altri portali simili; ci&ograve; rende il nostro sito molto veloce intuitivo, anche grazie all'utilizzo delle locandine che permettono di individuare e scegliere subito la visione da voi preferita indirizzandovi al filmato sui link sopra indicati, dove basta premere Play per visualizzare il tutto. <strong>Non diffondiamo nessun video</strong> in quanto non ne &egrave; permesso il download. <p><a href="index.cgi">www.allstreaming.com</a> - <b>Film in Streaming Gratis Online</b></p>

</div>
CENTER



function->footer();
