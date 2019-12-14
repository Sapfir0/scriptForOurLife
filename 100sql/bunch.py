import random


def generation(arr: list, dlina: int) -> list:
	def generator(sgen: list, prev_index: int = -1):
		if len(sgen) < dlina:
			for i in range(prev_index + 1,len(arr)):
				sgen.append(arr[i])
				yield from generator(sgen, i)
				sgen.pop()
		else:
			yield sgen.copy()
	return [i for i in generator([])]


def generateRandomBunch(arr: list):
	bunch = random.choice(generation(arr, random.randrange(1, len(arr))))
	random.shuffle(bunch)
	return bunch