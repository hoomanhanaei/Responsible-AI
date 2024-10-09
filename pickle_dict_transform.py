import pandas as pd , numpy as np
import pickle


def skill_counter(file="user_skills.pkl"):
    # Load the data from the pickle file
    with open("user_skills.pkl", "rb") as file:
        data = pickle.load(file)
    # print(data)

    # Initialize an empty dictionary
    a_dict = {}
    # Iterate over each user and their corresponding skills
    for user, skills in data.items():
        # print(user)
        # print(skills)

        for skill in skills:
            # print(skill)
            # If the skill is not in the dictionary, add it with the user as the first value in a list.
            if skill not in a_dict:
                a_dict[skill] = 1
            # If the skill already exists, append the user to the existing list
            # or Increment the count for each skill
            else:
                a_dict[skill] += 1

            # break

        # break

    # print(a_dict)

    return a_dict


file = skill_counter()
df = pd.DataFrame.from_dict(file, orient="index")
df.columns = ["Number of People"]
df.index.name = "Skills"
# print(df)

with open("nfile.txt", "w") as file:
    file.write(df.to_string())

   


