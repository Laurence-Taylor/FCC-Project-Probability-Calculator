import copy
import random

class Hat:
    contents = []

    def __init__(self, **args):
        if len(args) == 0:
            raise TypeError(
                f"Tiene que depositar alguna bola en el sombrero."
            )
        balls = []
        # I move for each argument
        for color, amount in args.items():
            # Add each color to the list (creating the list)
            for i in range(amount):
                balls.append(color)
        self.contents = balls    
    
    def draw(self, amount):
        if amount > len(self.contents):
            amount = len(self.contents)
        # create list of balls to extract
        extracted_balls = []
        # extract each ball random
        for i in range(amount):
            to_get = random.randrange(0,len(self.contents))
            extracted_balls.append(self.contents[to_get])
            deleted_color = self.contents[to_get] # Comentar......
            del self.contents[to_get]
            #print('#',to_get) # Comentar......
            #print('color:',deleted_color)  # Comentar......
            #print(extracted_balls)  # Comentar......
            #print(self.contents)  # Comentar......
            #print()  # Comentar......
            #self.contents = tmp_hat_balls
        return extracted_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print()
    print(expected_balls)
    print()
    count=0
    list_expexted_ball = []
    for key, value in expected_balls.items():
        for _ in range(value):
            list_expexted_ball.append(key)
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        list_extracted_balls = hat_copy.draw(num_balls_drawn)
        tmp_list_expexted_ball = copy.deepcopy(list_expexted_ball)
        tmp_list_extracted_balls = copy.deepcopy(list_extracted_balls)
        for i in range(len(list_expexted_ball)):
            for j in range(len(tmp_list_extracted_balls)):
                if list_expexted_ball[i]==tmp_list_extracted_balls[j]:
                    to_delete=list_expexted_ball[i]
                    tmp_list_expexted_ball.remove(to_delete)
                    tmp_list_extracted_balls.remove(to_delete)
                    break      
        if tmp_list_expexted_ball==[]:
            count += 1
    if count == 0:
        return 0
    else:
        return round(count/num_experiments,5)


hat = Hat(black=6, red=4, green=3)

probability = experiment(hat=hat, expected_balls={'red':2,'green':1},num_balls_drawn=5, num_experiments=10)
print(probability)
