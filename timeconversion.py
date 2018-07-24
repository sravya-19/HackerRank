from datetime import datetime


@profile
def convert_to_time(s):
	time_24 = datetime.strptime(s, '%I:%M:%S%p').time()
	print(time_24)


if __name__ == '__main__':
	string = input()
	convert_to_time(string)
