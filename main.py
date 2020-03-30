import tkinter as tk
import backend
from backend import Database


database = Database()


def view_command():
    data_grid.delete(0, tk.END)
    for row in database.view():
        show_rows(row)

def find_by_name_command():
    data_grid.delete(0, tk.END)
    for row in database.find_by_name(team_name_text.get()):
        show_rows(row)

def find():
    data_grid.delete(0, tk.END)
    for row in database.view():
        if is_premier_league_true.get() == 1 and row[1] in backend.PREMIER_LEAGUE and goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
            show_rows(row)
        elif is_ligue_one_true.get() == 1 and row[1] in backend.LIGUE_ONE and goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
            show_rows(row)
        elif is_bundesliga_true.get() == 1 and row[1] in backend.BUNDESLIGA and goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
            show_rows(row)
        elif is_la_liga_true.get() == 1 and row[1] in backend.LA_LIGA and goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
            show_rows(row)
        elif is_serie_a_true.get() == 1 and row[1] in backend.SERIE_A and goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
            show_rows(row)
        elif is_premier_league_true.get() == 0 and is_ligue_one_true.get() == 0 and is_bundesliga_true.get() == 0 and is_la_liga_true.get() == 0 and is_serie_a_true.get() == 0:
            if goals_in_a_row_check(row, number_of_games_value.get(), goals_each_game_value.get(), less_or_more_value.get()):
                show_rows(row)

def close_command():
    database.__del__()
    root.quit()

def goals_convert(row):
    converted_list = []
    tmp_row = str(row[2])
    for item in tmp_row:
        if item.isdigit():
            converted_list.append(int(item))
    return converted_list


def average_goals(converted_list, games_num):
    return sum(converted_list[:games_num]) / len(converted_list[:games_num])

def goals_in_a_row_check(row, games_num, goals_each_game, less_or_more):
    x = goals_convert(row)
    tmp_goals = []
    for goal in range(len(x[:games_num])):
        if less_or_more == 1:
            if x[goal] >= float(goals_each_game):
                tmp_goals.append(x[goal])
                if len(tmp_goals) == games_num:
                    return True
        elif less_or_more == 0:
            if x[goal] <= float(goals_each_game):
                tmp_goals.append(x[goal])
                if len(tmp_goals) == games_num:
                    return True

def show_rows(row):
    good_looking_row = row[1] + " | " + str(goals_convert(row)) + f" | Last {len(goals_convert(row))} games"
    data_grid.insert(tk.END, good_looking_row)

root = tk.Tk()




show_all_btn = tk.Button(root, text="Show all records", command=view_command).grid(row=1, column=4)
find_btn = tk.Button(root, text="Find", command=find).grid(row=2, column=4)
find_by_name_btn = tk.Button(root, text="Find by name", command=find_by_name_command).grid(row=3, column=4)
exit_btn = tk.Button(root, text="Exit", command=close_command).grid(row=4, column=4)
search_by_name_label = tk.Label(root, text="Find by team name", anchor="e").grid(row=7, column=0)

team_name_text = tk.StringVar()
search_by_name_entry = tk.Entry(root, textvariable=team_name_text, width=16).grid(row=7, column=1)

most_popular_leagues_label = tk.Label(root, text="Check which leagues want you to filter:").grid(row=8, column=0, columnspan=2)

premier_league_label = tk.Label(root, text="Premier League").grid(row=9, column=0)
is_premier_league_true = tk.IntVar()
premier_league_checkbox = tk.Checkbutton(root, text="Choose", variable=is_premier_league_true).grid(row=9, column=1, sticky="w")


la_liga_label = tk.Label(root, text="LaLiga").grid(row=10, column=0)
is_la_liga_true = tk.IntVar()
la_liga_checkbox = tk.Checkbutton(root, text="Choose", variable=is_la_liga_true).grid(row=10, column=1, sticky="w")

bundesliga_label = tk.Label(root, text="Bundesliga").grid(row=11, column=0)
is_bundesliga_true = tk.IntVar()
bundesliga_checkbox = tk.Checkbutton(root, text="Choose", variable=is_bundesliga_true).grid(row=11, column=1, sticky="w")

serie_a_label = tk.Label(root, text="Serie A").grid(row=12, column=0)
is_serie_a_true = tk.IntVar()
serie_a_checkbox = tk.Checkbutton(root, text="Choose", variable=is_serie_a_true).grid(row=12, column=1, sticky="w")

ligue_one_label = tk.Label(root, text="Ligue 1").grid(row=13, column=0)
is_ligue_one_true = tk.IntVar()
ligue_one_checkbox = tk.Checkbutton(root, text="Choose", variable=is_ligue_one_true).grid(row=13, column=1, sticky="w")


goals_in_a_row_label = tk.Label(root, text="Find team by goals in a row").grid(row=14, column=0, columnspan=2)
number_of_games_label = tk.Label(root, text="Number of games").grid(row=15, column=0)
number_of_games_value = tk.IntVar()
number_of_games_entry = tk.Entry(root, textvariable=number_of_games_value).grid(row=15, column=1)

goals_each_game_label = tk.Label(root, text="Goals each game").grid(row=16, column=0, sticky="s")
goals_each_game_value = tk.StringVar()
goals_each_game_scale = tk.Scale(root, orient="horizontal", length=200, from_=0.0, to=5.0, resolution=0.50, variable=goals_each_game_value).grid(row=16, column=1)

less_or_more_value = tk.IntVar()
less_radio = tk.Radiobutton(root, text="Less <", variable=less_or_more_value, value=0).grid(row=17, column=0)
more_radio = tk.Radiobutton(root, text="More >", variable=less_or_more_value, value=1).grid(row=17, column=1)

data_grid_label = tk.Label(root, text="Team List",font=("Courier", 20)).grid(row=0, column=0, columnspan=2, ipady=10, padx=20)
data_grid = tk.Listbox(root, height=6, width=50)
data_grid.grid(row=1, column=0, rowspan=6, columnspan=2, padx=20)

sb1 = tk.Scrollbar(root)
sb1.grid(row=1, column=2, rowspan=6, padx=5)

data_grid.configure(yscrollcommand=sb1.set)
sb1.configure(command=data_grid.yview())

if __name__ == '__main__':
    root.title("Bet Helper")
    root.mainloop()