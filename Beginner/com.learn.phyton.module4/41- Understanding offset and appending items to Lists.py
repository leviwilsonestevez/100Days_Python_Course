states_of_america = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado",
                     "Connecticut",
                     "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
                     "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine",
                     "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
                     "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
                     "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota",
                     "Tennessee",
                     "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin",
                     "West Virginia",
                     "Wyoming"]

state = states_of_america[1]  # Alabama

print(f"The state {state} is selected using brakets index")
states_of_america.append("Port Rico")  # Add a new state
states_of_america.extend(["A", "B", "C"])  # Add a lot of new data

for state in states_of_america:
    print(state)
