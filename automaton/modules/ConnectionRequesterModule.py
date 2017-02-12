from core.Module import Module
from utils import LogHelper, LinkedinHelper
from utils.DatabaseHelper import DatabaseHelper
from modules.ConnectionRequester.ConnectionRequester import ConnectionRequester

class ConnectionRequesterModule(Module):

	DATABASE_TABLE = 'contacts'

	def run(self, params, callback):
		self.MAX_PROCESSES = 1
		self.push(params, callback, self.run_queue)

	def run_queue(self, params, callback):
		LogHelper.log('EXECUTING ' + self.__class__.__name__, True)
		LogHelper.log('INPUT ' + self.__class__.__name__ + ' ' + str(params))
		self.db = DatabaseHelper(table=self.DATABASE_TABLE)
		bot_email = params['bots']['email']
		sel = LinkedinHelper.clone_driver_wait(params['bots']['driver'])
		args = {'driver': sel}
		connection_requester = ConnectionRequester(args)
		def connection_requester_callback(url):
			self.db.update({'email':bot_email,'url':url},{'status':'INVITED'})
			output = {'accepted':[url]}
			LogHelper.log('OUTPUT ' + self.__class__.__name__ + ' ' + str(output))
			self.pop(params, output, callback)
		connection_requester.run(params, connection_requester_callback)