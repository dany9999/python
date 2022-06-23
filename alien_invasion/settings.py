
class Settings:
    #a class to store all settings for Alien Invasion

    def __init__(self):    #initilize thge game's settings

        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.background_color = (0,0,0)
        
        #ship speed
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color= (255,255,255)
        self.bullets_allowed = 3