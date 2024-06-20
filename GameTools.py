# PACKAGES

from tkinter import *
from math import *
from time import *
from random import *

######################################################################

# CLASSES



class General_Methods:

    def __init__(self):
        pass

    
    # MATH

    def ConvertAngle(self, angle):

        # This is for converting the angle between math coordinate system and tkinter coordinate system (mutual)
        
        return (450 - angle) % 360



    def to_principal(self, angle):

        # Convert any arbitary angle to principle angle to help calculating and expressing
        
        return (angle + 180) % 360 - 180



    def calculate_distance(self, x1, y1, x2, y2):

        # distance between 2 points
        
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)



    def rotate_point(self, centerX, centerY, pointX, pointY, angle):

        # This is for rotating a point around a center point to some angle

        # Adjust the angle to follow the mathematical convention
        
        angle = 90 - angle
        if angle < 0:
            angle += 360

        # Convert the angle to radians to use trig
        
        angle = radians(angle)

        # Translate the point to the origin
        
        tempX = pointX - centerX
        tempY = pointY - centerY

        # Perform the rotation
        
        rotatedX = tempX * cos(angle) - tempY * sin(angle)
        rotatedY = tempX * sin(angle) + tempY * cos(angle)

        # Translate the point back to the original location
        
        finalX = rotatedX + centerX
        finalY = rotatedY + centerY

        return finalX, finalY


    #############################################################################

    # DRAW

    def draw_line_viaAngle(self, screen, startX, startY, angle, length, width, color):

        # Draw the line via a certain angle
        
        angle = radians(self.to_principal(angle)) # Turn it to radians to use the trig functions

        # calculate the end point coordinates
        endX = startX + length * cos(angle)
        endY = startY - length * sin(angle)
        line = screen.create_line(startX, startY, endX, endY, fill = color, width = width)

        return line



    def draw_oval(self, screen, centerX, centerY, hori_radius, vert_radius, fcol, ocol, width = 1):

        # This function only needs the center point, and the 2 neccessary radii

        x1 = centerX - hori_radius
        x2 = centerX + hori_radius
        y1 = centerY - vert_radius
        y2 = centerY + vert_radius

        return screen.create_oval(x1, y1, x2, y2, fill = fcol, outline = ocol, width = width)
    


    def draw_circle(self, screen, centerX, centerY, radius, fcol, ocol, width = 1):

        # Drawing the circle via the center point
        
        return self.draw_oval(screen, centerX, centerY, radius, radius, fcol, ocol, width)
    


    def draw_rectangle(self, screen, centerX, centerY, length, width, fcol, ocol, stroke = 1):

        # draw the rectangle via the center point, length, and width

        hori_radius = length/2
        vert_radius = width/2
        x1 = centerX - hori_radius
        x2 = centerX + hori_radius
        y1 = centerY - vert_radius
        y2 = centerY + vert_radius

        return screen.create_rectangle(x1, y1, x2, y2, fill = fcol, outline = ocol, width = stroke)



    def draw_square(self, screen, centerX, centerY, side_length, fcol, ocol, stroke = 1):

        # draw the square via the center point

        return self.draw_rectangle(screen, centerX, centerY, side_length, side_length, fcol, ocol, stroke)
    


    def draw_arrow(self, screen, centerX, centerY, length, direction, color):

        # Draw a horizontal arrow (consists of tail and head)

        width = length/4

        tail = self.draw_rectangle(screen, centerX - direction * width, centerY, length, width, color, color)

        # pre-calculate the coordinates for the triangle (the head)
        
        coordinates = [centerX + direction * width, centerY - width,
                       centerX + direction * width * 3, centerY,
                       centerX + direction * width, centerY + width]
        
        head = screen.create_polygon(*coordinates, fill = color, outline = color)

        return [tail, head]



    def draw_rotated_rectangle(self, screen, centerX, centerY, length, width, angle, col):
        
        # Calculate the 4 corners of the rectangle
        
        corners = []

        for dx, dy in [(-length / 2, -width / 2), (-length / 2, width / 2), (length / 2, width / 2), (length / 2, -width / 2)]:
            
            dx_rot = dx * cos(radians(angle)) + dy * sin(radians(angle))
            dy_rot = -dx * sin(radians(angle)) + dy * cos(radians(angle))  # Subtract instead of add because of the tkinter coordinates system
            corners.append((centerX + dx_rot, centerY + dy_rot))

        return screen.create_polygon(*corners, fill=col, outline=col)
    


    def draw_eye(self, screen, centerX, centerY, eyeball_width):

        # an outer empty oval surrounding the inside circle

        radius = eyeball_width/2

        eyeball = self.draw_circle(screen, centerX, centerY, radius, "DodgerBlue2", "DodgerBlue2")

        outer_part = self.draw_oval(screen, centerX, centerY, radius * 2, radius, "", "black", 2)

        return [eyeball, outer_part]
    

    
    def draw_spikes(self, screen, centerX, centerY, diameter, color, spikes_num = 10):

        # Calculate the radius

        radius = diameter / 2

        # Calculate the points for the outer and inner polygons

        points = []

        for i in range(spikes_num):  # Number of spikes

            angle = i * (2 * pi) / spikes_num # 2pi is 360 degrees
            outer_x = centerX + radius * cos(angle)
            outer_y = centerY + radius * sin(angle)
            inner_x = centerX + (radius / 2) * cos(angle + pi / spikes_num)
            inner_y = centerY + (radius / 2) * sin(angle + pi / spikes_num)
            points.extend([outer_x, outer_y, inner_x, inner_y])

        # Draw the outer and inner polygons

        return screen.create_polygon(*points, fill = color, outline = color)
    


    def draw_range_icon(self, screen, centerX, centerY, diameter):

        radius = diameter/2

        outer = self.draw_circle(screen, centerX, centerY, radius, "", "cornflower blue", diameter/10)

        arrow1 = self.draw_arrow(screen, centerX - radius * 0.4, centerY, radius * 0.5, -1, "orchid2")

        arrow2 = self.draw_arrow(screen, centerX + radius * 0.4, centerY, radius * 0.5, 1, "purple3")

        return [outer, arrow1, arrow2]



    def draw_explosion_icon(self, screen, centerX, centerY, diameter):

        outer_part = self.draw_spikes(screen, centerX, centerY, diameter, "tomato")

        inner_part = self.draw_spikes(screen, centerX, centerY, diameter * 0.6, "orange")

        return [outer_part, inner_part]
    

    
    def draw_resource_icon(self, screen, centerX, centerY, length):

        box = self.draw_rectangle(screen, centerX, centerY, length, length * 0.7, "", "brown3", length/20)

        circle = self.draw_circle(screen, centerX, centerY, length/4, "brown3", "brown3")

        plus_sign = screen.create_text(centerX + length * 0.8, centerY, text = "+", font = "Arial " + str(int(length * 0.6)), fill = "brown3")

        return [box, circle, plus_sign]
    


    def draw_shield(self, screen, x1, y1, length):

        stroke = length/6

        width = (length * 2)/3

        coordinates = [x1, y1,
                       x1 + width, y1,
                       x1 + width, y1 + length * 0.7,
                       x1 + width/2, y1 + length,
                       x1, y1 + length  * 0.7]
        
        return screen.create_polygon(*coordinates, fill = "green3", outline = "green4", width = stroke)
    


    def draw_sport_icon(self, screen, centerX, centerY, size, color="black"):
        
        # Calculate the points for the figure
        head_radius = size / 10
        body_length = size * 0.4
        leg_length = size / 3
        arm_length = size / 4
        width = size/20

        # Draw the head
        
        # Draw the head
        head = self.draw_circle(screen, centerX, centerY, head_radius, color, color)

        # Draw the body
        body = screen.create_line(centerX, centerY, centerX, centerY + body_length, fill=color, width = width)

        # Draw the legs
        leg1 = screen.create_line(centerX, centerY + body_length, centerX - leg_length / 2, centerY + body_length + leg_length, fill=color, width = width)
        leg2 = screen.create_line(centerX, centerY + body_length, centerX + leg_length / 2, centerY + body_length + leg_length, fill=color, width = width)

        # Draw the arms
        arm1 = screen.create_line(centerX, centerY + body_length / 2, centerX - arm_length, centerY + body_length / 2, fill=color, width = width)
        arm2 = screen.create_line(centerX, centerY + body_length / 2, centerX + arm_length, centerY + body_length / 2, fill=color, width = width)

        return [head, body, leg1, leg2, arm1, arm2]



    def draw_heal_icon(self, screen, centerX, centerY, width):

        stroke = width * 0.2

        line1 = screen.create_line(centerX, centerY - width * 0.4, centerX, centerY + width * 0.4, fill = "tomato", width = stroke)
        line2 = screen.create_line(centerX - width * 0.4, centerY, centerX + width * 0.4, centerY, fill = "tomato", width = stroke)

        outer_part = self.draw_square(screen, centerX, centerY, width, "", "tomato", width * 0.1)

        return [line1, line2, outer_part]
    


    def draw_gatlin_icon(self, screen, centerX, centerY, diameter):

        radius = diameter/2

        circle_base = self.draw_circle(screen, centerX, centerY, radius, "light goldenrod", "light goldenrod")

        arrow1 = self.draw_arrow(screen, centerX, centerY - radius * 0.5, radius * 0.7, 1, "red")
        arrow2 = self.draw_arrow(screen, centerX, centerY, radius * 0.7, 1, "red")
        arrow3 = self.draw_arrow(screen, centerX, centerY + radius * 0.5, radius * 0.7, 1, "red")

        return [circle_base, arrow1, arrow2, arrow3]



    def draw_captain_america(self, screen, centerX, centerY, diameter):

        radii = [diameter * (i/10) for i in range(5, 1, -1)]

        colors = ["red", "white", "red", "#0c4e80"]

        circles = [self.draw_circle(screen, centerX, centerY, radii[i], colors[i], colors[i]) for i in range(4)]

        star = self.draw_spikes(screen, centerX, centerY, 2 * radii[3], "white", 5)



    def fire_work_animation(self, screen, centerX, centerY, option, radius):

        # Color palettes
        palettes = [
        ["#F0EA65", "#0EF028", "#CBF065", "#F0D965", "#65F070"],
        ["#8D65F0", "#E865F0", "#BA65F0", "#656AF0", "#F065AB"]
        ]

        fps = 144
        number = 400

        pieces = [0 for _ in range(number)]
        colors = [choice(palettes[option - 1]) for _ in range(number)]
        angles = [uniform(-180, 180) for _ in range(number)]
        
        x_values = [centerX for _ in range(number)]
        y_values = [centerY for _ in range(number)]
        speeds = [uniform(0.2, radius//150) for _ in range(number)]
        xSpeeds = [speeds[i] * cos(radians(angles[i])) for i in range(number)]
        ySpeeds = [-1 * speeds[i] * sin(radians(angles[i])) for i in range(number)]

        for f in range(fps):
            for i in range(number):
                # Assuming self.draw_line_viaAngle is correctly defined
                pieces[i] = self.draw_line_viaAngle(screen, x_values[i], y_values[i], angles[i], radius/40, radius/80, colors[i])
                x_values[i] += xSpeeds[i]
                y_values[i] += ySpeeds[i]

            screen.update()
            sleep(1 / fps)
            # Assuming screen.delete is correctly defined and can take a list of items to delete
            screen.delete(*pieces)






class Ammunition:

    def __init__(self, x_pos, y_pos, shoot_range, LEFT_WALL, RIGHT_WALL, UP_WALL, DOWN_WALL):

        self.x, self.y = x_pos, y_pos
        self.angle = 0
        self.width = 10
        self.speed = 10

        self.active = False
        self.alive = True

        self.head, self.body = 0, 0
        
        self.shoot_range = shoot_range
        self.age = 0

        self.methods = General_Methods()

        self.LEFT_WALL = LEFT_WALL
        self.RIGHT_WALL = RIGHT_WALL
        self.UP_WALL = UP_WALL
        self.DOWN_WALL = DOWN_WALL
        


    def calculate_lifespan(self, target):

        D = self.methods.calculate_distance(self.x, self.y, target.x, target.y)

        if self.shoot_range < D:
            self.max_lifespan = ceil((self.shoot_range + 32)/self.speed)
        else:
            self.max_lifespan = ceil(D/self.speed)



    def draw(self, screen):

        if self.active:

            angle = self.methods.to_principal(self.angle)

            # Calculate the position of the head of the cannon
            head_x = self.x + (self.width) * cos(radians(angle))
            head_y = self.y - (self.width) * sin(radians(angle))  # Subtract instead of add

            # Draw the head of the cannon
            self.head = self.methods.draw_circle(screen, head_x, head_y, self.width/2, "orange", "orange")

            # Draw the body of the cannon
            self.body = self.methods.draw_rotated_rectangle(screen, self.x, self.y, 2 * self.width, self.width, angle, "orange")

        else:

            self.head, self.body = 0, 0



    def launch(self, angle):

        self.active = True
        self.angle = angle
    


    def move_update(self):
        new_x = self.x + self.speed * cos(radians(self.angle))
        new_y = self.y - self.speed * sin(radians(self.angle))

        if new_x - self.width/2 < self.LEFT_WALL or new_x + self.width/2 > self.RIGHT_WALL or \
        new_y - self.width/2 < self.UP_WALL or new_y + self.width/2 > self.DOWN_WALL:
            self.alive = False
            self.active = False
        else:
            self.x = new_x
            self.y = new_y
            if self.age >= self.max_lifespan:
                self.alive = False
                self.active = False
            else:
                self.age += 1



    def delete(self, screen):

        if self.head != 0 and self.body != 0:
            screen.delete(self.head, self.body)






class Tank:

    def __init__(self, id, special_technique, FPS, WIDTH, HEIGHT, LEFT_WALL, RIGHT_WALL, UP_WALL, DOWN_WALL):

        self.methods = General_Methods()

        self.FPS = FPS
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.LEFT_WALL = LEFT_WALL
        self.RIGHT_WALL = RIGHT_WALL
        self.UP_WALL = UP_WALL
        self.DOWN_WALL = DOWN_WALL

        self.id = id
        self.name = "Player " + str(id)
        self.special_technique = special_technique
        self.color1 = "blue4" if self.id == 1 else "forest green"
        self.color2 = "sky blue" if self.id == 1 else "green2"

        self.length = 40
        self.width = 40
        self.barrel_length = 32
        self.tire_length = self.length * 0.25
        self.tire_width = self.width * 0.2

        self.x = self.LEFT_WALL + 50 if self.id == 1 else self.RIGHT_WALL - 50
        self.y = self.UP_WALL + 50 if self.id == 1 else self.DOWN_WALL - 50
        self.speed = 2
        self.rotate_speed = 1
        self.angle = 0 if self.id == 1 else 180

        self.body = 0
        self.platform = 0
        self.barrel = 0
        self.shield = 0
        self.shoot_circle = 0
        self.tires = []

        self.shield_radius = 26
        self.fuel = 10000
        self.full_fuel = self.fuel
        self.live_points = 100
        self.ammunitions_num = 35
        self.ammunitions_used = 0
        self.ammunitions = []

        self.hurt = 6
        self.shoot_range = ceil(sqrt(self.WIDTH ** 2 + self.HEIGHT ** 2) / 5)
        self.attack_cooldown = 0
        self.attack_cooldown = 0 
        self.attack_interval = self.FPS // 3
        self.collide_cooldown = 0
        self.collide_interval = floor(self.FPS * 1.5)
        self.heal_cooldown = 0
        self.heal_interval = floor(self.FPS * 0.6)



    def set_enemy(self, enemy):

        self.set_enemy = enemy

        # Create the ammunitions after the enemy is set

        self.ammunitions = [Ammunition(self.x, self.y, self.shoot_range, self.LEFT_WALL, self.RIGHT_WALL, self.UP_WALL, self.DOWN_WALL) for _ in range(self.ammunitions_num)]



    def set_special_technique(self, technique_names):

        self.technique_name = technique_names[self.special_technique]

        if self.special_technique == 1:
            
            self.shoot_range *= 1.5
            
            for ammunition in self.ammunitions:

                ammunition.shoot_range = self.shoot_range


        elif self.special_technique == 2:
            
            self.hurt = int(1.5 * self.hurt)
            self.ammunitions_num -= 5
            self.ammunitions = [Ammunition(self.x, self.y, self.shoot_range, self.LEFT_WALL, self.RIGHT_WALL, self.UP_WALL, self.DOWN_WALL) for _ in range(self.ammunitions_num)]


        elif self.special_technique == 3:

            self.speed = floor(self.speed * 0.5)
            self.fuel = floor(self.fuel * 0.5)
            self.full_fuel = self.fuel
            self.shoot_range = floor(self.shoot_range * 0.7)

            for ammunition in self.ammunitions:

                ammunition.shoot_range = self.shoot_range


        elif self.special_technique == 4:
            
            self.ammunitions_num += 10

            # reset the ammunitions array

            self.ammunitions = [Ammunition(self.x, self.y, self.shoot_range, self.LEFT_WALL, self.RIGHT_WALL, self.UP_WALL, self.DOWN_WALL) for _ in range(self.ammunitions_num)]


        elif self.special_technique == 5:

            self.speed //= 2
            self.fuel //= 2
            self.full_fuel = self.fuel


        elif self.special_technique == 6:
            
            self.fuel = ceil(self.fuel * 1.5)
            self.full_fuel = self.fuel
            self.speed = ceil(self.speed * 1.5)
            self.rotate_speed = ceil(self.speed * 1.5)


        elif self.special_technique == 8:

            self.technique_name = "Gatlin"
            self.attack_interval /= 2



    def display_technique_icon(self, screen):

        parameters1 = [40, 60, 35]
        parameters2 = [self.WIDTH - 40, self.HEIGHT - 60, 35]

        if self.id == 1:

            if self.special_technique == 1:

                self.methods.draw_range_icon(screen, *parameters1)

            elif self.special_technique == 2:

                self.methods.draw_explosion_icon(screen, *parameters1)

            elif self.special_technique == 3:

                self.methods.draw_eye(screen, 40, 60, 20)

            elif self.special_technique == 4:

                self.methods.draw_resource_icon(screen, *parameters1)

            elif self.special_technique == 5:

                self.methods.draw_shield(screen, 30, 40, 35)

            elif self.special_technique == 6:

                self.methods.draw_sport_icon(screen, *parameters1, "purple")

            elif self.special_technique == 7:

                self.methods.draw_heal_icon(screen, *parameters1)

            elif self.special_technique == 8:

                self.methods.draw_gatlin_icon(screen, *parameters1)


        else:

            if self.special_technique == 1:

                self.methods.draw_range_icon(screen, *parameters2)

            elif self.special_technique == 2:

                self.methods.draw_explosion_icon(screen, *parameters2)

            elif self.special_technique == 3:

                self.methods.draw_eye(screen, self.WIDTH - 40, self.HEIGHT - 60, 20)

            elif self.special_technique == 4:

                self.methods.draw_resource_icon(screen, *parameters2)

            elif self.special_technique == 5:

                self.methods.draw_shield(screen, self.WIDTH - 50, self.HEIGHT - 80, 35)

            elif self.special_technique == 6:

                self.methods.draw_sport_icon(screen, *parameters2, "purple")

            elif self.special_technique == 7:

                self.methods.draw_heal_icon(screen, *parameters2)

            elif self.special_technique == 8:

                self.methods.draw_gatlin_icon(screen, *parameters2)



    def draw_display_panels(self, screen):

        fuel_length = 0 if self.fuel == 0 else (self.fuel/self.full_fuel) * 100

        if self.id == 1:

            self.name_display = screen.create_text(40, 25, text = self.name, font = "Arial 12", fill = self.color1)
            
            self.live_box = screen.create_rectangle(80, 15, 180, 30, fill = "", outline = self.color1, width = 3)
            self.live_bar = screen.create_rectangle(80, 15, 80 + self.live_points, 30, fill = self.color2)
            self.live_display = screen.create_text(200, 25, text = str(self.live_points), font = "Arial 10", fill = self.color1)

            self.fuel_text = screen.create_text(280, 25, text = str(self.fuel) + " mL fuel", font = "Arial 10", fill = self.color1)
            self.fuel_box = screen.create_rectangle(340, 15, 440, 30, fill = "", outline = "black", width = 3)
            self.fuel_bar = screen.create_rectangle(340, 15, 340 + fuel_length, 30, fill = self.color2)

            self.ammunitions_text = screen.create_text(520, 25, text = "Ammunitions: " + str(self.ammunitions_num), font = "Arial 10", fill = self.color1)

            self.technique_text = screen.create_text(150, 55, text = self.technique_name, font = "Arial 12 bold", fill = "tomato")



        
        else:

            self.name_display = screen.create_text(self.WIDTH - 40, self.HEIGHT - 25, text = self.name, font = "Arial 12", fill = self.color1)

            self.live_box = screen.create_rectangle(self.WIDTH - 180, self.HEIGHT - 30, self.WIDTH - 80, self.HEIGHT - 15, fill = "", outline = self.color1, width = 3)
            self.live_bar = screen.create_rectangle(self.WIDTH - 180, self.HEIGHT - 30, self.WIDTH - 180 + self.live_points, self.HEIGHT - 15, fill = self.color2)
            self.live_display = screen.create_text(self.WIDTH - 200, self.HEIGHT - 25, text = str(self.live_points), font = "Arial 10", fill = self.color1)

            self.fuel_text = screen.create_text(self.WIDTH - 280, self.HEIGHT - 25, text = str(self.fuel) + " mL fuel", font = "Arial 10", fill = self.color1)
            self.fuel_box = screen.create_rectangle(self.WIDTH - 440, self.HEIGHT - 30, self.WIDTH - 340, self.HEIGHT - 15, fill = "", outline = "black", width = 3)
            self.fuel_bar = screen.create_rectangle(self.WIDTH - 440, self.HEIGHT - 30, self.WIDTH - 440 + fuel_length, self.HEIGHT - 15, fill = self.color2)

            self.ammunitions_text = screen.create_text(self.WIDTH - 520, self.HEIGHT - 25, text = "Ammunitions: " + str(self.ammunitions_num), font = "Arial 10", fill = self.color1)

            self.technique_text = screen.create_text(self.WIDTH - 150, self.HEIGHT - 55, text = self.technique_name, font = "Arial 12 bold", fill = "tomato")



    def draw(self, screen, frames):
        
        # Every second it show up it should consume fuel
        if frames % self.FPS == 0 and self.fuel > 0:

            self.fuel -= 1
        
        # TANK COMPONENTS

        self.body = self.methods.draw_rotated_rectangle(screen, self.x, self.y, self.length, self.width, self.angle, self.color2)
        self.platform = self.methods.draw_rotated_rectangle(screen, self.x, self.y, self.length * 0.6, self.width * 0.6, self.angle, self.color1)

        self.endX = self.x + self.barrel_length * cos(radians(self.angle))
        self.endY = self.y - self.barrel_length * sin(radians(self.angle))  # Subtract instead of add because of tkinter angle system
        
        self.barrel = screen.create_line(self.x, self.y, self.endX, self.endY, fill = self.color1, width = 7)
        
        # Draw the tires

        # Calculate the unrotated positions of corners of the tank
        half_length = self.length / 2
        half_width = self.width / 2
        corners = [
            (self.x - half_length, self.y - half_width),
            (self.x - half_length, self.y + half_width),
            (self.x + half_length, self.y - half_width),
            (self.x + half_length, self.y + half_width)
        ]

        # Rotate and draw the tires at the corners

        self.tires = [] # reset it to empty every time
        for ox, oy in corners:
            x, y = self.methods.rotate_point(self.x, self.y, ox, oy, self.angle)
            self.tires.append(self.methods.draw_rotated_rectangle(screen, x, y, self.tire_length, self.tire_width, self.angle, self.color1))
        
        
        # Draw the display panels

        self.draw_display_panels(screen)

        
        # "ACCESSIBILITY" STUFF
        
        # self.shield = draw_circle(self.x, self.y, self.shield_radius, "", "gray")


        # At the first 15 seconds, the game will give each player their shooting range

        if frames > 0 and frames <= self.FPS * 15:

            self.shoot_circle = self.methods.draw_circle(screen, self.x, self.y, self.shoot_range, "", "orange")

    

    def draw_ammunitions(self, screen):

        # Draw the munitions atop the components (better)

        for ammunition in self.ammunitions:
            if ammunition.active:
                ammunition.draw(screen)



    def check_slight_collision(self, x, y):
        
        if (x - self.shield_radius < self.LEFT_WALL - 1 or x + self.shield_radius > self.RIGHT_WALL + 1 or
                y - self.shield_radius < self.UP_WALL - 1 or y + self.shield_radius > self.DOWN_WALL + 1):
            
            return True
        
        if self.enemy is not None:
            distance = self.methods.calculate_distance(x, y, self.enemy.x, self.enemy.y)
            if distance < self.shield_radius + self.enemy.shield_radius - 1:
                return True
        
        return False
    


    def check_rigid_collision(self, x, y):
        
        if (x - self.shield_radius <= self.LEFT_WALL or x + self.shield_radius >= self.RIGHT_WALL or
                y - self.shield_radius <= self.UP_WALL or y + self.shield_radius >= self.DOWN_WALL):
            
            return True
        
        if self.enemy is not None:
            distance = self.methods.calculate_distance(x, y, self.enemy.x, self.enemy.y)
            if distance <= self.shield_radius + self.enemy.shield_radius:
                return True
        
        return False



    def collision_penalty(self):

        if self.check_rigid_collision(self.x, self.y):
        
            if self.collide_cooldown == 0:
                if self.live_points > 0:
                    self.live_points -= 1
                self.collide_cooldown = self.collide_interval  # Reset the cooldown



    def heal_handler(self):

        # Increase self heal cooldown

        if self.heal_cooldown < self.heal_interval:

            self.heal_cooldown += 1

        else:

            if self.live_points < self.heal_interval:

                self.live_points += 1

                self.heal_cooldown = 0


    
    def go(self):

        if self.fuel - self.speed >= 0:

            # Calculate new position
            new_x = self.x + self.speed * cos(radians(self.angle))
            new_y = self.y - self.speed * sin(radians(self.angle))  # Subtract instead of add
            
            # Check collision and handle movement
            if not self.check_slight_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
                # Consume petrol
                self.fuel -= self.speed

                if self.special_technique == 7:
                    self.heal_handler()



    def go_back(self):

        if self.fuel - self.speed >= 0:
            # Calculate new position
            new_x = self.x - self.speed * cos(radians(self.angle))
            new_y = self.y + self.speed * sin(radians(self.angle))  # Add instead of subtract
            
            # Check collision and handle movement
            if not self.check_slight_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
                # Consume petrol
                self.fuel -= self.speed
            
                if self.special_technique == 7:
                    self.heal_handler()



    def rotate(self):
        self.angle = self.methods.to_principal(self.angle + self.rotate_speed)



    def counter_rotate(self):
        self.angle = self.methods.to_principal(self.angle - self.rotate_speed)



    def calculate_absolute_angle(self):

        cx, cy = self.WIDTH/2, self.HEIGHT/2

        x1 = self.x - cx if self.x >= cx else (-1) * (cx - self.x)
        y1 = cy - self.y if self.y <= cy else (-1) * (self.y - cy)
        x2 = self.enemy.x - cx if self.enemy.x >= cx else (-1) * (cx - self.enemy.x)
        y2 = cy - self.enemy.y if self.enemy.y <= cy else (-1) * (self.enemy.y - cy)

        return degrees(atan2(y2 - y1, x2 - x1))
    


    def check_shoot_success(self):

        cx, cy = self.WIDTH/2, self.HEIGHT/2

        x1 = self.x - cx if self.x >= cx else (-1) * (cx - self.x)
        y1 = cy - self.y if self.y <= cy else (-1) * (self.y - cy)
        x2 = self.enemy.x - cx if self.enemy.x >= cx else (-1) * (cx - self.enemy.x)
        y2 = cy - self.enemy.y if self.enemy.y <= cy else (-1) * (self.enemy.y - cy)

        D = self.methods.calculate_distance(x1, y1, x2, y2)

        K, R = self.shoot_range, self.enemy.shield_radius

        # print(D - R)

        if self.special_technique == 3:

            return True if K >= D - R else False
        
        else: 

            if K < D - R:
                return False

            elif K == D - R:
                angle = degrees(atan2(y2 - y1, x2 - x1))

                return True if self.angle == angle else False

            elif D - R < K < D:

                angle1 = degrees(atan2(y2 - y1, x2 - x1)) - degrees(acos((D**2 + K**2 - R**2) / (2 * D * K)))
                angle2 = degrees(atan2(y2 - y1, x2 - x1)) + degrees(acos((D**2 + K**2 - R**2) / (2 * D * K)))
                
                # print(angle1, self.angle, angle2)

                return True if self.angle >= min(angle1, angle2) and self.angle <= max(angle1, angle2) else False

            else:

                angle1 = degrees(atan2(y2 - y1, x2 - x1)) - degrees(asin(R / D))
                angle2 = degrees(atan2(y2 - y1, x2 - x1)) + degrees(asin(R / D))
                
                # print(angle1, angle2)

                return True if self.angle >= min(angle1, angle2) and self.angle <= max(angle1, angle2) else False
    

        
    def attack(self):

        if self.attack_cooldown <= 0 and self.fuel >= 30:

            # Every time the barrel works, it will consume energy (fuel in the tank)

            self.fuel -= 30

            if self.ammunitions_num > 0:

                if self.special_technique == 3:

                    self.ammunitions[self.ammunitions_used].launch(self.calculate_absolute_angle())

                else: 
                
                    self.ammunitions[self.ammunitions_used].launch(self.angle)

                self.ammunitions_num -= 1
                self.ammunitions_used += 1

                # print(self.check_shoot_success())

                if self.check_shoot_success():

                    hurt = self.hurt if self.enemy.special_technique != 5 else floor(self.hurt * 2/3)
                    
                    if self.enemy.live_points - hurt <= 0:
                        self.enemy.live_points = 0
                    else:
                        self.enemy.live_points -= hurt

                self.attack_cooldown = self.attack_interval # reset



    def update(self, enemy):

        # Update the enemy info
        self.enemy = enemy
        
        
        for ammunition in self.ammunitions:

            # Update the max lifespan for each munition

            ammunition.calculate_lifespan(self.enemy)

            # if active, update position to animate; if not, update position with the tank

            if ammunition.active:
                ammunition.move_update()
            else:
                ammunition.x = self.x
                ammunition.y = self.y

        

        # Decrease attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Monitor collision and give penalty if applicable

        self.collision_penalty()

        # Decrease collision cooldown
        if self.collide_cooldown > 0:
            self.collide_cooldown -= 1



    def delete(self, screen):

        screen.delete(self.body, self.platform, self.barrel)
        screen.delete(*self.tires)

        if self.shield is not None:

            screen.delete(self.shield)

        if self.shoot_circle is not None:

            screen.delete(self.shoot_circle)

        screen.delete(self.name_display, self.live_box, self.live_bar, self.live_display)
        screen.delete(self.fuel_text, self.fuel_box, self.fuel_bar)
        screen.delete(self.ammunitions_text)
        screen.delete(self.technique_text)

        for munition in self.ammunitions:
            munition.delete(screen)






class Game:

    def __init__(self):

        self.myInterface = Tk()

        self.methods = General_Methods()

        self.WIDTH = 650
        self.HEIGHT = round((4/5) * self.WIDTH / 50) * 50
        self.LEFT_WALL, self.RIGHT_WALL = 80, self.WIDTH - 80
        self.UP_WALL, self.DOWN_WALL = 80, self.HEIGHT - 80
        self.BACKGROUND_COL = "#FAF0DC"
        self.FPS = 144
        self.screen_widths = {

            "Chromebook" : 650,
            "Small Laptop" : 800,
            "Big Laptop" : 1000,
            "Desktop" : 1200,

        }


        self.menu_screen = 0
        self.game_screen = 0

        self.keys_pressed = {
            "a": False, 
            "d": False, 
            "w": False, 
            "s": False, 
            "Left": False, 
            "Right": False, 
            "Up": False, 
            "Down": False, 
            "g" : False, 
            "m" : False, 
            }

        self.tank1 = 0
        self.tank2 = 0
        self.technique1, self.technique2 = 0, 0


        self.technique_names = {

            0 : "Don't need anything",
            1 : "Long Shooter",
            2 : "Furious Shooter",
            3 : "Auto-Aiming",
            4 : "Resource God",
            5 : "Juggernaut",
            6 : "Sport Champion",
            7 : "Self Heal",
            8 : "Gatlin"

        }

        self.technique_descriptions = {

            1 : "Longer shoot range",
            2 : "Greater shoot hurt, but fewer ammunitions",
            3 : "The tank aims the opponent for you, but slower speed and shorter shoot range",
            4 : "10 more ammunitions",
            5 : "Less than 70 % hurt when being hit, but also half speed",
            6 : "Greater speed, fuel, and rotating speed -> More flexible",
            7 : "Recover live points when you move",
            8 : "Greater shooting frequency possible"

        }

        self.rules_descriptions = [

            "Tanks start with 100 live points; reaching 0 means losing.",
            "A normal tank has 35 ammunitions for shooting.",
            "Fuel begins at 10,000 mL for a normal tank.",
            "Fuel is consumed by moving (1 mL/pixel), shooting, and time (1 mL/second).",
            "The normal shooting range is 1/4 of the screen.",
            "Normal tanks lose 6 points per hit and 1 point every 1.5 seconds when colliding.",
            "One (or none) special technique can be chosen by each player.",
            "*The Captain America Shields are simply for asthetics (No actual impacts)"

        ]
        
        self.operations1 = [
            
            "Player 1",
            "W - Go forward",
            "S - Go back",
            "A - Rotate counterclockwise",
            "D - Rotate clockwise",
            "G - Attack"
            
            ]
            
        self.operations2 = [
            
            "Player 2",
            "Up - Go forward",
            "Down - Go back",
            "Left - Rotate counterclockwise",
            "Right - Rotate clockwise",
            "M - Attack"
            
            ]


        self.player_turn = 1
        self.game_running = False

        self.endgame_texts = {

            1 : "Player 2 wins!",
            2 : "Player 1 wins!",
            3 : "Both run out of fuel. Draw!"

        }

        self.button_fg = "yellow"
        self.button_bg = "brown4"
        self.active_bg = "hot pink"



    # SCREENSIZE SELECTIONS



    def initialize_game_screen(self):

        self.HEIGHT = round((4/5) * self.WIDTH / 50) * 50
        self.LEFT_WALL, self.RIGHT_WALL = 80, self.WIDTH - 80
        self.UP_WALL, self.DOWN_WALL = 80, self.HEIGHT - 80

        self.game_screen = Canvas(self.myInterface, width = self.WIDTH, height = self.HEIGHT, background = self.BACKGROUND_COL)
        self.game_screen.pack()



    def show_screensize_select(self):
        
        self.menu_screen = Canvas(self.myInterface, width = 300, height = 300, bg = self.BACKGROUND_COL)
        self.menu_screen.pack()

        self.menu_screen.create_text(150, 25, text = "Welcome!", font = "Arial 12 bold italic")
        self.menu_screen.create_text(150, 50, text = "Please choose your computer type", font = "Arial 10")

        x, y = 150, 85
        for key, value in self.screen_widths.items():
            self.create_button(key, value, x, y)
            y += 50  # Adjust y-coordinate for next button


        self.menu_screen.mainloop()


    
    def on_screensize_click(self, value):

        self.WIDTH = value

        self.menu_screen.destroy()

        self.initialize_game_screen()

        self.startApplication()



    def create_button(self, key, value, x, y):
        
        button = Button(self.menu_screen, text = key, font = "Arial 9 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command = lambda : self.on_screensize_click(value))
        self.menu_screen.create_window(x, y, window = button)



    # BEFORE GAME GREETINGS & PREP


    
    def show_rules(self):

        self.game_screen.delete("all")
        self.game_screen.create_text(self.WIDTH/2, 25, text="Rules", font = "Arial 16 bold")


        for i in range(len(self.rules_descriptions)):

            self.game_screen.create_text(40, 70 + i * 40, text = self.rules_descriptions[i], font = "Arial 11", anchor = W)


        self.back_button = Button(self.game_screen, text="Back", font = "Arial 10 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.back_to_homescreen)
        self.game_screen.create_window(self.WIDTH - 50, self.HEIGHT - 50, window=self.back_button)
        
        
    
    def show_operations(self):
        
        self.game_screen.delete("all")
        self.game_screen.create_text(self.WIDTH/2, 25, text="Operations", font="Arial 16 bold")
        
        for i in range(len(self.operations1)):
            
            font = "Arial 13 bold" if i == 0 else "Arial 11" 
            
            self.game_screen.create_text(self.WIDTH/4, 70 + i * 40, text = self.operations1[i], font = font)
            self.game_screen.create_text(self.WIDTH * 3/4, 70 + i * 40, text = self.operations2[i], font = font)

        self.back_button = Button(self.game_screen, text="Back", font = "Arial 10 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.back_to_homescreen)
        self.game_screen.create_window(self.WIDTH - 50, self.HEIGHT - 50, window=self.back_button)

    

    def show_techniques(self):

        self.game_screen.delete("all")
        self.game_screen.create_text(self.WIDTH/2, 25, text="Special Techniques", font="Arial 16 bold")


        for i in range(1, 9):

            self.game_screen.create_text(self.WIDTH/2, 20 + i * 50, text = self.technique_names[i], font = "Arial 12")
            self.game_screen.create_text(self.WIDTH/2, 38 + i * 50, text = self.technique_descriptions[i], font = "Arial 10", fill = "blue")


        self.back_button = Button(self.game_screen, text="Back", font = "Arial 10 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.back_to_homescreen)
        self.game_screen.create_window(self.WIDTH - 50, self.HEIGHT - 50, window=self.back_button)



    def back_to_homescreen(self):
        self.game_screen.delete("all")
        self.startApplication()



    def startApplication(self):

        self.game_screen.create_text(self.WIDTH/2 - 145, self.HEIGHT * 0.3, text="TANK", fill = "dodger blue", font="Arial 50 bold")
        self.game_screen.create_text(self.WIDTH/2 + 145, self.HEIGHT * 0.3, text="BATTLE", fill = "forest green", font="Arial 50 bold")
        self.game_screen.create_text(self.WIDTH/2, self.HEIGHT * 0.55, text="(Press space to play game, press Esc to quit)", font="Arial 16 italic")  
        
        self.rules_button = Button(self.game_screen, text="Rules", font = "Arial 12 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.show_rules)
        self.game_screen.create_window(self.WIDTH/2, self.HEIGHT - 150, window=self.rules_button)
        
        self.operations_button = Button(self.game_screen, text="Operations", font = "Arial 12 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.show_operations)
        self.game_screen.create_window(self.WIDTH/2, self.HEIGHT - 100, window=self.operations_button)
        
        self.special_techniques_button = Button(self.game_screen, text="Special Techniques", font = "Arial 12 bold", fg=self.button_fg, bg=self.button_bg, activebackground=self.active_bg, command=self.show_techniques)
        self.game_screen.create_window(self.WIDTH/2, self.HEIGHT - 50, window=self.special_techniques_button)
        
        self.game_screen.bind('<space>', self.startGame)
        self.game_screen.bind('<Escape>', self.quitGame)
        self.game_screen.focus_set()



    def startGame(self, event):

        if not self.game_running:

            self.game_screen.delete("all")
            self.rules_button.destroy()
            self.operations_button.destroy()
            self.special_techniques_button.destroy()
            self.player_turn = 1
            self.technique_selection()



    def technique_selection(self):

        self.technique_buttons = []

        for i in range(9):

            font = "Arial 11 bold italic" if i == 0 else "Arial 11 bold"
            fg = "red3" if i == 0 else "medium blue"

            button = Button(self.game_screen, text=str(self.technique_names[i]), font = font, fg = fg, bg="light salmon", activebackground="maroon1", command=lambda i=i: self.on_technique_click(i))
            self.technique_buttons.append(button)
            self.game_screen.create_window(self.WIDTH/2, 75 + i * 45, window = button)

        # Add instructions for the players
        player_name = "First" if self.player_turn == 1 else "Second"
        color = "dodger blue" if self.player_turn == 1 else "forest green"
        self.select_instructions = self.game_screen.create_text(self.WIDTH/2, 25, text=f"{player_name} player, please choose technique", fill = color, font="Arial 12 bold")



    def on_technique_click(self, technique):

        if self.player_turn == 1:

            self.technique1 = technique

            self.player_turn = 2 # Switch to the second player after assigning

            # Remove player 1's buttons and instructions

            for button in self.technique_buttons: button.destroy()

            self.game_screen.delete(self.select_instructions)
            self.technique_buttons.clear()

            # Show player 2's buttons
            self.technique_selection()

        
        else:

            self.technique2 = technique

            # Remove player 2's buttons and instructions
            for button in self.technique_buttons: button.destroy()

            self.game_screen.delete(self.select_instructions)
            self.technique_buttons.clear()


            # Start the game
            self.game_running = True
            self.runGame()



    def setTanks(self):

        self.tank1 = Tank(1, self.technique1, self.FPS, self.WIDTH, self.HEIGHT, self.LEFT_WALL, self.RIGHT_WALL, self.UP_WALL, self.DOWN_WALL)
        self.tank2 = Tank(2, self.technique2, self.FPS, self.WIDTH, self.HEIGHT, self.LEFT_WALL, self.RIGHT_WALL, self.UP_WALL, self.DOWN_WALL)

        self.tank1.set_enemy(self.tank2)
        self.tank2.set_enemy(self.tank1)
        self.tank1.set_special_technique(self.technique_names)
        self.tank2.set_special_technique(self.technique_names)



    # KEY CONTROL


    def keyDownHandler(self, event):

        self.keys_pressed[event.keysym] = True



    def keyUpHandler(self, event):

        self.keys_pressed[event.keysym] = False


    
    def operationsControl(self):

        if self.keys_pressed["a"]:
            self.tank1.rotate()

        if self.keys_pressed["d"]:
            self.tank1.counter_rotate()

        if self.keys_pressed["w"]:
            self.tank1.go()

        if self.keys_pressed["s"]:
            self.tank1.go_back()

        if self.keys_pressed["Left"]:
            self.tank2.rotate()

        if self.keys_pressed["Right"]:
            self.tank2.counter_rotate()

        if self.keys_pressed["Up"]:
            self.tank2.go()

        if self.keys_pressed["Down"]:
            self.tank2.go_back()

        if self.keys_pressed["g"]:
            self.tank1.attack()

        if self.keys_pressed["m"]:
            self.tank2.attack()



    def game_bindings(self):

        self.game_screen.bind("<Key>", self.keyDownHandler)
        self.game_screen.bind("<KeyRelease>", self.keyUpHandler)

        self.game_screen.focus_set()



    # POST-GAME



    def checkEndGame(self):

        if self.tank1.live_points == 0:

            return 1

        if self.tank2.live_points == 0:

            return 2
        
        if self.tank1.fuel == 0 and self.tank2.fuel == 0:

            return 3
        
        return 0
    

    
    def endgame_process(self):

        text_positions = [self.WIDTH/2, self.HEIGHT/2]

        self.tank1.draw_display_panels(self.game_screen)
        self.tank2.draw_display_panels(self.game_screen)

        if self.checkEndGame() > 0 and self.checkEndGame() < 3:

            self.methods.fire_work_animation(self.game_screen, self.WIDTH/2, self.HEIGHT/2, self.checkEndGame(), (self.WIDTH - 160)/2)

        endgame_text = self.endgame_texts[self.checkEndGame()]

        self.game_screen.create_text(*text_positions, text = endgame_text, font = "Arial 20 bold")

        self.hint_text = self.game_screen.create_text(self.WIDTH/2, self.HEIGHT/2 + 50, text="(Press space to return to homepage, Press Esc to quit)", font = "Arial 12")
        self.game_screen.bind('<space>', self.replayGame)
        self.game_screen.bind('<Escape>', self.quitGame)
        self.game_screen.focus_set()



    # GAME ENVIRONMENT DRAWINGS


    
    def draw_walls(self):

        self.game_screen.create_rectangle(self.LEFT_WALL, self.UP_WALL, self.RIGHT_WALL, self.DOWN_WALL, fill = "#F5DEB3", width = 5)



    def draw_background(self):

        y = self.UP_WALL + 30

        while y < self.DOWN_WALL - 30:

            self.methods.draw_captain_america(self.game_screen, 40, y, 35)
            self.methods.draw_captain_america(self.game_screen, self.WIDTH - 40, y, 35)

            y += 40


    # GENERAL RUNNINGS



    def quitGame(self, event):

        self.game_screen.delete("all")

        self.game_screen.create_text(self.WIDTH/2, self.HEIGHT/2, text = "It's so sad to say goodbye", font = "Arial 30 bold", fill = "tomato")
        self.game_screen.create_text(self.WIDTH/2, self.HEIGHT * 0.7, text = "See you in the next battle!", font = "Arial 20 bold", fill = "orange")

        self.game_screen.update()
        sleep(3)

        self.myInterface.quit()



    def replayGame(self, event):
        self.game_screen.delete("all")
        self.startApplication()



    def runGame(self):

        self.game_bindings()
        self.setTanks()

        self.draw_walls()
        self.draw_background()
        self.tank1.display_technique_icon(self.game_screen)
        self.tank2.display_technique_icon(self.game_screen)


        f = 0

        while True:

            self.operationsControl()

            self.tank1.draw(self.game_screen, f)
            self.tank2.draw(self.game_screen, f)
            self.tank1.draw_ammunitions(self.game_screen)
            self.tank2.draw_ammunitions(self.game_screen)


            self.tank1.update(self.tank2)
            self.tank2.update(self.tank1)
            self.game_screen.update()

            sleep(1 / self.FPS)

            self.tank1.delete(self.game_screen)
            self.tank2.delete(self.game_screen)

            f += 1



            if self.checkEndGame() > 0:
                self.game_running = False
                break

        
        self.endgame_process()



    def runApplication(self):
        self.show_screensize_select()


#####################################################################