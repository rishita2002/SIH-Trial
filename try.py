import pandas as pd

df = pd.read_csv('eng.csv')
df['rando']='<br><br>'
del df['College']
del df['Serial']
del df['PRNo']

df.insert(loc = 2,
          column = 'r1',
          value = ', E-mail:')
df.insert(loc = 4,
          column = 'col1',
          value = ', Phone:')
print(df)
be_students = df[df['Class'] == 'BE']
te_students = df[df['Class'] == 'TE']
se_students = df[df['Class'] == 'SE']
# print(be_students)
# print(te_students)
# print(be_students)

f = open('be.txt', "a")
f.write('<link href="txtstyle.css" rel="stylesheet" type="text/css" />\n')
f.close()
be_students.to_csv(r'be.txt', header=None, index=None, sep='\t', mode='a')