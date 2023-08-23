Function ObtenerValorCelda(nombreHoja As String, fila As Integer, columna As String) As Variant
    Dim valor As Variant
    Dim celda As Range
    
    ' Construir la referencia de la celda usando el nombre de la hoja, la fila y la columna
    Set celda = ThisWorkbook.Sheets(nombreHoja).Cells(fila, columna)
    
    ' Obtener el valor de la celda
    valor = celda.Value
    
    ' Devolver el valor de la celda
    ObtenerValorCelda = valor
End Function
