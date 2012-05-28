<?xml version="1.0" encoding="UTF-8"?> 

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:a="http://www.prenotazioni.it"> 
<!-- xsl:output method='html' version='1.0' encoding='UTF-8' indent='yes' /> --> 



<xsl:template match="/">
<xsl:for-each select="collection/film">
		<xsl:sort select="normalize-space(substring(date,7,4))" order="descending" />
		<xsl:sort select="normalize-space(substring(date,4,2))" order="descending" />
		<xsl:sort select="normalize-space(substring(date,0,2))" order="descending" />
		<xsl:value-of select="title" />
	</xsl:for-each>
</xsl:template>


</xsl:stylesheet>



<!--
<xsl:template match="/">
	<xsl:for-each select="//collection/film">
		<xsl:sort order="date">
			Portfolio Name: <xsl:value-of select="title" />
		</xsl:sort>
	</xsl:for-each>
</xsl:template>


</xsl:stylesheet>
 -->