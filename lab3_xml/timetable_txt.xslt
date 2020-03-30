<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:strip-space elements="Timetable/Day" />
<xsl:output method="text"/>

<xsl:template match="/">
<xsl:for-each select="Timetable/Day">
<xsl:value-of select="@Name" />:
<xsl:for-each select="Class"> 
<xsl:value-of select="ClassName"/>, <xsl:value-of select="ClassRoom"/>, <xsl:value-of select="Teacher"/>, <xsl:value-of select="StartTime"/>-<xsl:value-of select="EndTime"/>, <xsl:value-of select="Type" />. 
</xsl:for-each>
</xsl:for-each>
</xsl:template> 
</xsl:stylesheet>