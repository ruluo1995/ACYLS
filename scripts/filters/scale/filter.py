import os
from common import FilterParameter, CustomFilterBase

class Filter(CustomFilterBase):

	def __init__(self):
		CustomFilterBase.__init__(self, os.path.dirname(__file__))
		self.name = "Scale"

		visible_tag = self.dull['visual'].find(".//*[@id='visible1']")
		self.param['scale'] = FilterParameter(visible_tag, 'transform', 'scale\((.+?)\) ', 'scale(%.2f) ')

		gui_elements = ("window", "scale")

		self.on_scale_changed = self.build_plain_handler('scale')

		self.gui_load(gui_elements)
		self.gui_setup()

	def gui_setup(self):
		self.gui['scale'].set_value(float(self.param['scale'].match()))
