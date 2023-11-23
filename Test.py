import math
class Point() :
    def __init__(self,x=0,y=0) :
        self.__x = x
        self.__y = y
    def get_abscisse(self) :
        return self.abscisse
    def get_ordonne(self) :
        return self.ordonne
    def set_abscisse(self,x) :
        self.__abscisse=x
    def set_ordonne(self,y) :
        self.__ordonne=y
    def distance(self,new_point):
        dx = self.__x - new_point.__x
        dy = self.__y - new_point.__y
        distance = math.sqrt(dx**2 + dy**2)
        return distance
    def norme(self):
        distance_origine = math.sqrt(self.__x**2 + self.__y**2)
        return distance_origine



