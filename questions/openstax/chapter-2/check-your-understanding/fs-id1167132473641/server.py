import random
def generate(data):
 camera=random.randint(12,30); farther=random.randint(4,12); back=random.randint(2,camera+farther-2); depth=camera+farther-back
 data["params"].update(camera_depth=camera,farther=farther,back=back); data["correct_answers"].update(distance=depth,displacement=-depth)
