# class Lights:
#     def __init__(self, first_light, second_light, last_light, current_light):
#         self.first_light = first_light
#         self.second_light = second_light
#         self.last_light = last_light
#         self.current_light = current_light
#
#     def show_lights(self):
#         print(f"Now the traffic light color is {self.current_light}")
#
#         if self.current_light == "red":
#             print("Please wait.")
#         elif self.current_light == "green":
#             print("You can go now.")
#         elif self.current_light == "yellow":
#             print("Get ready.")
#
# lights_obj = Lights("red", "green", "yellow", "yellow")
# lights_obj.show_lights()

# Ուրիշ տարբերակ

import time
class Lights:
    def __init__(self, first_light, second_light, last_light, current_light, cycle_counter):
        self.first_light = first_light
        self.second_light = second_light
        self.last_light = last_light
        self.current_light = current_light
        self.cycle_counter = cycle_counter

    def show_lights(self):
        print(f"Now the traffic light color is {self.current_light}")

        if self.current_light == "red":
            print("Please wait.")
        elif self.current_light == "green":
            print("You can go now.")
        elif self.current_light == "yellow":
            print("Get ready.")

    def change_light(self):
        if self.current_light == self.first_light:
            self.current_light = self.second_light
        elif self.current_light == self.second_light:
            self.current_light = self.last_light
        elif self.current_light == self.last_light:
            self.current_light = self.first_light

    def cycle(self):
        self.cycle_counter += 1

        if self.cycle_counter == 10:
            self.change_light()
            self.cycle_counter = 0


lights_obj = Lights("red", "green", "yellow", "red", 0)

for _ in range(30):
    lights_obj.show_lights()
    time.sleep(1)
    lights_obj.cycle()
