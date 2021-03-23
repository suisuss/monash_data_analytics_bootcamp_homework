Sub fun()
    
    For Each Sheet In Worksheets
        Dim Volume As Double
        Dim log_row As Integer
        log_row = 2
        Volume = 0
        
        
        LastRow = Sheet.Cells(Sheet.Rows.Count, "A").End(xlUp).Row
        
        Sheet.Cells(1, 9).Value = "Ticker"
        Sheet.Cells(1, 10).Value = "Yearly Change"
        Sheet.Cells(1, 11).Value = "Yearly Change Percentage"
        Sheet.Cells(1, 12).Value = "Total Volume"
        
        current_set_open = Sheet.Cells(2, 3).Value
    
    
            For i = 2 To LastRow
        
                ' Check if we are still within the same credit card brand, if it is not...
                If Sheet.Cells(i + 1, 1).Value <> Sheet.Cells(i, 1).Value And Sheet.Cells(i + 1, 3).Value <> 0 Then
                    ' Get set data
                    current_set_ticker = Sheet.Cells(i, 1).Value
                    current_set_close = Sheet.Cells(i, 6).Value
                    current_set_yearly_change = current_set_close - current_set_open
                    current_set_yearly_change_percentage = ((current_set_close - current_set_open) / current_set_open) * 100
                    
                    'Log set data
                    Sheet.Cells(log_row, 9).Value = current_set_ticker
                    Sheet.Cells(log_row, 10).Value = current_set_yearly_change
                    If current_set_yearly_change < 0 Then
                        Sheet.Cells(log_row, 10).Interior.ColorIndex = 3
                    ElseIf current_set_yearly_change > 0 Then
                        Sheet.Cells(log_row, 10).Interior.ColorIndex = 4
                    End If
                    Sheet.Cells(log_row, 11).Value = current_set_yearly_change_percentage
                    Sheet.Cells(log_row, 12).Value = Volume
                    
                    ' Setup for next set
                    log_row = log_row + 1
                    current_set_open = Sheet.Cells(i + 1, 3).Value
                    Volume = 0
                    
                Else
                    Volume = Cells(i, 7).Value + Volume
                    
                End If
            
            Next i

        max_percentage_change = WorksheetFunction.Max(Sheet.Range("k:k"))
        min_percentage_change = WorksheetFunction.Min(Sheet.Range("k:k"))
        max_volume_change = WorksheetFunction.Max(Sheet.Range("l:l"))
        Sheet.Cells(1, 13).Value = "Max Percentage Change"
        Sheet.Cells(1, 14).Value = "Min Percentage Change"
        Sheet.Cells(1, 15).Value = "Max Volume"
        Sheet.Cells(2, 13).Value = max_percentage_change
        Sheet.Cells(2, 14).Value = min_percentage_change
        Sheet.Cells(2, 15).Value = max_volume_change
    
    Next Sheet
        
End Sub


