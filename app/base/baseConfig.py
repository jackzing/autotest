import os,sys
class BaseConfig:
	siteConf = {}

	"""load setting from here"""
	def __init__(self, config = {}):
		if not isinstance(config, dict):
			raise BaseException("Error: please pass a dict parameter")
		self.config = config
		self._init()
		

	def load(self, stage = ''):
		self.loadExtraConf('setting.common')
		basePath = os.path.join(BaseConfig.siteConf['basePath'], 'setting', 'domain')
		if 'stage' in self.config.keys() and \
		os.path.isfile(os.path.join(basePath, self.config['stage'] + '.py')):
			"""befor load"""
			self.loadExtraConf('setting.domain.' + self.config['stage'])
			"""after load"""
		if len(stage) > 0 and \
		os.path.isfile(os.path.join(basePath,stage + '.py')):
			self.loadExtraConf('setting.domain.' + stage)
		return BaseConfig.siteConf

	def loadExtraConf(self, module):
		conf = __import__(module, fromlist=["*"])
		BaseConfig.siteConf = dict(BaseConfig.siteConf, **conf.siteConf)


	def getbasePath(self):
		basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
		return basePath

	def _init(self):
		basePath = self.getbasePath()
		BaseConfig.siteConf['basePath'] = basePath
		if basePath not in sys.path:
			print('adddd')
			sys.path.append(basePath)
# initializer when import
BaseConfig()
