# [('blood type', 'blood group')]
recipients = [['B1', 'Rh+', 'John'], ['B1', 'Rh-', 'Julette'], ['B2', 'Rh+', 'Lestat'], ['B2', 'Rh-', 'Flocky'],
              ['B3', 'Rh+', 'Creed'], ['B3', 'Rh-', 'Sam'], ['B4', 'Rh+', 'McLeod']]
             #['B2', 'Rh+']]
donors = [['B1', 'Rh+', 'Mary'], ['B3', 'Rh-', 'Dean'], ['B2', 'Rh-', 'Ragnar'], ['B3', 'Rh+', 'Logan'],
          ['B1', 'Rh-', 'Romeo'], ['B2', 'Rh+', 'Louis'], ['B4', 'Rh-', 'Koschey']]

non_ideal_couple = [[donor, recipient] for donor in donors for recipient in recipients if donor[0] == recipient[0]]
ideal_couple = [couple for couple in non_ideal_couple if couple[0][1] == couple[1][1]]

print(ideal_couple)
