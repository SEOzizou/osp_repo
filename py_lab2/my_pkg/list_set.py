#!/usr/bin/python

def union_list(list_1, list_2):
	# list_1, list_2 : list type
	union = list(set(list_1+list_2))
	return union

def interset_list(list_1, list_2):
	# list_1, list_2 : list type
	intersection = [x for x in list_1 if x in list_2]
	return intersection
