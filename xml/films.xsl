<?xml version="1.0" encoding="UTF-8"?> 

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:a="http://www.prenotazioni.it"> 
<xsl:output method='text' version='1.0' encoding='UTF-8' indent='yes' /> 



<xsl:template match="/">
<xsl:for-each select="collection/film/date">
<xsl:sort select="." data-type="date" order="descending"/>
<xsl:if test="position() = 1">
<xsl:value-of select="."/>
</xsl:if>
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