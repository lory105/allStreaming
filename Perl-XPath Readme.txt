# Esempio di codice per leggere tutti i film presenti nel DB

# salvo il percorso in cui si trova il file del DB da leggere
my $file="../xml/films.xml";

# creo un oggetto XPath e gli associo il file
my $xp = XML::XPath->new(filename => $file);


#my $query = "/collection/film[@id=1]";

#$xp->find()->get_nodelist;


# foreach my $book ($xp->find( $query )->get_nodelist){
# oppure
foreach my $book ($xp->find('//collection/film')->get_nodelist){
	print "ID:";
	print $book->findvalue('@id')."\n";			# stampo l'attributo id di film
	print "TITLE:";
        print $book->find('title')->string_value."\n"; 		# stampo un il tag title di film
        print "date:"; 
        print $book->find('date')->string_value."\n";
        print "\n";

#       print $book->findvalue(".")->string_value."\n";	# stampo tutti i tag di film uno sotto l'altro

} 
