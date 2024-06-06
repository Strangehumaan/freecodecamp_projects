import pandas as pd


def calculate_demographic_data(print_data=True):

    df = pd.read_csv('C:/Users/Saad/Documents/Data analysis/Projects/Data/adult.data.csv')

    race_count = df['race'].value_counts()

    avg_men = round(df.loc[df['sex'] == 'Male','age'].mean(),1)

    percentage_with_bachelor_degree = round((len(df[df['education'] == 'Bachelors'])/len(df))*100,1)

    higher_education = ['Bachelors','Masters','Doctorate']
    mask = df['education'].isin(higher_education)
    higher_edu = df[mask]
    higher_edu_salary = higher_edu[higher_edu['salary'] == '>50K']
    percentage_with_avdance_and_50K = round((len(higher_edu_salary)/len(higher_edu)*100),1)

    lower_edu = df[~mask]
    lower_edu_salary = lower_edu[lower_edu['salary'] == '>50K']
    percentage_with_lower_and_50K = round((len(lower_edu_salary)/len(lower_edu))*100,1)

    min_hour = df['hours-per-week'].min()
    mask1 = (df['hours-per-week'] == min_hour) & (df['salary'] == '>50K')
    min_50K = df[mask1]


    country_percent = (df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100))
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent[highest_earning_country], 1)

  
    good_earn = df.loc[df['salary'] == '>50K', ['native-country', 'occupation']]
    mask3 = good_earn['native-country'] == 'India'
    india_highest_earners = good_earn[mask3]
    top_IN_occupation = india_highest_earners['occupation'].value_counts().idxmax()

   
    
    return {
        'race_count': race_count,
        'average_age_men': avg_men,
        'percentage_bachelors': percentage_with_bachelor_degree,
        'higher_education_rich': percentage_with_avdance_and_50K,
        'lower_education_rich': percentage_with_lower_and_50K,
        'min_work_hours': min_hour,
        'rich_percentage': min_50K,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
print(calculate_demographic_data())