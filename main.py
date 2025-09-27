import pandas as pd

df = pd.read_csv('/Users/marcusarocha/Downloads/World Important Dates.csv')
pd.set_option("display.max_columns", None)
df = df.drop(["Outcome", "Important Person/Group Responsible", "Affected Population", "Place Name"], axis=1)
df_filtered = df[df["Date"].str.isnumeric()]

gameLoop = True

while gameLoop:

    for events in df_filtered:

        random_row1 = df_filtered.sample(n=1)
        date_1 = int(random_row1["Year"].iloc[0])
        random_row2 = df_filtered.sample(n=1)
        date_2 = int(random_row2["Year"].iloc[0])

        if abs(date_2 - date_1) <= 21:
            break



    def check(answer):

        firstcomesfirst = date_1 > date_2

        if guess == "1" and firstcomesfirst or guess != "1" and not firstcomesfirst:
            return "Right"
        else:
            return  "Wrong"


    print("===============================")
    print("Which came first?")
    print("===============================\n")

    print(f"01. {random_row1["Name of Incident"].iloc[0]}")
    print(f"02. {random_row2["Name of Incident"].iloc[0]}")
    print("")

    guess = input("Your Guess (1/2): ")
    print(f"{check(guess)}\n\n")
