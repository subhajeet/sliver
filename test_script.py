import pexpect
import time





def main():
		start_time = time.time()
		sliver = pexpect.spawn('./sliver-server')
		sliver.sendline('help')
		sliver.sendline('exit')
		sliver.interact()
		sliver.sendcontrol('C')
		sliver.sendline('exit')
		print("--- %s seconds ---" % (time.time() - start_time))
		
		
		
		
if __name__ == '__main__':
	main()
		
