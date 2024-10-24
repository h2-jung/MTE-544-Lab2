# Type of planner
from math import exp


POINT_PLANNER=0; TRAJECTORY_PLANNER=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        NUM_POINTS = 20
        
        # Parabolic Function
        parabolic_step = 1.5/NUM_POINTS
        p_xs = [i * parabolic_step for i in range(NUM_POINTS + 1)]
        trajectory = []
        for x in p_xs:
            trajectory.append([round(x, 3), round(x*x, 3)])
            
        # Sigmoid Function
        # sigmoid_step = 2.5/NUM_POINTS
        # s_xs = [i * sigmoid_step for i in range(NUM_POINTS + 1)]
        # trajectory = []
        # for x in s_xs:
        #     trajectory.append([round(x, 2), round(2/(1 + exp(-2*x))-1, 2)])
        
        return trajectory

def main():
     plan = planner(1)
     print(plan.plan())
     
if __name__=="__main__":
    main()
