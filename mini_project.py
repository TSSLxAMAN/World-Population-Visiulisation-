import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
dataset = pd.read_csv('population.csv')
df = pd.DataFrame(dataset)

while True:
    print("""
    1 = All countries population
    2 = Top 10 in 2022
    3 = Bottom 10 in 2022
    4 = Graph
""")
    userinput = int(input("Enter your choice : "))
    match userinput:
        case 1 : 
            print(df[["Rank","Country","Capital","2022 Population","2020 Population","2015 Population"]])

        case 2 :
            toprank = df.sort_values(by="Rank").head(10)
            print(toprank[["Rank","Country","2022 Population"]])
            top_populatoion = df.sort_values(by="2022 Population",ascending=False).head(10)
            x = top_populatoion["2022 Population"]
            y = top_populatoion["Country"]
            population = []
            name = []
            for i in y:
                name.append(i)
            for i in x:
                population.append(i)

            plt.bar(name,population)
            plt.xlabel("Country name")
            plt.ylabel("Poplation")
            plt.title("Population graph of top 10")
            plt.show()



        case 3 : 
            bottorank = df.sort_values(by="Rank").tail(10)
            print(bottorank[["Rank","Country","2022 Population"]])
            bottom_poputlation = df.sort_values(by="2022 Population",ascending=False).tail(10)
            x = bottom_poputlation["2022 Population"]
            y = bottom_poputlation["Country"]
            population = []
            name = []
            for i in y:
                name.append(i)
            for i in x:
                population.append(i)
            plt.bar(name,population)
            plt.xlabel("Country name")
            plt.ylabel("Poplation")
            plt.title("Population graph of bottom 10")
            plt.show()


        case 4 :
            x = pd.DataFrame(df,columns=["Country","1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population",'2020 Population','2022 Population'])
            first_country = input("Enter 1st country name : ")
            second_country = input("Enter 2nd country name : ")
            country1 = x.loc[x["Country"] == first_country.capitalize()]
            print(country1)
            country2 = x.loc[x["Country"] == second_country.capitalize()]
            print(country2) 
            country1 = country1.drop(columns=["Country"])
            country2 = country2.drop(columns=["Country"])
            country1_population = country1.values
            country2_population = country2.values
            result = country1_population.flatten()
            result2 = country2_population.flatten()
            year = ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population",'2020 Population','2022 Population']
            year2 = ["1970 Population","1980 Population","1990 Population","2000 Population","2010 Population","2015 Population",'2020 Population','2022 Population']
            print(np.shape(country1_population))
            print(country1_population)
            print(np.shape(country2_population))
            print(country2_population)
            from matplotlib import style
            style.use('ggplot')
            x = result
            x1 = result2
            y = year
            y1 = year2
            plt.plot(y1,x1,"m",label= second_country)
            plt.plot(y,x,"r",label= first_country)
            plt.xlabel("Years")
            plt.ylabel("Population")
            plt.title(f"Population comparison of {first_country} and {second_country}")
            plt.legend()
            plt.show()