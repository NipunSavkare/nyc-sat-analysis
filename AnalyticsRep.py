import pandas as pd
import matplotlib.pyplot as plt
schools = pd.read_csv('schools.csv')
math_school=schools.sort_values(['average_math'],ascending=False)
best_math_school0=math_school[['school_name','average_math']]
best_math_school=best_math_school0[best_math_school0['average_math']>=640]
print(best_math_school)

schools['total_SAT'] = schools['average_math']+schools['average_reading']+schools['average_writing']

tot_sco=schools.sort_values(['total_SAT'],ascending=False)
top_10_schools=tot_sco[['school_name','total_SAT']].iloc[:10,:] 

print(top_10_schools)

largest_std_dev=schools.groupby('borough')['total_SAT'].agg(average_SAT='mean',num_schools='count',std_SAT='std')
largest_std_dev=largest_std_dev.round(2)
largest_std_dev=largest_std_dev.sort_values(['std_SAT'],ascending=False).head(1)
print(largest_std_dev)

std_df=schools.groupby('borough')['total_SAT'].agg(std_SAT='std')
plt.figure(figsize=(7,5))
plt.bar(std_df.index ,std_df['std_SAT'],color='lightgreen')


plt.title('Standard Deviation of Total SAT Scores by Borough')
plt.ylabel('Standard Deviation')
plt.xlabel('Borough')
plt.show()






