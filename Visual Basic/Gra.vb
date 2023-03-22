Public Class Form1

    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click
        'Obliczanie sumy liczb podanych przez użytkownika

        Dim num1, num2, sum As Integer

        'Pobieranie wartości z pól tekstowych
        num1 = Integer.Parse(txtNum1.Text)
        num2 = Integer.Parse(txtNum2.Text)

        'Obliczanie sumy
        sum = num1 + num2

        'Wyświetlanie wyniku w polu tekstowym
        txtResult.Text = sum.ToString()

    End Sub

    Private Sub btnClear_Click(sender As Object, e As EventArgs) Handles btnClear.Click
        'Czyszczenie pól tekstowych

        txtNum1.Text = ""
        txtNum2.Text = ""
        txtResult.Text = ""

    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        'Zamykanie aplikacji

        Me.Close()

    End Sub
End Class
