class CoolUtils():
    
    def overlaping(sprite, target):
        xBool = False
        yBool = False

        if (sprite.x > target.x and sprite.x < target.x + target.daImage.get_width()):
            xBool = True
        if (sprite.y > target.y and sprite.y < target.y + target.daImage.get_height()):
            yBool = True

        return (xBool and yBool)