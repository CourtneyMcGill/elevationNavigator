import numpy as np
import random



def generateDummyElevationMtrx(peak_elv, stop_side):
	peak = np.matrix(peak_elv)
	elv_mtx = buildBase(peak, ((peak_elv -1)/2), peak_elv -1, peak.shape[0], stop_side)

#	print "we back bitches"
#	print "here is the matrix:", elv_mtx
	np.savetxt("../datafiles/elevation.csv", elv_mtx, delimiter=",")


def buildBase(mat, min_height, max_height, side, stop_side):
	if side * 2 >= stop_side:
#		print "we done"
		return mat
	print "the min_height is", min_height
	print "the max_height is", max_height
#	print "the new size will be", side * 2
	bigger_mat = np.random.random_integers(min_height, max_height, (side * 2, side * 2))
	ins_h = random.randint(0, side)
	ins_w = random.randint(0, side)
	if side == 1:
		bigger_mat[np.ix_([ins_h], [ins_w])] = mat
#		print "did len 1"
	else:
#		print "the bit mat is:", bigger_mat
#		print "the mat to insert is:", mat
#		print "the insert h dimentsions are:", (ins_h, ins_h + side -1)
#		print "the insert w dimentsions are:", (ins_w, ins_w + side - 1)
		bigger_mat[ins_h: ins_h + side, ins_w: ins_w + side] = mat
#		bigger_mat[np.ix_([ins_h, ins_h + side -1], [ins_w, ins_w + side - 1])] = mat
#		print "did len", side
	return buildBase(bigger_mat, ((min_height-1) /2.0), min_height -1, side * 2, stop_side)


generateDummyElevationMtrx(19000, 130)




