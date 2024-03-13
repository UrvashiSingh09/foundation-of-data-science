
# print('hello')
# list1 =  ['my','name','is','urvashi','singh']
# df =  pd.DataFrame(list1)
# print(df)

# import pandas as pd 
# list2 =  [10,30.4,'cactus','x']
# df =  pd.DataFrame(list2 , columns=['Tabular form'])
# print(df)

# import pandas as pd 
# data = pd.Series([1,1,1,2,2,3,3,4,0,5])
# # print(data.value_counts())
# print(data.value_counts(sort=True))

# dataset = {'grade' : ['A','B','A','A','C','B'], 
#                 "Name" : ["Harsh","Raj","Kanak","Suyash","Uma","Shima"],
#                 'Gender':['M','M','F','M','F','F']}
# df = pd.DataFrame(dataset)
# print(df)

# import pandas as pd
# data = {'X':[78, 85, 96, 80, 86], 'Y':[84, 94, 89, 83, 86], 'Z':[86, 97, 96, 72, 83]}
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# print(df)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# first_3_rows = df.head(3)
# print(first_3_rows)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# selected_columns = df[['name', 'score']]
# print(selected_columns)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# selected_rows = df[df['attempts'] >2]
# print(selected_rows)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# selected_rows = df[df['score'].isna()]
# print(selected_rows)

# import pandas as pd
# import numpy as np
# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#              'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# df = pd.DataFrame(exam_data, index=labels)
# mean_score = df['score'].mean()
# print("Mean score:", mean_score)

# import pandas as pd
# student_data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
#                  'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
#                  'marks': [200, 210, 190, 222, 199]}
# df1 = pd.DataFrame(student_data1)
# student_data2 = {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
#                  'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
#                  'marks': [201, 200, 198, 219, 201]}
# df2 = pd.DataFrame(student_data2)
# df3 = pd.concat([df1, df2], ignore_index=True)
# print(df3)

# import pandas as pd
# student_data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
#                  'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
#                  'marks': [200, 210, 190, 222, 199]}
# df1 = pd.DataFrame(student_data1)
# student_data2 = {'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
#                  'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
#                  'marks': [201, 200, 198, 219, 201]}
# df2 = pd.DataFrame(student_data2)
# df3 = pd.concat([df1, df2], axis=1)
# print(df3)

# import pandas as pd
# student_data1 = {'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
#                  'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
#                  'marks': [200, 210, 190, 222, 199]}
# df1 = pd.DataFrame(student_data1)
# new_rows = {'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 205}
# new_df = pd.DataFrame(new_rows, index=[0])
# df2 = df1.append(new_rows, ignore_index=True)
# print(df2)