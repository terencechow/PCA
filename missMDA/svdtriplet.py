def svdtriplet(X,roww=[],colw=[],ncp=np.inf):
	if hasattr(X,'pop'):
		X=np.array(X,float)
	elif hasattr(X,'shape'):
		X=X.astype(float)
	else:
		print "Please use a numpy array or a list!"
		return
	if roww==[]:
		roww = np.array(np.ones(X.shape[0])/X.shape[0],float)
	else:
		roww = np.array(roww,dtype=float)
	if colw==[]:
		colw = np.array(np.ones(X.shape[1]),float)
	else:
		colw = np.array(colw,dtype=float)

	ncp = min(ncp,X.shape[0]-1,X.shape[1])
	roww /= roww.sum()
	X *= np.sqrt(colw)
	X *= np.sqrt(roww[:,None])
	U = np.array([])
	s = np.array([])
	V = np.array([])

	if X.shape[1]<X.shape[0]:
		U, s, V = np.linalg.svd(X,full_matrices=False)
		V = V.T
		U = U[:,:ncp]
		V = V[:,:ncp]
		if ncp>1:
			mult = np.sign(V.sum(axis=0))
			mult[mult==0]=1
			U *= mult
			V *= mult
		U /= np.sqrt(roww[:,None])
		V /= np.sqrt(colw[:,None])
	else:
		V, s, U = np.linalg.svd(X.T,full_matrices=False)
		U = U.T
		U = U[:,:ncp]
		V = V[:,:ncp]
		mult = np.sign(V.sum(axis=0))
		mult[mult==0]=1	
		V *= mult
		U *= mult
		U /= np.sqrt(roww[:,None])
		V /= np.sqrt(colw[:,None])

	s = s[:min(X.shape[1],X.shape[0]-1)]
	num = s[:ncp] <1e-15
	if num.sum() >=1:
		U[:,num] *= s[num]
		V[:,num] *= s[num]

	return s,U,V