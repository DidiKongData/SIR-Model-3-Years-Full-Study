Attribute VB_Name = "Module1"
Sub Begin()
    
    Load UserForm1
    UserForm1.Show
    
    'Une fois que les paramètres de simulations sont entrées par l'utilisateur,
    'on peut lancer la simulation !
    
    'On voudrais afficher les paramètres choisis par l'utilisateur
    'sur la feuille Excel :
    
    Cells(1, 9).Value = "mu"
    Cells(1, 8).Value = "nu"
    Cells(1, 10).Value = "beta"
    Cells(1, 11).Value = "gamma"
    Cells(1, 12).Value = "Infectés % à t = 0"
    Cells(1, 13).Value = "Immunisés % à t = 0"
    Cells(1, 14).Value = "Mort % à t = 0"
    Cells(1, 15).Value = "Incubées % à t = 0"
    
    Dim beta As Double
    Dim gamma As Double
    
    Dim mu As Double
    Dim nu As Double
    
    Dim inf As Double
    Dim imm As Double
    Dim mort As Double
    
    'Au lieu d'utiliser de nouvelles variables globales,
    'on utilise ici les cases de la feuille Excel existante.
    
    beta = Cells(2, 10).Value 'Tx de transmission
    
    gamma = Cells(2, 11).Value 'Tx de guérison
    
    
    mu = Cells(2, 9).Value 'Tx de mortalité
    
    nu = Cells(2, 8).Value 'Temps moyen d'incubation
    
    
    inf = Cells(2, 12).Value 'Pourcentage d'infectés à t=0
    
    imm = Cells(2, 13).Value 'Pourcentage d'immunisés à t=0
    
    mort = Cells(2, 14).Value 'Pourcentage de mort à t=0
    
    incub = Cells(2, 15).Value 'Pourcentage d'incubées à t=0
    
    
    Dim N As Integer
    N = 3000 'Pop Totale
    
    Dim dt As Double
    dt = 0.01 ' Le pas différentiel
    '(indicateur de la précision de la solution graphique du système différentiel)
    
    
    
    ' Tableaux qui vont contenir les valeurs des populations par compartiments
    Dim S(1 To 10000)
    Dim I(1 To 10000)
    Dim R(1 To 10000)
    Dim M(1 To 10000)
    
    'Conditions initiales
    
    I(1) = N * (inf / 100) 'individus infectés à t=1
    R(1) = N * (imm / 100) 'individus guéris à   t=1
    M(1) = N * (mort / 100) 'individus mort à   t=1
    S(1) = N - I(1) - R(1) - M(1) 'individus sains à t=1
    
    'Résolution système différentiel : méthode d'Euler, approx de la dérivée par tangente
    'En dimension 3, "manipulations" des composantes du gradient (incrémentation composantes par composantes)
    For j = 1 To 10000 - 1
    
        'Calcul des dérivées locales
        Dim dS As Double
        dS = -beta * S(j) * I(j) / N
        
        Dim dI As Double
        dI = beta * S(j) * I(j) / N - gamma * I(j) - mu * I(j)
        
        Dim dR As Double
        dR = gamma * I(j)
        
        Dim dM As Double
        dM = mu * I(j)
        
        ' Incrémentation des valeurs (dS = (S(j+1)-S(j))/dt : taux de variation de la dérivation)
        S(j + 1) = S(j) + dt * dS
        I(j + 1) = I(j) + dt * dI
        R(j + 1) = R(j) + dt * dR
        M(j + 1) = M(j) + dt * dM
        
    
    Next j
    
    'Affichage résultats sur la plage de cellules excel
    
    Worksheets("SIR").Cells(1, 1).Value = "Temps"
    Worksheets("SIR").Cells(1, 2).Value = "Sain"
    Worksheets("SIR").Cells(1, 3).Value = "Infectés"
    Worksheets("SIR").Cells(1, 4).Value = "Rétablis"
    Worksheets("SIR").Cells(1, 5).Value = "Morts"
    Worksheets("SIR").Cells(1, 6).Value = "Incubées"
    
    For k = 1 To 10000
        Worksheets("SIR").Cells(k + 1, 1).Value = k * dt
        Worksheets("SIR").Cells(k + 1, 2).Value = S(k)
        Worksheets("SIR").Cells(k + 1, 3).Value = I(k)
        Worksheets("SIR").Cells(k + 1, 4).Value = R(k)
        Worksheets("SIR").Cells(k + 1, 5).Value = M(k)
    Next k

    ' Pour l'affichage du graphique, nous avons enregistrer une macro,
    ' effectuer les opérations qu'on voulait,
    ' puis on a repris le code enregistré dans la macro :
    
    Columns("A:F").Select
    ActiveSheet.Shapes.AddChart2(227, xlLine).Select
    ActiveChart.SetSourceData Source:=Range("SIR!$A:$F")
    ActiveChart.ChartColor = 13
    ActiveChart.FullSeriesCollection(1).IsFiltered = True
    ActiveChart.ClearToMatchStyle
    ActiveChart.ChartStyle = 233
    ActiveChart.ChartTitle.Select
    ActiveChart.ChartTitle.Text = "Modèle SEIRM"
    Selection.Format.TextFrame2.TextRange.Characters.Text = "Modèle SEIRM"
    With Selection.Format.TextFrame2.TextRange.Characters(1, 12).ParagraphFormat
        .TextDirection = msoTextDirectionLeftToRight
        .Alignment = msoAlignCenter
    End With
    With Selection.Format.TextFrame2.TextRange.Characters(1, 12).Font
        .BaselineOffset = 0
        .Bold = msoTrue
        .NameComplexScript = "+mn-cs"
        .NameFarEast = "+mn-ea"
        .Fill.Visible = msoTrue
        .Fill.ForeColor.RGB = RGB(242, 242, 242)
        .Fill.Transparency = 0
        .Fill.Solid
        .Size = 16
        .Italic = msoFalse
        .Kerning = 12
        .Name = "+mn-lt"
        .UnderlineStyle = msoNoUnderline
        .Spacing = 1
        .Strike = msoNoStrike
    End With
    ActiveChart.ChartArea.Select
    ActiveChart.SetElement (msoElementLegendTop)
    
End Sub
