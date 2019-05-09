import subprocess

def increment():
	f = 'contribbot.py'
	r = open(f, 'r')
	lines = r.read().splitlines()
	penult = len(lines) - 2
	count = int(lines[penult])
	count += 1
	lines[penult] = str(count)
	r.close()
	w = open(f, 'w')
	w.write('\n'.join(lines))
	w.close()
	return count

def commit(msg):
	commands = [
		'git add .',
		'git commit -m \"' + str(msg) + '\"',
		'git status',
		'git push'
		]
	for command in commands:
		subprocess.call(command, shell=True)

if __name__ == '__main__':
	count = increment()
	commit('Commit #' + str(count))

''' times run:
107
'''