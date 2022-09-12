
def ARE(nbr_mois):
    salaire_total = 0
    for i in range(nbr_mois) :
        salaire_mois=float(input())
        salaire_total += salaire_mois
    jours_calendaires=365*(nbr_mois/12)
    SJR1= ((0.404*salaire_total)+12.47)/jours_calendaires
    SJR2= (0.57*salaire_total)/jours_calendaires
    if SJR1>SJR2:
        SJR=SJR1
        ARE=30*SJR
        print('Ton salaire journalier de référence est de',round(SJR1))
        print('Ton allocation ARE est de',ARE)

    else:
        SJR=SJR2
        ARE=30*SJR
        print('Ton salaire journalier est de' ,round(SJR2),'euros')
        print('Ton allocation ARE est de', round(ARE),'euros')



nbr_mois= int(input('Nombre de mois travaillés:'))

ARE(nbr_mois)