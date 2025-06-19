
from reportlab.platypus import Flowable 
from reportlab.graphics.shapes import Circle
from reportlab.lib.units import inch

class FullPageBar(Flowable):
    def __init__(self, color, height):
        Flowable.__init__(self)
        self.color = color
        self.height = height

    def draw(self):
        page_width = self.canv._pagesize[0]
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, page_width, self.height, fill=1, stroke=0)
        