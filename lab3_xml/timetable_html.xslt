<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">

<html>
    <head>
        <meta charset="utf-8"/> 
    </head>
    <body>
        <h2>Timetable for current week</h2>
        <table border="1">
            <tr bgcolor="#cccccc"> 
                <th style="text-align:left">Предмет</th>
                <th style="text-align:left">Аудитория</th>
                <th style="text-align:left">Преподаватель</th>
                <th style="text-align:left">Начало пары</th>
                <th style="text-align:left">Конец пары</th>
                <th style="text-align:left">Тип пары</th>
            </tr>
        <xsl:for-each select="Timetable/Day">
            <tr><td colspan="6"><b><xsl:value-of select="@Name" /></b></td></tr>

            <xsl:for-each select="Class"> 
            <tr>
                <td><xsl:value-of select="ClassName"/></td> 
                <td><xsl:value-of select="ClassRoom"/></td>
                <td><xsl:value-of select="Teacher"/></td>
                <td><xsl:value-of select="StartTime"/></td>
                <td><xsl:value-of select="EndTime"/></td>
                <td><xsl:value-of select="Type" /></td>
            </tr>
            </xsl:for-each>
        </xsl:for-each>
        </table>

    </body>
</html>

</xsl:template> 
</xsl:stylesheet>
