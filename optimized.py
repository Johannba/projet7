import csv
import time
import matplotlib.pyplot as plt
import numpy as np

filename= "dataset1_Python+P7.csv"
filename2= "dataset2_Python+P7.csv"

actions=[] 
with open(filename,'r') as data: 
   for line in csv.reader(data):
       if line[1]=="price":
          continue
       element={}
       element["name"] = line[0]
            
       element["price"] = float(line[1])
       element["profit"] = float(line[2])
       if element["price"]> 0 and element["profit"] > 0 : 
             actions.append(element)
               
# print(actions[0:1])
   
actions2=[] 
with open(filename2,'r') as data: 
   for line in csv.reader(data):
       if line[1]=="price":
          continue
       element={}
       element["name"] = line[0]
            
       element["price"] = float(line[1])
       element["profit"] = float(line[2])
       if element["price"]> 0 and element["profit"] > 0 : 
             actions2.append(element)
               
def profit(actions):
    return actions['profit']
def price(actions):
    return actions['price']

def total_price(actions):
    Total_price=0
    for price in actions[0]:
        Total_price=Total_price+price['price']       
    return Total_price 


def total_profit(call_modif_key):
    Total_profit=0
    for profit in call_modif_key[0]:
        Total_profit=Total_profit+profit['profit']
    return Total_profit    
# print(total_profit(actions))
#algoritme glouton

def glouton(call_modif_key,price_max):
    start = time.time()
    table_triee=sorted(call_modif_key,key= profit, reverse=True)
    price_total=0
    #Algho glouton
    solution_gloutone=[]
    # i est égale à zéro
    i=0
    #tant qu'il reste des actions à traiter et que le prix max n'est pas atteint
    while i < len(table_triee) and price_total < price_max:
    #on prend la 1er action restante
        actions=table_triee[i]
        price_actions= price(actions)
        #si elle n'est pas trop chere (capacité restante suffisante)
        if price_total + price_actions <= price_max:
            #on l'ajoute à solution_gloutonne et on met à jour le prix total de la solution gloutonne
            solution_gloutone.append(actions)
            #mettre à jour le prix total
            price_total= price_total+price_actions
        #on passe à l'action suivante    
        i=i+1
    end = time.time()
    return solution_gloutone,end-start

solution_gloutonne=glouton(actions,500)
solution_gloutonne2=glouton(actions2,500)
# final_solution=total_price(solution_gloutonne)*total_profit(solution_gloutonne)/100
# final_solution2=total_price(solution_gloutonne2)*total_profit(solution_gloutonne2)/100
final_solution=(100*total_profit(solution_gloutonne))/total_price(solution_gloutonne)
final_solution2=(100*total_profit(solution_gloutonne2))/total_price(solution_gloutonne2)
# print("algho1")
# print(total_price(solution_gloutonne))
# print(final_solution)
# print("algho2")
# print(total_price(solution_gloutonne2))
# print(total_profit(solution_gloutonne))
# print(total_profit(solution_gloutonne2))
# print(final_solution2)
# print(solution_gloutonne2)

if __name__ == '__main__':
    times = []
    for i in range(len(actions)):
        time_val= glouton(actions[:i],500)
        times.append(time_val[1])
  
    
    x = [i for i in range(0,len(actions))]
    print(x)
    data_type = object
    x = np.array(x)
    y = np.array(times)
    plt.plot(x, y)

    plt.show()

