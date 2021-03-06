from utils import LogHelper
from core.Module import Module
from modules.UserRequester.UserRequester import UserRequester

class UserRequesterModule(Module):

	server = None

	def __init__(self):
		super(self.__class__, self).__init__()
		self.server = UserRequester()

	def run(self, params, callback):
		self.MAX_PROCESSES = 1
		self.push(params, callback, self.run_queue)
		# super(self.__class__, self).run(params, callback)

	def run_queue(self, params, callback):
		LogHelper.log('EXECUTING ' + self.__class__.__name__, True)
		LogHelper.log('INPUT ' + self.__class__.__name__ + ' ' + str(params))
		LogHelper.log('PORT OPEN 0')
		output = {}
		LogHelper.log('OUTPUT ' + self.__class__.__name__ + ' ' + str(output))
		self.pop(params, output, callback)