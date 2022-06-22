import time
import matplotlib.pyplot as plt
import numpy as np

data = [{"nom": "action1", "cout_par_action": 20, "bénéfice": 5},
        {"nom": "action2", "cout_par_action": 30, "bénéfice": 10},
        {"nom": "action3", "cout_par_action": 50, "bénéfice": 15},
        {"nom": "action4", "cout_par_action": 70, "bénéfice": 20},
        {"nom": "action5", "cout_par_action": 60, "bénéfice": 17},
        {"nom": "action6", "cout_par_action": 80, "bénéfice": 25},
        {"nom": "action7", "cout_par_action": 22, "bénéfice": 7},
        {"nom": "action8", "cout_par_action": 26, "bénéfice": 11},
        {"nom": "action9", "cout_par_action": 48, "bénéfice": 13},
        {"nom": "action10", "cout_par_action": 34, "bénéfice": 27},
        {"nom": "action11", "cout_par_action": 42, "bénéfice": 17},
        {"nom": "action12", "cout_par_action": 110, "bénéfice": 9},
        {"nom": "action13", "cout_par_action": 38, "bénéfice": 23},
        {"nom": "action14", "cout_par_action": 14, "bénéfice": 1},
        {"nom": "action15", "cout_par_action": 18, "bénéfice": 3},
        {"nom": "action16", "cout_par_action": 8, "bénéfice": 8},
        {"nom": "action17", "cout_par_action": 4, "bénéfice": 12},
        {"nom": "action18", "cout_par_action": 10, "bénéfice": 14},
        {"nom": "action19", "cout_par_action": 24, "bénéfice": 21},
        {"nom": "action20", "cout_par_action": 114, "bénéfice": 18}]


def brute_force(table_actions):
    start = time.time()
    combinations = []
    for i in range(2**len(table_actions)):
        binary = f"{{0:0{len(table_actions)}b}}".format(i)

        actions = []
        benefice = 0
        cout_action = 0
        for j in range(len(binary)):
            if binary[j] == "1":

                actions.append(table_actions[j])
        for action in actions:
            benefice += action["cout_par_action"] * (action["bénéfice"]/100)
            cout_action += action["cout_par_action"]

        if cout_action <= 500:
            element = {"actions": actions, "bénéfice": benefice}
            combinations.append(element)
    combinations.sort(key=lambda x: x["bénéfice"], reverse=True)
    print(combinations[0]["bénéfice"])
    end = time.time()
    return end - start


if __name__ == '__main__':
    times = []
    for i in range(20):
        time_val= brute_force(data[:i])
        times.append(time_val)

    x = [i for i in range(1, 21)]
    print(x)

    x = np.array(x)
    y = np.array(times)
    plt.plot(x, y)

    plt.show()
