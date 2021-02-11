


def all_same(li: list) -> bool:
	if len(li) == 0:
		return True

	for i in range(len(li)):
		if li[i] != li[0]:
			return False

	return True


def dedup(li: list) -> list:
	if len(li) == 0:
		return [ ]

	dedup_list = [ ]

	for i in li:
		if i not in dedup_list:
			dedup_list.append(i)

	return dedup_list

def max_run(li) -> int:
	run_val = 1
	max_run_value = 1

	if len(li) == 0:
		return 0

	for i in range(len(li) - 1):
		if li[i + 1] == li[i]:
			run_val += 1
		else:
			run_val = 1

		if max_run_value < run_val:
			max_run_value = run_val

	return max_run_value