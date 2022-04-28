# 1776. Car Fleet II

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def get_simple_collision_time(p1, s1, p2, s2):
            return ((p2-p1)/(s1-s2))
        
        def get_dual_collision_time(col_time_prev_car, p1, s1, p2, s2, new_s1):
            dist_travelled_by_prev_car_before_col = s1 * col_time_prev_car
            new_p1 = p1 + dist_travelled_by_prev_car_before_col
            new_p2 = p2 + s2 * col_time_prev_car
            
            return col_time_prev_car + ((new_p2-new_p1)/(new_s1-s2))
        
        cars.reverse()
        number_cars = len(cars)
        after_col_speed = [y for x, y in cars]
        collision_time = [float('inf')] * number_cars
        
        for i in range(1, number_cars):
            if cars[i][1] > cars[i-1][1]:
                # current car speed > original speed of next car
                j = 1

                col_time = get_simple_collision_time(*cars[i-1], *cars[i])
                
                
                while col_time > collision_time[i-j]:
                    # prev car gets collided before this car collides with it, so compute with dual positions and speeds
                    col_time = get_dual_collision_time(collision_time[i-j], *cars[i-j], *cars[i], after_col_speed[i-j])
                    j += 1
                
                
                collision_time[i] = col_time
                after_col_speed[i] = after_col_speed[i-1]
            elif cars[i][1] > after_col_speed[i-1]:
                # current car speed > after collision speed of next car

                col_time = get_dual_collision_time(collision_time[i-1], *cars[i-1], *cars[i], after_col_speed[i-1])
                
                j = 2
                while col_time > collision_time[i-j]:
                    # prev car gets collided before this car collides with it, so compute with dual positions and speeds
                    col_time = get_dual_collision_time(collision_time[i-j], *cars[i-j], *cars[i], after_col_speed[i-j])
                    j += 1
                
                collision_time[i] = col_time
                after_col_speed[i] = after_col_speed[i-1]
            
        collision_time.reverse()
        
        return [x if x != float('inf') else -1 for x in collision_time]