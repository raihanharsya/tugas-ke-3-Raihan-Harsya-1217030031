import pandas as pd
df = pd.DataFrame({
    'Posisi': ['1', '20', '30', '40', '50', '60'],
    'Kecepatan': ['5', '10', '15', '20', '25', '30'],
    'Percepatan': ['2', '4', '6', '8', '10', '12']
})

df.rename(columns={
    'Posisi': 'Posisi benda (m)',
    'Kecepatan': 'Kecepatan Benda (m/s)',
    'Percepatan' : 'Percepatan Benda (m^2/s)'
}, inplace=True)
df
