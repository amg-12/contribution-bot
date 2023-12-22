import subprocess

def increment():
	f = 'contribbot.py'
	r = open(f, 'r')
	lines = r.read().splitlines()
	r.close()
	count = int(lines[-2]) + 1
	lines[-2] = str(count)
	w = open(f, 'w')
	w.write('\n'.join(lines))
	w.close()
	return count

def commit(msg):
	commands = [
		'git add .',
		'git commit -m \"{}\"'.format(msg),
		'git push'
	]
	for command in commands:
		subprocess.call(command, shell=True)

if __name__ == '__main__':
	count = increment()
	commit('Commit #' + str(count))

''' times run:
263
'''