VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   8680.001
   ClientLeft      =   110
   ClientTop       =   450
   ClientWidth     =   15460
   OleObjectBlob   =   "UserFormExport.frx":0000
   StartUpPosition =   1  'CenterOwner
End
Attribute VB_Name = "UserForm1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False


Private Sub ParamButton_Click()

    'Mettre au m�me �tat et bouton et l'affichage de la frame des param�tres secondaires.
    ParamFrame.Visible = ParamButton.Value

End Sub

Private Sub ValidButton_Click()

    ' R�cup�ration des valeurs des diff�rentes TextBoxs
    Cells(2, 12) = InfectesText.Value
    Cells(2, 13) = RetablisText.Value
    Cells(2, 14) = MortText.Value
    Cells(2, 15) = IncubText.Value
    
    Cells(2, 10) = betaText.Value
    Cells(2, 11) = gammaText.Value
    Cells(2, 9) = muText.Value
    Cells(2, 8) = nuText.Value
    
End Sub


Private Sub MortTickBox_Click()

    'Mettre le m�me �tat du  sur l'affichage de la frame des param�tres secondaires.
    MortFrame.Visible = MortTickBox.Value
    muFrame.Visible = MortTickBox.Value

End Sub

Private Sub IncubTickBox_Click()

    IncubFrame.Visible = IncubTickBox.Value
    nuFrame.Visible = IncubTickBox.Value

End Sub


