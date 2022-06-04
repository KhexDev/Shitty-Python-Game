class CoolUtils():
    
    def overlaping(sprite, target):
        xBool = False
        yBool = False

        if (sprite.x > target.x and sprite.x < target.x + target.daImage.get_width()):
            xBool = True
        if (sprite.y > target.y and sprite.y < target.y + target.daImage.get_height()):
            yBool = True

        return (xBool and yBool)

    def overlapingXY(target_x, target_y, x, y, target_width, target_height):
        xBool = False
        yBool = False

        if (x > target_x and x < target_x + target_x + target_width):
            xBool = True
        if (y > target_y and y < target_y + target_height):
            yBool = True

        return (xBool and yBool)