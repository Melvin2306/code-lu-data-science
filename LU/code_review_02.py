#!/usr/bin/env python
# coding: utf-8

# Code Review 2
import seaborn as sns

df = sns.load_dataset('penguins')
df = df.dropna()
df.head(3)


# Example 1: Islands

# replace by a single line

islands = list(df['island'])

def find_island(name, list_of_islands):

  if name in list_of_names:
    return True
  else:
    return False

find_island('Biscoe', islands)


# Example 2: Group count

# How many female/male penguins are there?

# replace by a one-liner
female = df.loc[(df['sex'] == 'Female')]['sex'].count()
male = df.loc[(df['sex'] == 'Male')]['sex'].count()

female, male


# Example 3: Total penguin weight

# Which group of penguins is heavier in total?

# Can the code be simplified?
weight_ade = 0
weight_gentoo = 0

for i, j in df.iterrows():
    if df['species'][i] == 'Adelie':
        weight_ade += df['body_mass_g'][i]
    elif df['species'][i] == 'Gentoo':
        weight_gentoo += df['body_mass_g'][i]

weight_ade, weight_gentoo


# Example 4: Beak sizes

# longest 5 beaks of chinstrap penguins 

# Explain the code and make it more readable
df[df['species'] == 'Chinstrap'][:5].sort_values(by='bill_length_mm', ascending=False)


# Example 5: Any Dreams?

# explain the expression
df[df.eq("Dream").any(1)]
